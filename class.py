#Class – Blueprint yang dibuat oleh programmer untuk sebuah object. 
#Class Ini mendefinisikan satu set atribut 
#yang akan mengkarakterisasi sebuah object yang dicontohkan dari class ini.
class Mobile:
	def maju(self):
		print("Mobil saya maju")	

	def mundur(self):
		print("mobil saya mundur")
#Object – Contoh dari sebuah Class. 
#Object Ini adalah versi class yang direalisasikan, 
#dimana class dimanifestasikan ke dalam sebuah program.
#object = turunan dari class
def main():
	avanza = Mobile()
	avanza.maju()
	avanza.mundur()

main()