print('-'*80)
res = 'S'
print('Calcular Renda Rural')
while res == 'S':
    print('-'*80)
    valor_kg_boi = float(input('Qual o valor do kg do boi / vaca? '))
    quant_hec = float(input('Qual a quantidade de hectares? '))
    resultado = (valor_kg_boi * 1000 / 48)*(quant_hec)
    print('-'*80)
    print('O valor da renda rural é R$ {:.2f}'.format(resultado))
    print('-'*80)
    res = str(input('Calcular novamente (S / N)? ')).strip().upper()
    while res != 'S' and res != 'N':
        print('Resposta inválida!')
        res = str(input('Calcular novamente (S / N)? ')).strip().upper()
print('FIM')



