# Esse programa tem por objetivo transcrever a sequencia de nucleotideos em uma sequencia de RNA, por exemplo: ACGTGCTA -> ACGUGCUA
dna = input("Digite a sequência:")
aux = list(dna)
for i in range(len(aux)):
    if dna[i] == 'T':
        aux[i] = 'U'

rna = "".join(aux)
print(rna)
