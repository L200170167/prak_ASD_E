class MhsTif(object):
    def __init__(self, nama, nim, kotaTinggal, uangSaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kotaTinggal
        self.uangSaku = uangSaku

    def __str__(self):
        x = self.nim
        return x

    def getnim(self):
        return self.nim

c0 = MhsTif("Ika", "L10", "Sukoharjo", 240000)
c1 = MhsTif("Budi", "L51", "Sragen", 230000)
c2 = MhsTif("Ahmad", "L2", "Surakarta", 250000)
c3 = MhsTif("Chandra", "L18", "Surakarta", 235000)
c4 = MhsTif("Eka", "L4", "Boyolali", 240000)
c5 = MhsTif("Fandi", "L31", "Salatiga", 250000)
c6 = MhsTif("Deni", "L13", "Klaten", 245000)
c7 = MhsTif("Galuh", "L5", "Wonogiri", 245000)
c8 = MhsTif("Janto", "L23", "Klaten", 245000)
c9 = MhsTif("Hasan", "L64", "Karanganyar", 270000)
c10 = MhsTif("Khalid", "L29", "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#NOMOR 1
def cetakDaftar(d):
    for i in d:
        print (i)
        
print("NOMOR 1")
cetakDaftar(Daftar)

#NOMOR 2
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

A = [1,2,3,4,5,8,11,13,14,15]
B = [6,7,9,10,12,16,18,20,22]
C = []
C.extend(A)
C.extend(B)
print("")
print("NOMOR 2")
print ('Nilai C' , C)

#NOMOR 3
print("")
print("NOMOR 3")
from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[q]= A[q]
    A[q]= tmp
    
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil   

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
            
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print('insertion:%g detik' %(ak-aw));
