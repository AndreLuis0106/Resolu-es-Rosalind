# Esse programa tem o objetivo de calcular a probabilidade de 2 organismos se acasalarem e o descendente possuir um alelo domante
# Entre 3 organismos, um homozigoto domante, outro heterozigot e um homozigot recessivo
populacao = input("Digite as populações de cada organismo:")
homoDominante = float(populacao[0])
heterozigoto = float(populacao[1])
homoRecessivo = float(populacao[2])

total = 0
for i in populacao:
    total += float(i)

dominantTotal = homoDominante/total
heterozigotoDominanteTotal = (heterozigoto/total) * ((homoDominante/(total-1)) + (
    heterozigoto-1)/(total-1) * 0.75 + ((homoRecessivo/(total-1)) * 0.5))
domHeterRecesTotal = (homoRecessivo/total) * \
    (homoDominante/(total-1) + heterozigoto/(total-1) * 0.5)

probabilidade = dominantTotal + heterozigotoDominanteTotal + domHeterRecesTotal

print(f'A probabilidade é: {probabilidade: .5f}')
print(probabilidade)
