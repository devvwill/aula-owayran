from pedidos import cadastrarClientes
cadastro = cadastrarClientes()

from pedidos import cadastrarProdutos
item = cadastrarProdutos()

from pedidos import calcularTotal
subtotal, total = calcularTotal(item)

from pedidos import emitirRecibo
emitirRecibo(cadastro, item, subtotal, total)