compra= int(input("digite o valor da compra:"))
presta= int(input("digite o numero de prestações:"))

prestacoes = compra/presta

if prestacoes > 500:
    print("usuário não consegue pagar")
else:
    print("usuário consegue pagar")


