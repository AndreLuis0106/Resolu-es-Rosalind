# Esse programa verifica em quais posições uma substring aparece em uma string, depois retorna as posições
dna = input("Digite a sequência: ")
seq = input("Digite a sequência que se queira achar: ")

cont = 0
while (cont < (len(dna) - len(seq))):
    if dna.find(seq, cont, len(dna)) == -1:
        break
    else:
        print(dna.find(seq, cont, len(dna))+1)

    cont = dna.find(seq, cont, len(dna)) + 1
