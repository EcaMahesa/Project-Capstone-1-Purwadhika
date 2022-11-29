import math

# Data Awal
my_dict = [
{'NIM':'2100','nama':'Eca','kelas':'JCDS','nilai':95, 'status':'Lulus'},
{'NIM':'2101','nama':'Lucki','kelas':'JCDS','nilai':90, 'status':'Lulus'},
{'NIM':'2102','nama':'Jason','kelas':'JCWD','nilai':100, 'status':'Lulus'}
]

# ID dan Password access guru
access_guru = [
{'ID':'Guru01', 'pass':'Rahasia'},
{'ID':'Guru02', 'pass':'Password'},
]

# ID dan Password access murid dan orangtua
access_murid_orangtua = [
{'NIM':'2100', 'pass':'orangtuaeca'},
{'NIM':'2101','pass':'orangtualucki'},
{'NIM':'2102','pass':'orangtuajason'}
]

# Format Header
def format():
    return print(f''' 
{'NIM':<13}|{'Nama':<13}|{'Kelas':<13}|{'Nilai':<13}|{'Status':<13}''')

# ini Menu access pilih
print(f'''
1.Guru
2.Murid Orang Tua / Siswa
3.Exit''')
individu = int(input('Silahkan Pilih Menu: '))


# Diminta masukin ID yang sudah ada untuk pilih guru
if individu == 1:
    accessid = input('ID: ')
    for i in range(1):
        for j in range(len(access_guru)):
            if accessid == access_guru[j]['ID']:
                accesspassword = input('Password: ')
                for i in range(1):
                    for j in range(len(access_guru)):
                        if accesspassword == access_guru[j]['pass']:
                            while True:
                                print(f'''
Welcome To Purwadhika School
List Menu:
1.Menampilkan Data Siswa
2.Menambah Data Siswa
3.Menghapus Data Siswa
4.Mengupdate Data Siswa
5.Exit Program''')
                                a = int(input(f'''Masukan Angka Menu Yang Ingin Dijalankan: '''))

                                if a == 1:
                                    while True:
                                        if a == 1:
                                            Sub_Menu = print(f'''
1.  Tampilkan Seluruh Data
2.  Tampilkan Data Siswa Tertentu
3.  Kembali Ke Menu''')
                                        b = int(input( 'Masukan Angka Sub-Menu: '))
                                        
                                        if b == 1:
                                            format()
                                            for i in range(len(my_dict)):
                                                nim = my_dict[i]['NIM'] 
                                                nama = my_dict[i]['nama'] 
                                                kelas = my_dict[i]['kelas'] 
                                                nilai = my_dict[i]['nilai'] 
                                                status = my_dict[i]['status']
                                                print(f'''{nim:<13}|{nama:<13}|{kelas:<13}|{nilai:<13}|{status:<13}''')

                                        elif b == 2:
                                            c = input('Masukan NIM Siswa Yang Ingin Di Cari: ')
                                            for i in range(1):
                                                for j in range(len(my_dict)):
                                                    if c == my_dict[j]['NIM']:
                                                        format()
                                                        print(f'''{my_dict[j]['NIM']:<13}|{my_dict[j]['nama']:<13}|{my_dict[j]['kelas']:<13}|{my_dict[j]['nilai']:<13}|{my_dict[j]['status']:<13}''')
                                                        break
                                
                                                else:
                                                    print('Data Tidak Di Temukan')                 
                                            
                                        elif b == 3:
                                            break
                                        
                                        else:
                                            continue

                                elif a == 2:
                                        while True:
                                                Sub_Menu = print(f'''
1.  Menambah Data Siswa
2.  Kembali Ke Menu''')
                                                b = int(input(
'Masukan Angka Sub-Menu: '))  
                                            
                                                if b == 1:
                                                    c = input('Masukan NIM Yang Ingin Di Tambahkan: ')
                                                    for i in range(1):
                                                        for j in range(len(my_dict)):
                                                            if c == my_dict[j]['NIM']:
                                                                print('Data Sudah Ada')
                                                                break

                                                        else:
                                                            a = input('Masukan Nama Siswa: ')
                                                            b = input('Masukan Kelas Siswa: ')
                                                            f = int(input('Masukan Nilai Siswa: '))
                                                            d = input('Masukan Status Kelulusan: ')
                                                            format()
                                                            k = (f'{c:<13}|{a:<13}|{b:<13}|{f:<13}|{d:<13}')
                                                            print(k)
                                                            dict_tambahan = {'NIM':c,'nama':a,'kelas':b,'nilai':f,'status':d}
                                                            l = input('Apakah Data Ingin Di simpan(Y/N)?: ')
                                                            if l == 'y':
                                                                my_dict.append(dict_tambahan)
                                                                print('Data Berhasil Disimpan')
                                                                break
                                                            elif l == 'n':
                                                                continue
                                                            else:
                                                                continue 
                                                elif b == 2:
                                                    break
                                                
                                                else:
                                                    continue

                                elif a == 3:
                                        while True:
                                                Sub_Menu = print(f'''
1.  Menghapus Data Siswa
2.  Kembali Ke Menu''')
                                                b = int(input(
'Masukan Angka Sub-Menu: '))  
                                            
                                                if b == 1:
                                                    c = input('Masukan NIM Yang Ingin Di Hapus: ')
                                                    for i in range(1):
                                                        for j in range(len(my_dict)):
                                                            if c == my_dict[j]['NIM']:
                                                                g = input('Apakah Anda Yakin Ingin Menghapus Data(y/n)? ')
                                                                if g == 'y':
                                                                    del my_dict[j]


                                                                break
                                                            

                                                        else:
                                                            print('Data Tidak Ditemukan')
                                                elif b == 2:
                                                    break
                                                
                                                else:
                                                    continue
                                                
                                                        
                                elif a == 4:
                                        while True:
                                                Sub_Menu = print(f'''
1.  Mengupdate Data Siswa
2.  Kembali Ke Menu''')
                                                b = int(input(
'Masukan Angka Sub-Menu: '))  
                                            
                                                if b == 1:
                                                    c = input('Masukan NIM Siswa Yang Ingin Di Update: ')
                                                    for i in range(1):
                                                        for j in range(len(my_dict)):
                                                            if c == my_dict[j]['NIM']:
                                                                format()
                                                                print(f'''{my_dict[j]['NIM']:<13}|{my_dict[j]['nama']:<13}|{my_dict[j]['kelas']:<13}|{my_dict[j]['nilai']:<13}|{my_dict[j]['status']:<13}''')
                                                                h = input('Apakah Anda Ingin Mengubah Data Siswa Ini(y/n)? ')
                                                                if h == 'y':
                                                                    o = input('Kolom Mana Yang Ingin Anda Update: ')
                                                                    if o == 'nama':
                                                                        x = input('Masukan Nama Terbaru: ')
                                                                        my_dict[j]['nama'] = x
                                                                        format()
                                                                        print(f'''{my_dict[j]['NIM']:<13}|{my_dict[j]['nama']:<13}|{my_dict[j]['kelas']:<13}|{my_dict[j]['nilai']:<13}|{my_dict[j]['status']:<13}''')
                                                                        print('Data Berhasil Di Update')
                                                                        
                                                                    elif o == 'kelas':
                                                                        x = input('Masukan kelas Terbaru: ')
                                                                        my_dict[j]['kelas'] = x
                                                                        format()
                                                                        print(f'''{my_dict[j]['NIM']:<13}|{my_dict[j]['nama']:<13}|{my_dict[j]['kelas']:<13}|{my_dict[j]['nilai']:<13}|{my_dict[j]['status']:<13}''')
                                                                        print('Data Berhasil Di Update')
                                                            
                                                                    elif o == 'nilai':
                                                                        x = input('Masukan Nilai Terbaru: ')
                                                                        my_dict[j]['nilai'] = x
                                                                        format()
                                                                        print(f'''{my_dict[j]['NIM']:<13}|{my_dict[j]['nama']:<13}|{my_dict[j]['kelas']:<13}|{my_dict[j]['nilai']:<13}|{my_dict[j]['status']:<13}''')
                                                                        print('Data Berhasil Di Update')
                                                                
                                                                    elif o == 'status':
                                                                        x = input('Masukan Status Terbaru: ')
                                                                        my_dict[j]['status'] = x
                                                                        format()
                                                                        print(f'''{my_dict[j]['NIM']:<13}|{my_dict[j]['nama']:<13}|{my_dict[j]['kelas']:<13}|{my_dict[j]['nilai']:<13}|{my_dict[j]['status']:<13}''')
                                                                        print('Data Berhasil Di Update')
                                                                    break
                                                                if h == 'n':
                                                                    break

                                                        else:
                                                            print('Data Tidak Di Temukan')
                                                            continue            
                                                                
                                                                

                                                if b == 2:
                                                    break
                                
                                elif a == 5:
                                    print('Terima kasih')
                                    break

                                else:
                                    continue


