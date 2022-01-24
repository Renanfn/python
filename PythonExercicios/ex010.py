real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.51
euro = real / 6.24
libras = real / 7.41
print('Com R$ {}, você pode comprar: \nUS$ {:.2f} \n€ {:.2f} \n£ {:.2f}.'.format(real, dolar, euro, libras))
