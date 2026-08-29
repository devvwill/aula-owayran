def descrever_pedidos (cliente, **extras):
    print ("Cliente: ", cliente)
    for chave, valor in extras.items: 
        print (f"{chave} - {valor}")