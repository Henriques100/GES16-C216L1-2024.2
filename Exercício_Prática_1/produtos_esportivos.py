# Parte 1: Create (CRUD)

# Produto 1
def cadastro_bicicleta(estoque):
    modelo = input("Digite o modelo da bicicleta: ")
    empresa = input("Digite a empresa que confeccionou esse produto: ")
    quantidade = int(input("Digite a quantidade em estoque: ")) 
    estoque.append({"modelo": modelo, "empresa": empresa, "quantidade": quantidade})
    print(f"Bicicleta '{modelo}' cadastrado com êxito! ")
  
# Produto 2    
def cadastro_acessorios_bicicleta(estoque):
    modelo = input("Digite o modelo de acessórios da bicicleta: ")
    empresa = input("Digite a empresa que confeccionou esse produto: ")
    quantidade = int(input("Digite a quantidade em estoque: ")) 
    estoque.append({"modelo": modelo, "empresa": empresa, "quantidade": quantidade})
    print(f"Acessórios de bicicleta '{modelo}' cadastrado com êxito! ")

# Produto 3
def cadastro_tenis_esportivos(estoque):
    modelo = input("Digite o modelo de tênis esportivos: ")
    empresa = input("Digite a empresa que confeccionou esse produto: ")
    quantidade = int(input("Digite a quantidade em estoque: ")) 
    estoque.append({"modelo": modelo, "empresa": empresa, "quantidade": quantidade})
    print(f"Tênis esportivos '{modelo}' cadastrado com êxito! ")
        
# Produto 4
def cadastro_suplementos_alimentares(estoque):
    modelo = input("Digite o modelo de suplementos alimentares: ")
    empresa = input("Digite a empresa que confeccionou esse produto: ")
    quantidade = int(input("Digite a quantidade em estoque: ")) 
    estoque.append({"modelo": modelo, "empresa": empresa, "quantidade": quantidade})
    print(f"Suplementos alimentares '{modelo}' cadastrado com êxito! ")

# Produto 5
def cadastro_smartbands(estoque):
    modelo = input("Digite o modelo de smartbands: ")
    empresa = input("Digite a empresa que confeccionou esse produto: ")
    quantidade = int(input("Digite a quantidade em estoque: ")) 
    estoque.append({"modelo": modelo, "empresa": empresa, "quantidade": quantidade})
    print(f"Smartbands '{modelo}' cadastrado com êxito! ")
            
# Produto 6
def cadastro_relogios_fitness(estoque):
    modelo = input("Digite o modelo de relógios fitness: ")
    empresa = input("Digite a empresa que confeccionou esse produto: ")
    quantidade = int(input("Digite a quantidade em estoque: ")) 
    estoque.append({"modelo": modelo, "empresa": empresa, "quantidade": quantidade})
    print(f"Relógios fitness '{modelo}' cadastrado com êxito! ")

# Produto 7
def cadastro_equipamentos_musculacao(estoque):
    modelo = input("Digite o modelo de equipamentos de musculação: ")
    empresa = input("Digite a empresa que confeccionou esse produto: ")
    quantidade = int(input("Digite a quantidade em estoque: ")) 
    estoque.append({"modelo": modelo, "empresa": empresa, "quantidade": quantidade})
    print(f"Equipamentos de musculação '{modelo}' cadastrado com êxito! ")

# Produto 8
def cadastro_patins_acessorios(estoque):
    modelo = input("Digite o modelo de patins e seus acessórios: ")
    empresa = input("Digite a empresa que confeccionou esse produto: ")
    quantidade = int(input("Digite a quantidade em estoque: ")) 
    estoque.append({"modelo": modelo, "empresa": empresa, "quantidade": quantidade})
    print(f"Patins e acessórios '{modelo}' cadastrado com êxito! ")
    
#-------------------------------------------------------------------------------------------------    
        
# Parte 2 Read (CRUD)        
        
# Catálogo 1            
def catalogar_bicicleta(estoque):
    if len(estoque) == 0:
        print("Nenhuma bicicleta registrada")
    else:
        for bicicleta in estoque:
            print(f"Modelo: {bicicleta['modelo']}, Empresa: {bicicleta['empresa']}, Quantidade: {bicicleta['quantidade']}")       
            
