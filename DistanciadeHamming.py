# Esse programa calcula a distância de Hamming
seq1 = input("Digite a primeira sequência: ")
seq2 = input("Digite a segunda sequência: ")

aux1 = list(seq1)
aux2 = list(seq2)

dist_hamm = 0

for i in range(len(seq1)):
    if aux1[i] != aux2[i]:
        dist_hamm += 1

print(dist_hamm)
