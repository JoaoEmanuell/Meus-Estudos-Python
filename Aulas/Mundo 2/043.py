peso = float(input('\033[1;31mQual é o seu peso corporal em KG? \033[m'))
altura = float(input('\033[1;32mQual é a sua altura? \033[m'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de \033[1;33m{:.2f}\033[m você está \033[1;31mabaixo\033[m do peso!'.format(imc))
elif imc < 25:
    print('Seu IMC é de \033[1;33m{:.2f}\033[m você está no peso \033[1;34mideal\033[m!'.format(imc))
elif imc < 30:
    print('Seu IMC é de \033[1;33m{:.2f}\033[m você está com \033[1;32msobrepeso\033[m tome cuidado!'.format(imc))
elif imc < 40:
    print('Seu IMC é de \033[1;33m{:.2f}\033[m você está com \033[1;35mObesidade\033[m isso está ficando perigoso tome cuidado'.format(imc))
else:
    print('Seu IMC é de \033[1;33m{:.2f}\033[m você está com \033[1;31mObesidade mórbida\033[m eu recomendo uma cirugia!!!'.format(imc))
