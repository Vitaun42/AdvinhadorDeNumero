from random import randint

tentativas = 0
num = randint(0, 11)
print("Tente advinhar o número entre 0 e 10...")

while True:

    tentativas += 1
    resposta = int(input(f"tentativa [{tentativas}]: "))

    if resposta > num:
        print('Menos...')
    elif resposta < num:
        print('Mais...')
    else:
        break

print(f'Parabéns, o número era {num}!, Você acertou em {tentativas} tentativas')