# Catálogo 2            
def catalogar_acessorios_bicicleta(estoque):
    if len(estoque) == 0:
        print("Nenhum acessório de bicicleta registrada")
    else:
        for acessorios_bicicleta in estoque:
            print(f"Modelo: {acessorios_bicicleta['modelo']}, Empresa: {acessorios_bicicleta['empresa']}, Quantidade: {acessorios_bicicleta['quantidade']}")
            
# Catálogo 3            
def catalogar_tenis_esportivos(estoque):
    if len(estoque) == 0:
        print("Nenhum tênis esportivo registrado")
    else:
        for tenis_esportivo in estoque:
            print(f"Modelo: {tenis_esportivo['modelo']}, Empresa: {tenis_esportivo['empresa']}, Quantidade: {tenis_esportivo['quantidade']}")            
                     
# Catálogo 4            
def catalogar_suplementos_alimentares(estoque):
    if len(estoque) == 0:
        print("Nenhum suplemento alimentar registrado")
    else:
        for suplemento_alimentares in estoque:
            print(f"Modelo: {suplemento_alimentares['modelo']}, Empresa: {suplemento_alimentares['empresa']}, Quantidade: {suplemento_alimentares['quantidade']}")            

# Catálogo 5            
def catalogar_smartbands(estoque):
    if len(estoque) == 0:
        print("Nenhum smartband registrado")
    else:
        for smartbands in estoque:
            print(f"Modelo: {smartbands['modelo']}, Empresa: {smartbands['empresa']}, Quantidade: {smartbands['quantidade']}") 
                       
# Catálogo 6            
def catalogar_relogios_fitness(estoque):
    if len(estoque) == 0:
        print("Nenhum relógio fitness registrado")
    else:
        for relogios_fitness in estoque:
            print(f"Modelo: {relogios_fitness['modelo']}, Empresa: {relogios_fitness['empresa']}, Quantidade: {relogios_fitness['quantidade']}")            

# Catálogo 7            
def catalogar_equipamentos_musculacao(estoque):
    if len(estoque) == 0:
        print("Nenhum equipamento de musculação registrado")
    else:
        for equipamento_musculacao in estoque:
            print(f"Modelo: {equipamento_musculacao['modelo']}, Empresa: {equipamento_musculacao['empresa']}, Quantidade: {equipamento_musculacao['quantidade']}")            

# Catálogo 8            
def catalogar_patins_acessorios(estoque):
    if len(estoque) == 0:
        print("Nenhum patins e acessórios do mesmo registrado")
    else:
        for patins_acessorios in estoque:
            print(f"Modelo: {patins_acessorios['modelo']}, Empresa: {patins_acessorios['empresa']}, Quantidade: {patins_acessorios['quantidade']}")            

#-------------------------------------------------------------------------------------------------  

# Parte 3: Update (CRUD)

# Consulta 1: Bicicleta
def consultar_bicicletas(estoque):
    modelo = input("Digite o nome do modelo da bicicleta que deseja consultar: ")
    for bicicletas in estoque:
        if bicicletas["modelo"] == modelo:
            print(f"Modelo: {bicicletas['modelo']}, Empresa: {bicicletas['empresa']}, Quantidade: {bicicletas['quantidade']}") 
            return
    print("Nenhuma bicicleta encontrada no estoque.")                      

# Consulta 2: Acessórios da bicicleta
def consultar_acessorios_bicicleta(estoque):
    modelo = input("Digite o nome do modelo do acessório da bicicleta que deseja consultar: ")
    for acessorios_bicicletas in estoque:
        if acessorios_bicicletas["modelo"] == modelo:
            print(f"Modelo: {acessorios_bicicletas['modelo']}, Empresa: {acessorios_bicicletas['empresa']}, Quantidade: {acessorios_bicicletas['quantidade']}") 
            return
    print("Nenhum acessório de bicicleta encontrado no estoque.")                      

# Consulta 3: Tênis esportivo
def consultar_tenis_esportivo(estoque):
    modelo = input("Digite o nome do modelo do tênis esportivo que deseja consultar: ")
    for tenis_esportivo in estoque:
        if tenis_esportivo["modelo"] == modelo:
            print(f"Modelo: {tenis_esportivo['modelo']}, Empresa: {tenis_esportivo['empresa']}, Quantidade: {tenis_esportivo['quantidade']}") 
            return
    print("Nenhuma tênis esportivo encontrado no estoque.")  
                        
