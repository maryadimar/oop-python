class Mobil():
	"""docstring for Mobil"""
	def __init__(self, nama):
		self.nama = nama

	def maju(self):
		print("Mobil", self.nama ,"maju")

	def mundur(self):
		print("Mobil", self.nama ,"mundur")


def main():
	avanza = Mobil('Avanza putih')
	avanza.maju()
	avanza.mundur()

main()
		
		