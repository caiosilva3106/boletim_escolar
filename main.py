QTD_NOTAS=int(input("Digte a qtd de notas: "))
notas=[]
for i in range (QTD_NOTAS):
    nota=float(input(f"digite a nota {i+1}:"))
    notas.append (nota)
total_notas=0
for nota in notas:
    total_notas+= nota
media= total_notas/ len (notas)
if media>=7:
    print ("Desempenho Satifatório!")
else:
    print ("Desempenho Insatisfatório...")