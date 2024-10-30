import os 
os.system('cls')

print('Digite 50 números para verificar se são multiplos de 3.')

print('-'*50)

for i in range(0,50):
    
    x = int(input('Digite os numeros:'))
    print('-'*50)
    if x % 3 == 0:
        print('O número é multiplo')
        
    else:
        print('O número não é multiplo')    
             