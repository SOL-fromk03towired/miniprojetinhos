#ainda fazendo
from random import shuffle as misturar, choice as escolhaum

ad1 = ['um macaco', 'um galo', 'uma vaca','O BOLSONARO']
ad3 = ['polichinelo', '15 flexões']

d1 = f'Imitar {escolhaum(ad1)}'
d2 = 'Beijar a pessoa da frente'
d3 = f'Fazer {escolhaum(ad3)} '

desafios = [d1, d2, d3]

av1 = ['hentai? ', 'A TV globo? ']
av2 = [' do Snyder Cut? ', 'de Evangelion? ']

v1 = f'Você assiste {av1}'
v2 = f'Você gostou {av2}'
v3 = f'Conte a coisa mais vergonhosa que você ja passou ! '

verdade = [v1, v2, v3]

input('Digite "v" Caso queria VERDADE ou digite "d" Caso queira desafio\n'
      'Aperte ENTER se entendido...')
v_ou_d = str(input('Verdade ou desafio? '))

if v_ou_d == 'v':
    print(escolhaum(verdade))
if v_ou_d == 'd':
    print(escolhaum(desafios))