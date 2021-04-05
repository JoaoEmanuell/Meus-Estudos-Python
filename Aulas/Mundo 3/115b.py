from uteis import exe115

arq = 'exe115b'

if not exe115.arquivoExiste(arq):
    exe115.FileCreate(arq)
n = exe115.ex115('\033[1:33mSua opção: \033[m')