elif individu == 2:
    accessid = input('NIM Siswa: ')
    for i in range(1):
        for j in range(len(access_murid_orangtua)):
            if accessid == access_murid_orangtua[j]['NIM']:
                accesspassword = input('Password: ')
                for i in range(1):
                    for j in range(len(access_murid_orangtua)):
                        if accesspassword == access_murid_orangtua[j]['pass']:
                            while True:
                                print(f'''
Welcome To Purwadhika School
List Menu:
1.Menampilkan Data Siswa
2.Exit Program''')
                                a = int(input(f'''Masukan Angka Menu Yang Ingin Dijalankan: '''))

                                if a == 1:
                                    while True:
                                        if a == 1:
                                            Sub_Menu = print(f'''
1.  Tampilkan Seluruh Data
2.  Tampilkan Data Siswa Tertentu
3.  Kembali Ke Menu''')
                                        b = int(input( 'Masukan Angka Sub-Menu: '))
                                        
                                        if b == 1:
                                            format()
                                            for i in range(len(my_dict)):
                                                nim = my_dict[i]['NIM'] 
                                                nama = my_dict[i]['nama'] 
                                                kelas = my_dict[i]['kelas'] 
                                                nilai = my_dict[i]['nilai'] 
                                                status = my_dict[i]['status']
                                                print(f'''{nim:<13}|{nama:<13}|{kelas:<13}|{nilai:<13}|{status:<13}''')

                                        elif b == 2:
                                            c = input('Masukan NIM Siswa Yang Ingin Di Cari: ')
                                            for i in range(1):
                                                for j in range(len(my_dict)):
                                                    if c == my_dict[j]['NIM']:
                                                        format()
                                                        print(f'''{my_dict[j]['NIM']:<13}|{my_dict[j]['nama']:<13}|{my_dict[j]['kelas']:<13}|{my_dict[j]['nilai']:<13}|{my_dict[j]['status']:<13}''')
                                                        break

                                                else:
                                                    print('Data Tidak Di Temukan')                 
                                            
                                        elif b == 3:
                                            break
                                        
                                        else:
                                            continue

                                elif a == 2:
                                    print('Terima Kasih, Dan Sampai Jumpa')
                                    break

                                else:
                                    continue

elif individu == 3:
    print('Terimkasih, Dan Sumpai Jumpa')






  







