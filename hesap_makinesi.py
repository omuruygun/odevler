print("""
********************************
Hesap Makinesine Hoşgeldiniz :
İşlemler: 
1- Toplama 
2- Çıkarma 
3- Çarpma 
4- Bölme 
Çıkmak için q 'ya basınız.

""")
while True:
	işlem = input("Lütfen yapmak istediğiniz işlemi giriniz: ")
	if işlem not in ["1","2","3","4","q"]:
		print("Hatalı işlem girdiniz!!")
		continue
	else:
		if işlem == "q":
			print("Bizi tercih ettiğiniz için teşekürler...")
			break
		else:
			try:
				sayı1 = float(input("Birinci sayıyı giriniz: "))
				sayı2 = float(input("İkinci sayıyı giriniz:  "))
			except:
				print("Lütfen inputu doğru giriniz !! ")
				continue

			if işlem == "1":
				print("Girdiğiniz sayıların toplamı{} 'dir".format(sayı1+sayı2))
			elif işlem == "2":
				print("Girdiğiniz sayıların farkı {} 'dir".format(sayı1-sayı2))			
			elif işlem == "3":
				print("Girdiğiniz sayıların çarpımı{} 'dir".format(sayı1*sayı2))
			elif işlem == "4":
				try:
					print("Girdiğiniz sayıların bölümü{} 'dir".format(sayı1/sayı2))
				except ZeroDivisionError:
					print("Sıfır ile bölme yapılamaz")
