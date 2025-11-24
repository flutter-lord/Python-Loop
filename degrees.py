import math as m
print("Degrees\t\t\tSin\t\t\tCos")
for i in range(0, 361, 10):
    print(i,"\t\t\t",format(m.sin(m.radians(i)),".4f"),"\t\t\t",format( m.cos(m.radians(i)),".4f"))