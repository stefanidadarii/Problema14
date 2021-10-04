n=int(input('Introduceti n (2<=n<=10): '))
print('Introduceti elementele matricei:')
Matrice=[]
for i in range(n):
    a=[]
    for j in range (n):
        a.append(int(input()))
    Matrice.append(a)
dig_pr=0
dig_sec=0
for i in range(0,len(Matrice)):
    dig_pr+=Matrice[i][i]
    dig_sec+=Matrice[len(Matrice)-i-1][i]
print('Suma componentelor care se afla pe diagonala principla =', dig_pr)
print('Suma componentelor care se afla pe diagonala secundara =', dig_sec)
ss1=0
sj1=0
for i in Matrice:
    for j in i:
        if Matrice.index(i)<i.index(j):
            ss1+=j
        if Matrice.index(i)>i.index(j):
            sj1+=j
print('Suma componentelor care se afla mai sus de diagonala principală =', ss1)
print('Suma componentelor care se afla mai jos de diagonala principală =', sj1)
ss2=0
sj2=0
for i in Matrice:
    for j in i:
        if Matrice.index(i)+i.index(j)<n-1:
            ss2+=j
        if Matrice.index(i)+i.index(j)>n-1:
            sj2+=j
print('Suma componentelor care se afla mai sus de diagonala secundara =', ss2)
print('Suma componentelor care se afla mai jos de diagonala secundara =', sj2)
