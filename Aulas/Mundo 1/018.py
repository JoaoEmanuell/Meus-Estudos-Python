from math import radians,sin,cos,tan
an = float(input('\033[1;31mDigite o ângulo que você deseja \033[m'))
seno = sin(radians(an))
print('O ângulo \033[1;31m{}\033[m tem o seno de \033[1;32m{:.2f}\033[m'.format(an,seno))
cos = cos(radians(an))
print('O ângulo \033[1;31m{}\033[m tem o cosseno de \033[1;32m{:.2f}\033[m'.format(an,cos))
tan = tan(radians(an))
print('O ângulo \033[1;31m{}\033[m tem a tangente de \033[1;32m{:.2f}\033[m'.format(an,tan))