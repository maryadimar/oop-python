class Bunga(object):
#Contructor adalah sebuah method yang secara otomatis akan dieksekusi oleh Class 
#pada saat script dijalankan terlepas dari method mana yang akan dipanggil pertama kali. 
#method contructor biasanya menggunakan object __init__. 
	def __init__(self):
		print("ini method constructor")

	def mawar(self):
		print("jangan sentuh")

def main():
	namabunga = Bunga()
	namabunga.mawar()

main()
		