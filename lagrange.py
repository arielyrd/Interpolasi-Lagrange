print("Ariel Yordan Tjahyadinata - 56220200")
print("Metode Numerik - T - Pak Dwi")
print("")

print("Interpolasi Lagrange")
sumData = int(input("Masukan banyak data yang ingin dicari: "))
x = []
y = []
for i in range(sumData):
    xInput = float(input("Masukan x - {} : ".format(i+1)))
    yInput = float(input("Masukan y - {} : ".format(i+1)))
    x.append(xInput)
    y.append(yInput)
xI = float(input("Masukan x yang ingin dicari: "))


def lagrange(x, y, xI):
    rumus = len(x)
    hasil = 0.0
    for i in range(rumus):
        hasilAkhir = y[i]
        for j in range(rumus):
            if j != i:
                hasilAkhir *= (xI - x[j]) / (x[i] - x[j])
        hasil += hasilAkhir
    return hasil


if xI < min(x) or xI > max(x):
    print("Masukkan X dalam range data") 
elif xI == min(x) or xI == max(x):
    print("x harus berada diantara data dan tidak bisa sama dengan x yang diinput")
else:
    yO = lagrange(x, y, xI)
    print("Nilai interpolasi y pada x = {} adalah y = {}".format(xI, yO))
    