# Consulta 4: Suplementos alimentares
def consultar_suplementos_alimentares(estoque):
    modelo = input("Digite o nome do modelo do suplemento alimentar que deseja consultar: ")
    for suplementos_alimentares in estoque:
        if suplementos_alimentares["modelo"] == modelo:
            print(f"Modelo: {suplementos_alimentares['modelo']}, Empresa: {suplementos_alimentares['empresa']}, Quantidade: {suplementos_alimentares['quantidade']}") 
            return
    print("Nenhum suplemento alimentar encontrado no estoque.")                      

# Consulta 5: Smartbands
def consultar_smartbands(estoque):
    modelo = input("Digite o nome do modelo do smartband que deseja consultar: ")
    for smartbands in estoque:
        if smartbands["modelo"] == modelo:
            print(f"Modelo: {smartbands['modelo']}, Empresa: {smartbands['empresa']}, Quantidade: {smartbands['quantidade']}") 
            return
    print("Nenhum smartband encontrado no estoque.")       
    
# Consulta 6: Relógios fitness
def consultar_relogios_fitness(estoque):
    modelo = input("Digite o nome do modelo do relógio fitness que deseja consultar: ")
    for relogios_fitness in estoque:
        if relogios_fitness["modelo"] == modelo:
            print(f"Modelo: {relogios_fitness['modelo']}, Empresa: {relogios_fitness['empresa']}, Quantidade: {relogios_fitness['quantidade']}") 
            return
    print("Nenhum relógio fitness encontrado no estoque.")     
    
# Consulta 7: Equipamentos de musculação
def consultar_equipamentos_musculacao(estoque):
    modelo = input("Digite o nome do modelo do equipamento de musculação que deseja consultar: ")
    for equipamentos_musculacao in estoque:
        if equipamentos_musculacao["modelo"] == modelo:
            print(f"Modelo: {equipamentos_musculacao['modelo']}, Empresa: {equipamentos_musculacao['empresa']}, Quantidade: {equipamentos_musculacao['quantidade']}") 
            return
    print("Nenhum equipamento de musculação encontrado no estoque.")        

# Consulta 8: Patins e seus acessórios
def consultar_patins_acessorios(estoque):
    modelo = input("Digite o nome do modelo de patins e seus acessórios que deseja consultar: ")
    for patins_acessorios in estoque:
        if patins_acessorios["modelo"] == modelo:
            print(f"Modelo: {patins_acessorios['modelo']}, Empresa: {patins_acessorios['empresa']}, Quantidade: {patins_acessorios['quantidade']}") 
            return
    print("Nenhum patin e seus acessórios foram encontrados no estoque.")        
    
#-------------------------------------------------------------------------------------------------  

# Parte 4: Delete (CRUD)    

# Venda 1: Bicicletas
def vender_bicicletas(estoque):
    modelo = input("Digite o nome do modelo da bicicleta que deseja vender: ")
    for bicicletas in estoque:
        if bicicletas["modelo"] == modelo:
            quantidade = int(input("Digite a quantidade de venda: "))
            if quantidade <= bicicletas["quantidade"]:
               bicicletas["quantidade"] -= quantidade
               print(f"Venda registrada! Quantidade restante de '{modelo}': {bicicletas['quantidade']}") 
            else:
               print("Erro: Quantidade em estoque insuficiente.")       
            return
    print("Bicicleta não encontrada no estoque.")           
    
# Venda 2: Acessórios de bicicleta
def vender_acessorios_bicicleta(estoque):
    modelo = input("Digite o nome do modelo dos acessórios de bicicleta que deseja vender: ")
    for acessorios_bicicleta in estoque:
        if acessorios_bicicleta["modelo"] == modelo:
            quantidade = int(input("Digite a quantidade de venda: "))
            if quantidade <= acessorios_bicicleta["quantidade"]:
               acessorios_bicicleta["quantidade"] -= quantidade
               print(f"Venda registrada! Quantidade restante de '{modelo}': {acessorios_bicicleta['quantidade']}") 
            else:
               print("Erro: Quantidade em estoque insuficiente.")       
            return
    print("Acessórios de bicicleta não encontrada no estoque.")  
    
