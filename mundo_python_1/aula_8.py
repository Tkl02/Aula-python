# Modificando texto

#           estilo letra  cor letra   cor fundo
#                ↓            ↓           ↓
# ANSI ('  \033[ n;           n;          n   \033[m')
'''
as cores tanto das letras como do fundo são as mesmas sequencia
ja o estilo do texto e: 0 para neuto
                        1 para negrito
                        4 para sublinhado
                        7 para cor negativa(troca o fundo com a letra)

'''
#                     inicio      termino(sem o termino ele vai dar sequencia nas palavras seguinte   
#                       ↓          ↓        e não na selecionada apenas)
cores = { 'branco'  : '\033[30;40\033[m'
         'vermelho' : '\033[31;41\033[m'
         'verde'    : '\033[32;42\033[m'
         'amarelo'  : '\033[33;43\033[m'
         'azul'     : '\033[34;44\033[m'
         'roxo'     : '\033[35;45\033[m'
         'ciano'    : '\033[36;46\033[m'
         'cinza'    : '\033[37;46\033[m'}
