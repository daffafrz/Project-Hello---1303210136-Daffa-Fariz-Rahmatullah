#tugas besar 1 Pengenalan Pemrograman
#Nama  : Daffa Fariz Rahmatullah
#NIM   : 1303210136
#Kelas : IT-45-01
#Nilai Hore-Hore

# file_input = ("130121322X   90    50    40    60    130121323Y  80    70    60    60    130121325X  100   90    75    50    130121334Y  90    90    80    85    130121337Z  95    60    70    80    130121338X  50    50    40    60").split()
#reading pengoperasian file
daffa = open('tubes.txt', 'r')
finput = daffa.readlines()
transmit = ''
for i in finput:
    transmit += i
transmit2 = transmit.replace("\n", "\t")
transmit3 = transmit2.replace('\t', ' ')
file_input = transmit3.split()

#list dictionary
data_nilai = []

#nim
nim = []

#clo
clo = []

#list total nilai clo
clostudent = []

for i in range(len(file_input)):
    if i % 5 == 0:
        nim.append(file_input[i])
    else:
        clo.append(file_input[i])

for i in range(0, len(clo), 4):
    clo[i] = float(clo[i]) * 0.1
for j in range(1, len(clo), 4):
    clo[j] = float(clo[j]) * 0.25
for k in range(2, len(clo), 4):
    clo[k] = float(clo[k]) * 0.25
for l in range(3, len(clo), 4):
    clo[l] = float(clo[l]) * 0.4

#fungsi untuk membuat dictionary
for i in range(len(nim)):
    clos = []
    idks = i*4
    while idks < len(clo): 
        if (idks - 3) % 4 == 0:
            clos.append(clo[idks])
            dict1 = {'nim': clo[i], 'nilai clo': clos}
            data_nilai.append(dict1.copy())
            break
        else:
            clos.append(clo[idks])
            idks += 1

#for loop buat mentotalkan nilai clo setiap mahasiswa
for i in range(len(nim)):
    idx = i*4 #akses index clo dari index nim
    clostudent.append(sum(clo[idx:idx+4]))
for i in range(len(clostudent)):
    if clostudent[i] > 40:
        if clostudent[i] > 50:
            if clostudent[i] > 60:
                if clostudent[i] > 65:
                    if clostudent[i] > 70:
                        if clostudent[i] > 80:
                            clostudent[i] = "A"
                        else:
                            clostudent[i] = "AB"
                    else:
                        clostudent[i] = "B"
                else:
                    clostudent[i] = "BC"
            else:
                clostudent[i] = "C"
        else:
            clostudent[i] = "D"
    else:
        clostudent[i] = "E"
#fungsi indeks
def indeks(nim, niminput):
    global clostudent
    mahasiswa = nim.index(niminput)
    return "\nNilai dari mahasiswa dengan NIM {0}: {1}\n".format(niminput, clostudent[mahasiswa])
#fungsi report
def report():
    global clostudent
    AList = 0
    for nilai in clostudent:
        if nilai == "A" or nilai == "AB":
            AList += 1
    return "\nJumlah nilai A dan AB dari seluruh mahasiswa adalah {0} mahasiswa.\n".format(AList) #return "Jumlah nilai A dan AB dari seluruh mahasiswa adalah " + str(AList) + " mahasiswa."
#main program
inputan = int(input("\nMasukkan fungsi yang ingin anda gunakan\n\n1. Fungsi mencari nilai mahasiswa\n2. Fungsi untuk mencari jumlah nilai A dan AB\n\nMasukkan nomor fungsi yang ingin digunakan: "))
if inputan == 1:
    niminput = input("\nMasukkan nim mahasiswa: ")
    print(indeks(nim, niminput))
elif inputan == 2:
    print(report())