# Venda 3: Tênis esportivos
def vender_tenis_esportivos(estoque):
    modelo = input("Digite o nome do modelo dos tênis esportivos que deseja vender: ")
    for tenis_esportivos in estoque:
        if tenis_esportivos["modelo"] == modelo:
            quantidade = int(input("Digite a quantidade de venda: "))
            if quantidade <= tenis_esportivos["quantidade"]:
               tenis_esportivos["quantidade"] -= quantidade
               print(f"Venda registrada! Quantidade restante de '{modelo}': {tenis_esportivos['quantidade']}") 
            else:
               print("Erro: Quantidade em estoque insuficiente.")       
            return
    print("Tênis esportivos não encontrados no estoque.")             

# Venda 4: Suplementos alimentares
def vender_suplementos_alimentares(estoque):
    modelo = input("Digite o nome do modelo dos suplementos alimentares que deseja vender: ")
    for suplementos_alimentares in estoque:
        if suplementos_alimentares["modelo"] == modelo:
            quantidade = int(input("Digite a quantidade de venda: "))
            if quantidade <= suplementos_alimentares["quantidade"]:
               suplementos_alimentares["quantidade"] -= quantidade
               print(f"Venda registrada! Quantidade restante de '{modelo}': {suplementos_alimentares['quantidade']}") 
            else:
               print("Erro: Quantidade em estoque insuficiente.")       
            return
    print("Suplemento alimentar não encontrada no estoque.") 
    
# Venda 5: Smartbands
def vender_smartbands(estoque):
    modelo = input("Digite o nome do modelo dos smartbands que deseja vender: ")
    for smartbands in estoque:
        if smartbands["modelo"] == modelo:
            quantidade = int(input("Digite a quantidade de venda: "))
            if quantidade <= smartbands["quantidade"]:
               smartbands["quantidade"] -= quantidade
               print(f"Venda registrada! Quantidade restante de '{modelo}': {smartbands['quantidade']}") 
            else:
               print("Erro: Quantidade em estoque insuficiente.")       
            return
    print("Smartband não encontrada no estoque.")    
    
# Venda 6: Relógios Fitness
def vender_relogios_fitness(estoque):
    modelo = input("Digite o nome do modelo dos relógios fitness que deseja vender: ")
    for relogios_fitness in estoque:
        if relogios_fitness["modelo"] == modelo:
            quantidade = int(input("Digite a quantidade de venda: "))
            if quantidade <= relogios_fitness["quantidade"]:
               relogios_fitness["quantidade"] -= quantidade
               print(f"Venda registrada! Quantidade restante de '{modelo}': {relogios_fitness['quantidade']}") 
            else:
               print("Erro: Quantidade em estoque insuficiente.")       
            return
    print("Relógio fitness não encontrado no estoque.")         
    
# Venda 7: Equipamentos de musculação
def vender_equipamentos_musculacao(estoque):
    modelo = input("Digite o nome do modelo dos equipamentos de musculação que deseja vender: ")
    for equipamentos_musculacao in estoque:
        if equipamentos_musculacao["modelo"] == modelo:
            quantidade = int(input("Digite a quantidade de venda: "))
            if quantidade <= equipamentos_musculacao["quantidade"]:
               equipamentos_musculacao["quantidade"] -= quantidade
               print(f"Venda registrada! Quantidade restante de '{modelo}': {equipamentos_musculacao['quantidade']}") 
            else:
               print("Erro: Quantidade em estoque insuficiente.")       
            return
    print("Equipamento de musculação não encontrado no estoque.") 
    
# Venda 8: Patins e seus acessórios
def vender_patins_acessorios(estoque):
    modelo = input("Digite o nome do modelo dos patins e seus acessórios que deseja vender: ")
    for patins_acessorios in estoque:
        if patins_acessorios["modelo"] == modelo:
            quantidade = int(input("Digite a quantidade de venda: "))
            if quantidade <= patins_acessorios["quantidade"]:
               patins_acessorios["quantidade"] -= quantidade
               print(f"Venda registrada! Quantidade restante de '{modelo}': {patins_acessorios['quantidade']}") 
            else:
               print("Erro: Quantidade em estoque insuficiente.")       
            return
    print("Patins e seus acessórios não encontrados no estoque.")         
    
#------------------------------------------------------------------------------------------------- 

# Parte 5: Menu do usuário ou potencial comprador (cliente)

