print(""""
************************
ŞİFRE BELİRLEME
************************
""")
while True:
	try:
		parola = int(input("Lütfen parolanızı giriniz: "))
	except:
		print("Lütfen rakamlardan oluşan bir parola giriniz!!")
		continue
	if len(str(parola)) != 4 :
		print("Lütfen şifrenizi 4 haneli olacak şekilde giriniz!!")
		continue
	else:
		print("Yeni parolanız {}'dir".format(parola))
		break