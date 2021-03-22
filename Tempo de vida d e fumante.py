nome = (input("Olá, poderia informar o seu nome?"))
cigarros = int(input("Me informa quantos cigarro você costuma fumar por dia?"))
anos = int(input("Há quantos anos tem esse vício?"))

tempoPerdido = anos * 365 * cigarros * 10
horsPerdidas = tempoPerdido / 60
diasPerdidos = horsPerdidas / 24  

print(f"{nome}," "você perdeu %d dias da sua vida" % diasPerdidos)
