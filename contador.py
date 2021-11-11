from time import sleep
class conta:
    def contador(i,f,p):
        if i >=f:
            cont = i
            while cont>=f:
                print(f'{cont} ', end='',flush=True)
                sleep(0.7)
                cont -=1
            print('....')
    contador(3, 1, 1)