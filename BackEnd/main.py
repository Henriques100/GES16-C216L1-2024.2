from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
import time
import asyncpg
import os

# Função para obter a conexão com o banco de dados PostgreSQL
async def get_database():
    DATABASE_URL = os.environ.get("PGURL", "postgres://postgres:postgres@db:5432/esportivos")
    return await asyncpg.connect(DATABASE_URL)

# Inicializar a aplicação FastAPI
app = FastAPI()

# Modelo para adicionar novos esportivos
class Esportivo(BaseModel):
    id: Optional[int] = None
    tipo: str
    modelo: str
    empresa: str
    quantidade: int
    preco: float
    
class EsportivoBase(BaseModel):
    tipo: str
    modelo: str
    empresa: str
    quantidade: int
    preco: float
    
# Modelo para venda de esportivos
class VendaEsportivo(BaseModel):
    quantidade: int 
    
# Modelo para atualizar atributos de um esportivo (exceto o ID) 
class AtualizarEsportivo(BaseModel):
    tipo: Optional[str] = None
    modelo: Optional[str] = None
    empresa: Optional[str] = None
    quantidade: Optional[int] = None
    preco: Optional[float] = None
    
# Middleware para logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time    
    print(f"Path: {request.url.path}, Method: {request.method}, Process Time: {process_time:.4f}s")
    return response

# Função para verificar se o esportivo existe usado tipo e modelo   
async def esportivo_existe(tipo: str, modelo: str, conn: asyncpg.Connection):
    try:
      query = "SELECT * FROM esportivos WHERE LOWER(tipo) = LOWER($1) AND LOWER(modelo) = LOWER($2)"
      result = await conn.fetchval(query, tipo, modelo)
      return result is not None
    except Exception as e:
      raise HTTPException(status_code=500, detail=f"Falha ao verificar se o esportivo existe: {str(e)}")
    
# 1. Adicionar um novo esportivo
@app.post("/api/v1/esportivos/", status_code=201)
async def adicionar_esportivo(esportivo: EsportivoBase):
    conn = await get_database()
    if await esportivo_existe(esportivo.tipo, esportivo.modelo, conn):
       raise HTTPException(status_code=400, detail="Esportivo já existe.")
    try:
        query = "INSERT INTO esportivos (tipo, modelo, empresa, quantidade, preco) VALUES ($1, $2, $3, $4, $5)"
        async with conn.transaction():
            result = await conn.execute(query, esportivo.tipo, esportivo.modelo, esportivo.empresa, esportivo.quantidade, esportivo.preco)
            return {"message": "Esportivo adicionado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Falha ao adicionar o esportivo: {str(e)}")
    finally:
        await conn.close()
        
# 2. Listar todos os esportivos
@app.get("/api/v1/esportivos/", response_model=List[Esportivo])
async def listar_esportivos():
    conn = await get_database()
    try:
        # Buscar todos os esportivos no banco de dados
        query = "SELECT * FROM esportivos"
        rows = await conn.fetch(query)
        esportivos = [dict(row) for row in rows]
        return esportivos
    finally:
        await conn.close()

# 3. Buscar esportivo por ID
@app.get("/api/v1/esportivos/{esportivo_id}")
async def listar_esportivo_por_id(esportivo_id: int):
    conn = await get_database()
    try:
     # Buscar o esportivo por ID 
     query = "SELECT * FROM esportivos WHERE id = $1"
     esportivo = await conn.feychrow(query, esportivo_id)
     if esportivo is None:
        raise HTTPException(status_code=404, detail="Esportivo não encontrado.")
     return dict(esportivo)
    finally:
        await conn.close()

