biodata1= {f'nama' : 'sambo',
           'umur' : 17,
          'pekerjaan' : 'pelajar',
          'pekerjaan ortu' : 'petani',
          'pendapatan':1200000,
          }
biodata2 = {f'nama' : 'kosim',
             'umur' : 17,
             'pekerjaan' : 'pelajar',
             'pekerjaan ortu' : 'wiraswasta',
             'pendapatan' : 6700000,
             }

biodata3 ={f'nama' : 'mahmud',
           'umur': 18,
           'pekerjaan':'pelajar',
           'pekerjaan ortu':'pns',
           'pendapatan':5000000,
           }

nama = str(input('masukan nama :'))
umur = int(input('masukan umur : '))
pekerjaan = str(input('masukan pekerjaan :'))
pekerjaan_ortu =str(input('masukan pekerjaan ortu :'))
pendapatan = int(input('masukan pendapatan :'))
mampu = False
tidak_mampu = True
pekerjaan_ortu_yang_tidak_berhak_dapat_KIP ={'wiraswasta','pns','dokter'}

if (umur >= 10) and (pekerjaan not in pekerjaan_ortu_yang_tidak_berhak_dapat_KIP) and (mampu or tidak_mampu) and (pendapatan <= 1500000):
    hasil = ('dapat bantuan KIP')
else: 
    hasil = ('tidak dapat bantuan KIP')    

print('nama:',nama)
print('umur:',umur)
print('pekerjaan:',pekerjaan)
print('pekerjaan ortu:',pekerjaan_ortu)
print('pendapatan:',pendapatan)
print('klasifikasi:',hasil)
