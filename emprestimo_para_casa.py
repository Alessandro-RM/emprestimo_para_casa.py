valordacasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos de financiamento ? '))
prestação = valordacasa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valordacasa, anos, prestação))
if prestação <= mínimo:
    print('Emprestimo \033[32mAprovado\033[m !')
else:
    print('Empréstimo \033[31m Negado \033[m !')
