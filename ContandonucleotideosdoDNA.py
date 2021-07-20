# Esse programa lê uma sequência de nucleotideos que compõem o DNA, por exemplo: ACGTGCTTAGCCGAT
# A saída é a quantidade de ocorrência de cada letra na sequência
dna = input("digite a sequência: ")
contA = 0
contC = 0
contG = 0
contT = 0

for i in list(dna):
    if i == 'A':
        contA = contA + 1
    elif i == 'C':
        contC = contC + 1
    elif i == 'G':
        contG = contG + 1
    elif i == 'T':
        contT = contT + 1

print(f"{contA} {contC} {contG} {contT}")
