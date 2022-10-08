import random
import math

print("### Jogo de Adivinhação ###")
print("## Selecione um intervalo de números ##")

inferior = int(input("Insira limite inferior: "))
superior = int(input("Insira limite superior: "))

x = random.randint(inferior, superior)
chances = round(math.log2(superior - inferior))

print(f"Você só tem {chances} chances para adivinhar o número!")

count = 0

while count < chances:
    count += 1
    tentativa = int(input("Adivinhe o número: "))
    if x == tentativa:
        print(f"Parabéns! Você acertou na tentativa {count}.")
        break
    elif x > tentativa:
        print("Tente novamente! Você adivinhou muito baixo.")
    elif x < tentativa:
        print("Tente novamente! Você adivinhou muito alto")

if count >= chances and tentativa != x:
    print(f"O número é {x} \nMelhor sorte na próxima vez!")