# Menu de escolhas de produtos
def main():
    estoque = []
    while True:
        print("\nMenu Principal: ")
        print("1. Entrar no menu bicicleta")
        print("2. Entrar no menu acessórios de bicicleta")
        print("3. Entrar no menu de tênis esportivos")
        print("4. Entrar no menu de suplementos alimentares")
        print("5. Entrar no menu de smartbands")
        print("6. Entrar no menu de relógios fitness")
        print("7. Entrar no menu de equipamentos de musculação")
        print("8. Entrar no menu de patins e seus acessórios")
        print("9. Sair")
        
        controlador = input("Escolha o menu: ")
        
        if controlador == '1':
            menu_bicicleta()
        elif controlador == '2':
            menu_acessorios_bicicleta()
        elif controlador == '3':
            menu_tenis_esportivos()
        elif controlador == '4':
            menu_suplementos_alimentares()
        elif controlador == '5':
            menu_smartbands()    
        elif controlador == '6':
            menu_relogios_fitness()
        elif controlador == '7':
            menu_equipamentos_musculacao()
        elif controlador == '8':
            menu_patins_acessorios()                        
        elif controlador == '9':
            print("Saindo do programa...")
            break
        else:
            print("Opção não encontrada! Por favor, digite novamente.")                           
        

# Menu de bicicletas (1)
def menu_bicicleta():
    estoque = []
    while True:
        print(" Menu de Opções: ")
        print("1. Cadastrar bicicleta")
        print("2. Catalogar bicicletas")  
        print("3. Consultar bicicletas")
        print("4. Vender bicicleta")
        print("5. Voltar ao menu principal")
        print("6. Sair")
        
        alternativa = input("Escolha uma opção: ")
        
        if alternativa == '1':
           cadastro_bicicleta(estoque)
        elif alternativa == '2':
           catalogar_bicicleta(estoque)      
        elif alternativa == '3':
           consultar_bicicletas(estoque)
        elif alternativa == '4':
            vender_bicicletas(estoque)
        elif alternativa == '5':
            main()    
        elif alternativa == '6':
            print("Saída...") 
            break
        else:
            print("Opção ilegal! Por favor, tente novamente.")   

# Menu de acessórios de bicicletas (2)
def menu_acessorios_bicicleta():
    estoque = []
    while True:
        print(" Menu de Opções:")
        print("1. Cadastrar acessórios de bicicletas")
        print("2. Catalogar acessórios de bicicletas")  
        print("3. Consultar acessórios de bicicletas")
        print("4. Vender acessórios de bicicleta")
        print("5. Voltar ao menu principal")
        print("6. Sair")
        
        alternativa = input("Escolha uma opção: ")
        
        if alternativa == '1':
           cadastro_acessorios_bicicleta(estoque)
        elif alternativa == '2':
           catalogar_acessorios_bicicleta(estoque)      
        elif alternativa == '3':
           consultar_acessorios_bicicleta(estoque)
        elif alternativa == '4':
            vender_acessorios_bicicleta(estoque)
        elif alternativa == '5':
            main()    
        elif alternativa == '6':
            print("Saída...") 
            break
        else:
            print("Opção ilegal! Por favor, tente novamente.")                      

# Menu de tênis esportivos (3)
def menu_tenis_esportivos():
    estoque = []
    while True:
        print(" Menu de Opções:")
        print("1. Cadastrar tênis esportivo")
        print("2. Catalogar tênis esportivo")  
        print("3. Consultar tênis esportivo")
        print("4. Vender tênis esportivo")
        print("5. Voltar ao menu principal")
        print("6. Sair")
        
        alternativa = input("Escolha uma opção: ")
        
        if alternativa == '1':
           cadastro_tenis_esportivos(estoque)
        elif alternativa == '2':
           catalogar_tenis_esportivos(estoque)      
        elif alternativa == '3':
           consultar_tenis_esportivo(estoque)
        elif alternativa == '4':
            vender_tenis_esportivos(estoque)
        elif alternativa == '5':
            main()
        elif alternativa == '6':
            print("Saída...") 
            break
        else:
            print("Opção ilegal! Por favor, tente novamente.")  
            
