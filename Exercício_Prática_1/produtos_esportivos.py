# Parte 1: Create (CRUD)

# Produto esprotivo
def cadastro_produto_esportivo(estoque):
    modelo = input("Digite o modelo do produto esportivo: ")
    empresa = input("Digite a empresa que confeccionou esse produto: ")
    quantidade = int(input("Digite a quantidade em estoque: ")) 
    estoque.append({"modelo": modelo, "empresa": empresa, "quantidade": quantidade})
    print(f"Bicicleta '{modelo}' cadastrado com êxito! ")
    
#-------------------------------------------------------------------------------------------------    
        
# Parte 2 Read (CRUD)        
        
# Catálogo produto esportivo         
def catalogar_produto_esportivo(estoque):
    if len(estoque) == 0:
        print("Nenhum produto esportivo registrada")
    else:
        for produto_esportivo in estoque:
            print(f"Modelo: {produto_esportivo['modelo']}, Empresa: {produto_esportivo['empresa']}, Quantidade: {produto_esportivo['quantidade']}")       
            
#-------------------------------------------------------------------------------------------------  

# Parte 3: Update (CRUD)

# Consulta: Produto esportivo
def consultar_produto_esportivo(estoque):
    modelo = input("Digite o nome do modelo do produto esportivo que deseja consultar: ")
    for produto_esportivo in estoque:
        if produto_esportivo["modelo"] == modelo:
            print(f"Modelo: {produto_esportivo['modelo']}, Empresa: {produto_esportivo['empresa']}, Quantidade: {produto_esportivo['quantidade']}") 
            return
    print("Nenhum produto esportivo encontrada no estoque.")                      

#-------------------------------------------------------------------------------------------------  

# Parte 4: Delete (CRUD)    

# Venda: Produto esportivo
def vender_produto_esportivo(estoque):
    modelo = input("Digite o nome do modelo do produto esportivo que deseja vender: ")
    for produto_esportivo in estoque:
        if produto_esportivo["modelo"] == modelo:
            quantidade = int(input("Digite a quantidade de venda: "))
            if quantidade <= produto_esportivo["quantidade"]:
               produto_esportivo["quantidade"] -= quantidade
               print(f"Venda registrada! Quantidade restante de '{modelo}': {produto_esportivo['quantidade']}") 
            else:
               print("Erro: Quantidade em estoque insuficiente.")       
            return
    print("Produto esportivo não encontrado no estoque.")           
    
#------------------------------------------------------------------------------------------------- 

# Parte 5: Menu do usuário ou potencial comprador (cliente)

# Menu de escolhas de produtos
def main():
    estoque = []
    while True:
        print("\nMenu Principal: ")
        print("1. Cadastrar produto esportivo. ")
        print("2. Catalogar produto esportivo. ")
        print("3. Consultar produto esportivo")
        print("4. Vender produto esportivo")
        print("5. Sair")
        
        controlador = input("Escolha o menu: ")
        
        if controlador == '1':
            cadastro_produto_esportivo(estoque)
        elif controlador == '2':
            catalogar_produto_esportivo(estoque)
        elif controlador == '3':
            consultar_produto_esportivo(estoque)
        elif controlador == '4':
            vender_produto_esportivo(estoque)
        elif controlador == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção não encontrada! Por favor, digite novamente.")                           
        
if __name__ == "__main__":
    main()  