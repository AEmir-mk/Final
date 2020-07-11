# Emirhan MURÖZ 1904107029
# Github Link : https://github.com/AEmir-mk/Final.git
#SORU-1 ################################################################################################################
E = {0:" ", 1:"Ocak" , 2:"Şubat" , 3:"MART" , 4:"Nisan", 5:"Mayıs", 6:"Haziran", 7:"Temmuz", 8:"Ağustos", 9:"Eylül", 10:"Ekim", 11:"Kasım", 12:"Aralık"}

M = str("Lüften Tarihi Önce GÜN, Sonra AY, En Son YIL Şeklinde Giriniz! ")
print(M)

İ = int(input("GÜN : "))
R = int(input("AY : "))
H = int(input("YIL : "))

print(İ, E[R % 10] , H )
print()
#SORU-2 ################################################################################################################
A=1

N = int(input("Sayı : "))
if N <=-1 :
    print("HATA")
elif N >=16:
    print("HATA")
elif N == 0 :
    print (3)
elif N <9:
    for M in range(1,N+1):
        A = A * M
    print(A * 3)
elif N >= 9 :
    print(N*(N+1))
elif N < 16 :
    print(N*(N+1))
print()
#SORU-3 ################################################################################################################
# Harflerin değerlerini bulup matrisin 'H2' kısmına aktarmayı düşünmüştüm yapamadım.
U = str.lower(input("Adınız : "))
R = str.lower(input("Soyadınız : "))

Ö = []
for letter in U :
  Z = ord(letter) - 96
  Ö.append(Z)


for letter in R :
  Z = ord(letter) - 96
  Ö.append(Z)

print(Ö)
print()
E2 = list(Ö)[:3]
M2 = list(Ö)[3:6]
İ2 = list(Ö)[6:9]
R2 = list(Ö)[9:]

print("[" , E2)
print(" " , M2)
print(" " , İ2)
print(" " , R2, "]")
print()
print("Matris Çarpımı")

H2 = [[5,13,9],
     [18,8,1],
     [14,13,21],
     [18,15,26]]

A2 =[[1,2,-1],
   [2,5,2],
   [-1,-2,2]]

N2=[[0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0]]

for U2 in range(len(H2)):
    for Ö2 in range(len(A2[0])):
        for Z2 in range(len(A2)):
            N2[U2][Ö2] +=H2[U2][Z2]*A2[Z2][Ö2]
for M3 in N2:
    print(M3)

print()
#SORU-4 ################################################################################################################
E3 = []
İ3 = 1
R3 = int(input("Okul Numarası : "))
for H3 in range(İ3 , R3) :
    if H3 > 1 :
        for A3 in range(2 , H3) :
            if (H3 % A3) == 0 :
                break
        else :
            E3.append(H3)
print(E3)

