from fastapi import Body, FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
import time

# Inicializar o repositório de produtos esportivos (armazenados na memória)
produtosesportivos = [
    {"id" : 1, "modelo" : "Nike Air Zoom Pegasus", "empresa" : "Nike", "quantidade" : 800, "preco" : 465.50},
    {"id" : 2, "modelo" : "Specialized Roubaix", "empresa": "Roubaix", "quantidade" : 700, "preco" : 15000.00},
    {"id" : 3, "modelo" : "Nike Flight", "empresa": "Nike", "quantidade" : 780, "preco" : 414.30},
    {"id" : 4, "modelo" : "Adidas Climacool", "empresa": "Adidas", "quantidade" : 765, "preco" : 164.80},
]

# Inicializar a aplicação FastAPI
app = FastAPI()

# Modelo para adicionar novos produtos esportivos
class ProdutoEsportivo(BaseModel):
    id: Optional[int] = None
    modelo: str
    empresa: str
    quantidade: int
    preco: float
    
# Modelo para venda de produtos esportivos
class VendaProdutosEsportivos(BaseModel):
    quantidade: int   
    
# Modelo para atualizar atributos de um produto esportivo (exceto o ID) 
class AtualizarProdutosEsportivos(BaseModel):
    modelo: Optional[str] = None
    empresa: Optional[str] = None
    quantidade: Optional[int] = None
    preco: Optional[float] = None

    
# Função para gerar o próximo ID dinamicamente    
def gerar_proximo_id():
    if produtosesportivos:
        return max(produtoesportivo['id'] for produtoesportivo in produtosesportivos) + 1
    else:
        return 1

# Função auxiliar para buscar produtos esportivos por ID
def buscar_produtosesportivos_por_id(produtoesportivo_id: int):    
    for produtoesportivo in produtosesportivos:
        if produtoesportivo["id"] == produtoesportivo_id:
            return produtoesportivo
    return None

# Mddleware para logging
@app.middleware("http")
async def log_requests(request : Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Path: {request.url.path}, Method: {request.method}, Process Time: {process_time:.4f}s")
    return response

# 1. Adicionar um novo produto esportivo
@app.post("/api/v1/produtosesportivos/", status_code=201)
def adicionar_produtoesportivo(produtoesportivo: ProdutoEsportivo):
    # Verificar se o produto esportivo existe  
    for pe in produtosesportivos:
        if pe["empresa"].lower == produtoesportivo.empresa.lower() and pe["modelo"].lower == produtoesportivo.modelo.lower():
            raise HTTPException(status_code=400, detail= "Porduto esportivo já existe")
        
    #Gerar ID dinamicamente
    novo_produtoesportivo = produtoesportivo.model_dump()        
    novo_produtoesportivo['id'] = gerar_proximo_id()
    
    # Adicionar o novo produto esportivo ao repositório 
    produtosesportivos.append(novo_produtoesportivo)
    return {"message" : "Produto esportivo adicionado com sucesso!", "ProdutoEsportivo": novo_produtoesportivo}

# 2. Listar todos os produtos esportivos
@app.get("/api/v1/produtosesportivos", response_model=List[ProdutoEsportivo])
def listar_produtosesportivos():
    return produtosesportivos

# 3. Buscar produto esportivo por ID
@app.get("/api/v1/produtosesportivos/{produtoesportivo_id}")
def listar_produtosesportivos_por_id(produtoesportivo_id : int):
    produtoesportivo = buscar_produtosesportivos_por_id(produtoesportivo_id)
    if produtoesportivo is None:
        raise HTTPException(status_code=404, detail="Produto esportivo não encontrado.")
    return produtoesportivo

# 4. Vender um produto esportivo (reduzir quantidade do estoque)
@app.put("/api/v1/produtosesportivos/{produtoesportivo_id}/vender")
def vender_produtoesportivo(produtoesportivo_id: int, venda: VendaProdutosEsportivos):
    produtoesportivo = buscar_produtosesportivos_por_id(produtoesportivo_id)
    
    if produtoesportivo is None:
        raise HTTPException(status_code=404, detail="Produto esportivo não encontrado.")
    
    if produtoesportivo["quantidade"] < venda.quantidade:
        raise HTTPException(status_code=400, detail="Quantidade insuficiente no estoque.")
    
    produtoesportivo["quantidade"] -= venda.quantidade
    return {"message": "Venda realizada com sucesso!", "produtoesportivo": produtoesportivo}

# 5. Atualizar atributos de um produto esportivo pelo ID (exceto o ID)
@app.patch("/api/v1/produtosesportivos/{produtoesportivo_id}")
def atualizar_produtoesportivo(produtoesportivo_id: int, atualizar_ProdutoEsportivo: AtualizarProdutosEsportivos):
    produtoesportivo = buscar_produtosesportivos_por_id(produtoesportivo_id)
    
    if produtoesportivo is None:
        raise HTTPException(status_code=404, detail="Produto esportivo não encontrado.")
    
    # Atualizar apenas os campos fornecidos no body
    if atualizar_ProdutoEsportivo.modelo is not None:
        produtoesportivo["modelo"] = atualizar_ProdutoEsportivo.modelo
    
    if atualizar_ProdutoEsportivo.empresa is not None:
        produtoesportivo["empresa"] = atualizar_ProdutoEsportivo.empresa
    
    if atualizar_ProdutoEsportivo.quantidade is not None:
        produtoesportivo["quantidade"] = atualizar_ProdutoEsportivo.quantidade
    
    if atualizar_ProdutoEsportivo.preco is not None:
        produtoesportivo["preco"] = atualizar_ProdutoEsportivo.preco
    
    return {"message": "Produto esportivo atualizado com sucesso!", "produtoesportivo": produtoesportivo}

# 6. Remover produto esportivo pelo ID
@app.delete("/api/v1/produtosesportivos/{produtoesportivo_id}")
def remover_produtosesportivos(produtoesportivo_id: int):
    for i, produtoesportivo in enumerate(produtosesportivos):
        if produtoesportivo["id"] == produtoesportivo_id:
            del produtosesportivos[i]
            return {"message": "Produto esportivo removido com sucesso"}
        
# 7. Resetar  repositório de produtos esportivos
@app.delete("/api/v1/produtosesportivos/")
def resetar_produtosesportivos():
    global produtosesportivos
    produtosesportivos = [
    {"id" : 1, "modelo" : "Nike Air Zoom Pegasus", "empresa" : "Nike", "quantidade" : 800, "preco" : 465.50},
    {"id" : 2, "modelo" : "Specialized Roubaix", "empresa": "Roubaix", "quantidade" : 700, "preco" : 15000.00},
    {"id" : 3, "modelo" : "Nike Flight", "empresa": "Nike", "quantidade" : 780, "preco" : 414.30},
    {"id" : 4, "modelo" : "Adidas Climacool", "empresa": "Adidas", "quantidade" : 765, "preco" : 164.80},
    ]        
    return {"message": "Repositório limpo com sucesso!", "produtos esportivos" : produtosesportivos}