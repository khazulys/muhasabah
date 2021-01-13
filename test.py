import matplotlib
import matplotlib.pyplot as plt
import datetime, os
from datetime import date

f = open('records/records.txt','a')
ulang = 'ya'
total = 0
kun = 'ya'
tung = 0
def perbuatanBuruk():
	with open('records/total_keburukan.lst','a') as files:
		global kun, tung
		try:
			while(kun=='ya'):
				tung += 1
				sifat = input('Perbuatan Burukmu? ')
				f.write(f'Buruk: {sifat}\n')
				kun = input('Ada lagi perbuatan Burukmu? ')
		except KeyboardInterrupt:
			print('Wah hebat! Perbuatan burukmu {Null} hari ini.')
		rest = tung * 10
		files.write(f'{rest}\n')
		return rest

def perbuatanBaik():
	with open('records/total_kebaikan.lst','a') as files:
		global total,ulang
		while(ulang=='ya'):
			total += 1
			sifat= input('Perbuatan Baikmu? ')
			f.write(f'Baik: {sifat}\n')
			ulang = input('Ada lagi perbuatan Baikmu? ')
		rest = total * 10
		files.write(f'{rest}\n')
		return rest

def akumulasi_baik():
	with open('records/total_kebaikan.lst','r') as f:
		akumulasi = (len(f.readlines())*100) / 10
	return akumulasi

def akumulasi_buruk():
	with open('records/total_keburukan.lst','r') as a:
		akumulasii = (len(a.readlines())*100) / 10
	return akumulasii

def get_allrecords():
	tgl = datetime.date.today()
	date = str(tgl).split('-')
	year, month, day = date
	day_name = datetime.date(int(year), int(month), int(day))
	if day_name.strftime('%A')=='Sunday':
		left = [1, 2]
		heigth = []
		heigth.append(akumulasi_baik())
		heigth.append(akumulasi_buruk())
		tick_label = ['Kebaikan','Keburukan']
		fig = plt.figure()
		plt.bar(left, heigth, tick_label=tick_label, width=0.8, color=['green','red'])
		plt.xlabel('Total pahala: hanya Allah yang tau\nTotal Dosa: hanya Allah yang tau')
		plt.ylabel('Total')
		plt.title('Akumulasi total kebaikan/keburukanmu')
		fig.savefig('diagram.png')
		os.system('xdg-open diagram.png')
	else:
		perbuatanBaik();print('');perbuatanBuruk()
		print('Perbuatan baik/burukmu telah disimpan direcords')

if __name__=="__main__":
	import os;os.system('clear')
	import datetime
	from datetime import date
	print('''
		MUHASABAH
		---------\n''')
	tgl = datetime.date.today()
	date = str(tgl).split('-')
	year, month, day = date
	day_name = datetime.date(int(year), int(month), int(day))
	name = day_name.strftime("%A")
	tanggal = date
	print(f'\t{name}, {tanggal[2]}-{tanggal[1]}-{tanggal[0]}\n')
	get_allrecords()

