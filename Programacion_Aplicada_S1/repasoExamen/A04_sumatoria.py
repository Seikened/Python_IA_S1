sumatoria = 0
x= int(input("Que valor quieres usar: "))

for n in range(1,6,1):
    
    sumatoria += ( 2 * n ) / ( (x**n) +2 )
    print(sumatoria)