def descrever_pedidos (cliente, **extras):
    print ("Cliente: ", cliente)
    for chave, valor in extras.items(): 
        print (f"{chave} - {valor}")

dados = {"observacao":"Sem cebola", "retirada":False}
cliente = "Ana"
descrever_pedidos (cliente, **dados)
