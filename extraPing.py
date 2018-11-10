from os import system, name
ip = input('\tDigite o IP a ser pingado: ')
concat = ('ping ' + ip)

'''
No linux são enviados 64 bytes de dados por cada ping
No windows são envidados 32 bytes

poderia ser nerfada a execução no Linux, dividindo processos por 2, ou buffada a do windows, por multiplicar o número
de execuções por 2 (o que é mais viável já que deve ser um número inteiro)
'''


def processos():
    try:
        num_recebe = int(input('\n\tDigite o número de processos simultâneos: '))
        return num_recebe

    except ValueError:
        print('\n\033[31mCaractére inválido. Tente novamente:\033[m \n')
        return processos()


num = processos()


print('\033[32mComeçando...\033[m')


if name == 'posix': #nome do sistema - linux
    # while continuar is True:
    for i in range(0, num):
        system('xterm -e ' + concat + ' &')
else: # qualquer outro - windows
    # while continuar is True:
    for i in range(0, num):
        system('start /B ' + concat)  # /B para não aparecer janelas


system('exit')
