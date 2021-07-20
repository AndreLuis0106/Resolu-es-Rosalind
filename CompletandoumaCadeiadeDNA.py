# Esse programa tem como saída o complemento reverso de uma cadeia de DNA
dna = input("Digite a cadeia de DNA: ")
aux = list(dna)

for i in range(len(aux)):
    if dna[i] == 'A':
        aux[i] = 'T'
    elif dna[i] == 'T':
        aux[i] = 'A'
    elif dna[i] == 'C':
        aux[i] = 'G'
    elif dna[i] == 'G':
        aux[i] = 'C'

rna = "".join(aux)
print(rna[::-1])
