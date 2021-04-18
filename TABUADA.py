print('TABUADA DE 1 A 20:')
for a in range(1, 20):
    print('--' *5)
    for b in range(1, 11):
        print('{:2} x {:1} = {:2}'.format(a, b, a*b))
input('Aperte ENTER para finalizar o programa :]')