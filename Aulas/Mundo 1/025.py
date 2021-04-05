nm = str(input('\033[1;31mDigite o seu nome completo \033[m')).strip()
nmu = nm.upper()
print('\033[1;33mSeu nome tem Silva? \033[m\033[1;35m{}\033[m'.format('SILVA' in nmu))