# Menu de suplementos alimentares (4)
def menu_suplementos_alimentares():
    estoque = []
    while True:
        print(" Menu de Opções:")
        print("1. Cadastrar suplemento alimentar")
        print("2. Catalogar suplemento alimentar")  
        print("3. Consultar suplemento alimentar")
        print("4. Vender suplemento alimentar")
        print("5. Voltar ao menu principal")
        print("6. Sair")
        
        alternativa = input("Escolha uma opção: ")
        
        if alternativa == '1':
           cadastro_suplementos_alimentares(estoque)
        elif alternativa == '2':
           catalogar_suplementos_alimentares(estoque)      
        elif alternativa == '3':
           consultar_suplementos_alimentares(estoque)
        elif alternativa == '4':
            vender_suplementos_alimentares(estoque)
        elif alternativa == '5':
            main()    
        elif alternativa == '6':
            print("Saída...") 
            break
        else:
            print("Opção ilegal! Por favor, tente novamente.")              

# Menu de smartbands (5)
def menu_smartbands():
    estoque = []
    while True:
        print(" Menu de Opções:")
        print("1. Cadastrar smartbands")
        print("2. Catalogar smartbands")  
        print("3. Consultar smartbands")
        print("4. Vender smartbands")
        print("5. Voltar ao menu principal")
        print("6. Sair")
        
        alternativa = input("Escolha uma opção: ")
        
        if alternativa == '1':
           cadastro_smartbands(estoque)
        elif alternativa == '2':
           catalogar_smartbands(estoque)      
        elif alternativa == '3':
           consultar_smartbands(estoque)
        elif alternativa == '4':
            vender_smartbands(estoque)
        elif alternativa == '5':
            main()    
        elif alternativa == '6':
            print("Saída...") 
            break
        else:
            print("Opção ilegal! Por favor, tente novamente.")  

# Menu de relógios fitness (6)
def menu_relogios_fitness():
    estoque = []
    while True:
        print(" Menu de Opções:")
        print("1. Cadastrar relógio fitness")
        print("2. Catalogar relógio fitness")  
        print("3. Consultar relógio fitness")
        print("4. Vender relógio fitness")
        print("5. Voltar ao menu principal")
        print("6. Sair")
        
        alternativa = input("Escolha uma opção: ")
        
        if alternativa == '1':
           cadastro_relogios_fitness(estoque)
        elif alternativa == '2':
           catalogar_relogios_fitness(estoque)      
        elif alternativa == '3':
           consultar_relogios_fitness(estoque)
        elif alternativa == '4':
            vender_relogios_fitness(estoque)
        elif alternativa == '5':
            main()    
        elif alternativa == '6':
            print("Saída...") 
            break
        else:
            print("Opção ilegal! Por favor, tente novamente.")  
            
# Menu de equipamentos de musculação (7)
def menu_equipamentos_musculacao():
    estoque = []
    while True:
        print(" Menu de Opções:")
        print("1. Cadastrar equipamentos de musculação")
        print("2. Catalogar equipamentos de musculação")  
        print("3. Consultar equipamentos de musculação")
        print("4. Vender equipamentos de musculação")
        print("5. Voltar ao menu principal")
        print("6. Sair")
        
        alternativa = input("Escolha uma opção: ")
        
        if alternativa == '1':
           cadastro_equipamentos_musculacao(estoque)
        elif alternativa == '2':
           catalogar_equipamentos_musculacao(estoque)      
        elif alternativa == '3':
           consultar_equipamentos_musculacao(estoque)
        elif alternativa == '4':
            vender_equipamentos_musculacao(estoque)
        elif alternativa == '5':
            main()
        elif alternativa == '6':
            print("Saída...") 
            break
        else:
            print("Opção ilegal! Por favor, tente novamente.")              

# Menu de patins e seus acessórios (8)
def menu_patins_acessorios():
    estoque = []
    while True:
        print(" Menu de Opções:")
        print("1. Cadastrar patins e seus acessórios")
        print("2. Catalogar patins e seus acessórios")  
        print("3. Consultar patins e seus acessórios")
        print("4. Vender patins e seus acessórios")
        print("5. Voltar ao menu principal")
        print("6. Sair")
        
        alternativa = input("Escolha uma opção: ")
        
        if alternativa == '1':
           cadastro_patins_acessorios(estoque)
        elif alternativa == '2':
           catalogar_patins_acessorios(estoque)      
        elif alternativa == '3':
           consultar_patins_acessorios(estoque)
        elif alternativa == '4':
            vender_patins_acessorios(estoque)
        elif alternativa == '5':
            main()    
        elif alternativa == '6':
            print("Saída...") 
            break
        else:
            print("Opção ilegal! Por favor, tente novamente.")  

if __name__ == "__main__":
    main()  