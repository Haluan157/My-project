import statistics
import os

def tunggal():
    a = bool(1)
    d1 = []
    while a is True:
        d=float(input("Masukkan data = "))
        d1.append(d)
        a = bool(int(input("Ketik 1 untuk menambahkan lagi dan ketik 0 untuk berhenti menambahkan = ")))
        os.system("clear")
    average=statistics.mean(d1)
    dax=0
    for i in range(len(d1)):
        da=(d1[i]-average)**2
        dax+=da
    ragam=dax/len(d1)
    print("Ragam =",ragam)

def kelompok():
    a = bool(1)
    d1,d2,f=[],[],[]
    while a is True:
        d=float(input("Masukkan data kecil = "))
        dd=float(input("Masukkan data besar = "))
        f1=float(input("Masukkan frekuensi = "))
        d1.append(d)
        d2.append(dd)
        f.append(f1)
        a = bool(int(input("Ketik 1 untuk menambahkan lagi dan ketik 0 untuk berhenti menambahkan = ")))
        os.system("clear")
    ff=0
    flist=[]
    for i in range(len(d1)):
        fff=statistics.mean([d1[i],d2[i]])
        flist.append(fff)
        f3=fff*f[i]
        ff+=f3
    average=ff/sum(f)
    d5=0
    for i in range(len(d1)):
        dx=f[i]*(flist[i]-average)**2
        d5+=dx
    ragam=d5/sum(f)
    print("Ragam =",ragam)

print("Selamat datang di PPR (Pusat Perhitungan Ragam)")
u=int(input("\nKetik 1 untuk data tunggal dan ketik 2 untuk data berkelompok\n\nPilih angka = "))

if u == 1:
    tunggal()
elif u == 2:
    kelompok()