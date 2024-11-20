A = input()
B = input()
C = input()

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

a = colors.index(A)
b = colors.index(B)
c = 10 ** (colors.index(C))

print(int(f"{a}{b}")*c)