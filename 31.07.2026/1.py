def processos_pedido (dados) : 
    if not dados ["cpf"] : return false 
    total = 0 
    for i in dados ["itens"] : 
        total += i ["preco"] * i["qtd"]
    imposto = total * 0.18 
    db.execute (" INSERT  ")
    smtp.send(dados["email"])
    print ("ok")
    return total + imposto 
