import queue
fidoso = queue.Queue()
fgestant = queue.Queue()
fpop = queue.Queue()
mstrfidoso = []
mstrfgestant = []
mstrfpop = []
rodaroda = True
while rodaroda == True:
    print('================================================================================')
    print('1 - Inserir alguém na fila')
    print('2 - Mostrar as filas')
    print('3 - Retirar alguem da fila')
    print('4 - Sair')
    a = int(input('Digite uma das opções: '))
    if a == 1:
        esc = str(input('Qual fila deseja entrar? (Idoso/Gestante/Comum): '))
        name = str(input('Digite seu nome: '))
        if esc == 'Idoso' or esc == 'idoso':
            fidoso.put(name)
            mstrfidoso.append(name)
        elif esc == 'Gestante' or esc == 'gestante':
            fgestant.put(name)
            mstrfgestant.append(name)
        elif esc == 'Comum' or esc == 'comum':
            fpop.put(name)
            mstrfpop.append(name)
        else:
            print('Digite uma das filas existentes!')
    elif a == 2:
        print('FILA DE IDOSOS:')
        print(mstrfidoso)
        print('FILA DE GESTANTES:')
        print(mstrfgestant)
        print('FILA COMUM:')
        print(mstrfpop)
    elif a == 3:
        if fidoso.empty() == False:
            print('A pessoa retirada foi', fidoso.get())
        elif fgestant.empty() ==False:
            print('A pessoa retirada foi', fgestant.get())
        elif fpop.empty() == False:
            print('A pessoa retirada foi', fpop.get())
    elif a == 4:
        rodaroda = False
        print('Volte sempre!')
    else:
        print('Digite uma das opções sugeridas!')