# 4. Vender um esportivo (reduzir quantidade no estoque)
@app.put("/api/v1/esportivos/{esportivo_id}/vender/")
async def vender_esportivo(esportivo_id: int, venda: VendaEsportivo):
    conn = await get_database()
    try:
        # Verificar se o esportivo existe
        query = "SELECT * FROM esportivos WHERE id = $1"
        esportivo = await conn.fetchrow(query, esportivo_id)
        if esportivo is None:
            raise HTTPException(status_code=404, detail="Esportivo não encontrado.")
       
        # Verificar se a quantidade solicitada está disponível
        if esportivo['quantidade'] < venda.quantidade:
            raise HTTPException(status_code=400, detail="Quantidade solicitada não está disponível.")
        
        # Atualizar a quantidade no banco de dados
        nova_quantidade = esportivo['quantidade'] - venda.quantidade
        update_query = "UPDATE esportivos SET quantidade = $1 WHERE id = $2"
        await conn.execute(update_query, nova_quantidade, esportivo_id)
        
        # Calcular o valor total da venda
        valor_venda = esportivo['preco'] * venda.quantidade
        # Registrar a venda na tabela de vendas
        insert_venda_query = """
        INSERT INTO vendas (esportivo_id, quantidade_vendida, valor_venda)
        VALUES ($1, $2, $3)
        """
        await conn.execute(insert_venda_query, esportivo_id, venda.quantidade, valor_venda) 
        
        # Criar um novo dicionário com os dados atualizados
        esportivo_atualizado = dict(esportivo)
        esportivo_atualizado['quantidade'] = nova_quantidade
        
        return {"message": "Venda realizada com sucesso!", "esportivo": esportivo_atualizado}
    finally:
        await conn.close()
        
# 5. Atualizar atributos de um esportivo pelo ID (exceto o ID)
@app.patch("/api/v1/esportivos/{esportivos_id}")
async def atualizar_esportivo(esportivo_id: int, esportivo_atualizado: AtualizarEsportivo):
    conn = await get_database()
    try:
        # Verificar se o esportivo existe
        query = "SELECT * FROM esportivos WHERE id = $1"
        esportivo = await conn.fetchrow(query, esportivo_id)
        if esportivo is None:
            raise HTTPException(status_code=404, detail="Esportivo não encontrado.")
                    
         # Atualizar apenas os campos fornecidos
        update_query = """
            UPDATE esportivos
            SET tipo = COALESCE($1, tipo),
                modelo = COALESCE($2, modelo),
                empresa = COALESCE($3, empresa),
                quantidade = COALESCE($4, quantidade),
                preco = COALESCE($5, preco),
            WHERE id = $6    
        """
        await conn.execute(
            update_query,
            esportivo_atualizado.tipo,
            esportivo_atualizado.modelo,
            esportivo_atualizado.empresa,
            esportivo_atualizado.quantidade,
            esportivo_atualizado.preco,
            esportivo_id
            )
        return {"message": "Esportivo atualizado com sucesso"}
    finally:
        await conn.close()
        
# 6. Remover um esportivo pelo ID
@app.delete("/api/v1/esportivos/{esportivos_id}")
async def remover_esportivo(esportivo_id: int):
    conn = await get_database()
    try:
        # Verificar se o esportivo existe
        query = """
        SELECT * FROM esportivos WHERE id = $1
        """
        esportivo = await conn.fetchrow(query, esportivo_id)
        if esportivo is None:
            raise HTTPException(status_code=404, detail="Esportivo não encontrado.")
        
        # Remover o esportivo do banco de dados
        delete_query = "DELETE FROM esportivos WHERE id = $1"
        await conn.execute(delete_query, esportivo_id)
        return {"message": "Esportivo removido com sucesso!"}
    finally:
        await conn.close()
        
# 7. Resetar banco de dados de esportivos
@app.delete("/api/v1/esportivos/")
async def resetar_esportivos():
    init_sql = os.getenv("INIT_SQL", "db/init.sql")
    conn = await get_database()
    try:
        # Read SQL file contents
        with open(init_sql, 'r') as file:
            sql_commands = file.read()
        # Execute SQL commands
        await conn.execute(sql_commands)
        return {"message": "Banco de dados limpo com sucesso!"}   
    finally:
        await conn.close()
        
# 8. Listar vendas
@app.get("/api/v1/vendas")
async def listar_vendas():
    conn = await get_database()
    try:
        # Buscar todas as venda no banco de dados
        query = "SELECT * FORM vendas"
        rows = await conn.fetch(query)
        vendas = [dict(row) for row in rows]
        return vendas
    finally:
        await conn.close()