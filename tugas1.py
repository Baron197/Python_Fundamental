import math;
#nomor 1
x = 4;
y= 3;
z = 2;

w = ((x+y*z)/(x*y)) ** z;

#nomor 2
a = input("Masukan angka berapapun : ");
print("Kuadrat dari " + a + " = " + str((int(a) ** 2)));

#nomor 3

total = 485;
tahun = math.floor(total/360);
bulan = math.floor((total%360)/30);
minggu = math.floor(((total%360)%30)/7);
hari = math.floor(((total%360)%30)%7);
print(str(total) + ' Hari adalah');
print(str(tahun) + ' Tahun');
print(str(bulan) + ' Bulan');
print(str(minggu) + ' Minggu');
print(str(hari) + ' Hari');

#nomor 4
total = 49;
ratioTotal = 14;
satuan = total/ratioTotal;

usiaAndi = 4 * satuan;
usiaBudi = 10 * satuan;
print('Usia Andi 2 tahun lagi = ' + str(int(usiaAndi) + 2));
print('Usia Budi 2 tahun lagi = ' + str(int(usiaBudi) + 2));

#nomor 6
jamAwal = 9;
jarak = 120;
kecepatanTotal = 100/3600;
DetikTotal = jarak / kecepatanTotal;
lamaJam = math.floor(DetikTotal / 3600);
lamaMenit = math.floor((DetikTotal%3600)/60);
lamaDetik = math.floor((DetikTotal%3600)%60);

print('Lama jam = ' + str(lamaJam) + ' Lama Menit = ' + str(lamaMenit));
print('Tabraknya pukul ' + str(jamAwal + lamaJam) + ' dan menit ke ' + str(lamaMenit) + ' dan detik ke ' + str(lamaDetik));







