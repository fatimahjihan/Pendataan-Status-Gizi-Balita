# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:14:01 2020

@author: KELOMPOK 9 PROGKOMP
"""

        
#fungsipendataanbayi
def databalita():
    #berfungsi menentukan kebenaran untuk menjalankan pengulangan
    identitas = True
    
    while identitas:
        nama = str(input("Tuliskan nama bayi: "))
        #list untuk menampung data bayi
        databayi = []
        databayi.append(nama)
        judul = 'judul'
        #list untuk menampung judul data bayi
        header =[]
        header.append('NAMA')
        header.append('JENIS KELAMIN')
        header.append('USIA')
        header.append('BB')
        header.append('INDEKS')
        header.append('STATUS')
        jenis_kelamin=(str(input("1). Laki-Laki\n2). Perempuan\nJenis Kelamin: ")))    
        #mendata bayi laki-laki
        if jenis_kelamin == ("1"):
            databayi.append('Laki-Laki')
            usia = int(input("Berapa usia bayi?(bulan): "))
            databayi.append(f"{usia} bulan")
            datamedian_laki= [
        [0,2.9,3.3,3.9],
        [1,3.9,4.5,5.1],
        [2,4.9,5.6,6.3],
        [3,5.7,6.4,7.2],
        [4,6.2,7,7.8],
        [5,6.7,7.5,8.4],
        [6,7.1,7.9,8.8],
        [7,7.4,8.3,9.2],
        [8,7.7,8.6,9.6],
        [9,8,8.9,9.9],
        [10,8.2,9.2,10.2],
        [11,8.4,9.4,10.5],
        [12,8.6,9.6,10.8],
        [13,8.8,9.9,11],
        [14,9,10.1,11.3],
        [15,9.2,10.3,11.5],
        [16,9.4,10.5,11.7],
        [17,9.6,10.7,12],
        [18,9.8,10.9,12.2],
        [19,10,11.1,12.5],
        [20,10.1,11.3,12.7],
        [21,10.3,11.5,12.9],
        [22,10.5,11.8,13.2],
        [23,10.7,12,13.4],
        [24,10.8,12.2,13.6],
        [25,11,12.4,13.9],
        [26,11.2,12.5,14.1],
        [27,11.3,12.7,14.3],
        [28,11.5,12.9,14.5],
        [29,11.7,13.1,14.8],
        [30,11.8,13.3,15],
        [31,12,13.5,15.2],
        [32,12.1,13.7,15.4],
        [33,12.3,13.8,15.6],
        [34,12.4,14,15.8],
        [35,12.6,14.2,16],
        [36,12.7,14.3,16.2],
        [37,12.9,14.5,16.4],
        [38,13,14.7,16.6],
        [39,13.1,14.8,16.8],
        [40,13.3,15,17],
        [41,13.4,15.2,17.2],
        [42,13.6,15.3,17.4],
        [43,13.7,15.5,17.6],
        [44,13.8,15.7,17.8],
        [45,14,15.8,18],
        [46,14.1,16,18.2],
        [47,14.3,16.2,18.4],
        [48,14.4,16.3,18.6],
        [49,14.5,16.5,18.8],
        [50,14.7,16.7,19],
        [51,14.8,16.8,19.2],
        [52,15,17,19.4],
        [53,15.1,17.2,19.6],
        [54,15.2,17.3,19.8],
        [55,15.4,17.5,20],
        [56,15.5,17.7,20.2],
        [57,15.6,17.8,20.4],
        [58,15.8,18,20.6],
        [59,15.9,18.2,20.8],
        [60,16,18.3,21]
        ]
            
            median=0
            for median in datamedian_laki:
                if usia in median:
                    bb = float(input("Berapa berat bayi?(kg): "))
                    databayi.append(f"{bb} kg")                   
                    if bb>median[2]:
                         indeks = round((bb - median[2])/(median[3]-median[2]),2)
                         databayi.append(indeks)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             databayi.append('Gizi Lebih')
                             break                           
                         elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             databayi.append('Gizi Kurang')
                             break                           
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             databayi.append('Gizi Buruk')
                             break                           
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             databayi.append('Gizi Normal')
                             break                          
                    elif bb<median[2]:
                         indeks = round((bb - median[2])/(median[2] - median[1]),2)
                         databayi.append(indeks)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             databayi.append('Gizi Lebih')
                             break                            
                         elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             databayi.append('Gizi Kurang')
                             break                           
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             databayi.append('Gizi Buruk')
                             break                             
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             databayi.append('Gizi Normal')
                             break                             
                    else:
                         
                         indeks = round((bb - median[2])/(median[2]),2)
                         databayi.append(indeks)
                         if indeks > 2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Lebih")
                             databayi.append('Gizi Lebih')
                             break                          
                         elif -3 <= indeks <= -2:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Kurang")
                             databayi.append('Gizi Kurang')
                             break                           
                         elif indeks < -3:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Buruk")
                             databayi.append('Gizi Buruk')
                             break                           
                         else:
                             print("--------------------")
                             print("Indeks Gizi =", round(indeks,2))
                             print("Status Gizi = Gizi Normal")
                             databayi.append('Gizi Normal')
                             break                             
                elif usia >=60:
                    print("--------------------")
                    print("Maaf bayi anda tidak termasuk bayi balita.")
                    databayi.append('Bukan bayi balita')
                    break                
               
 