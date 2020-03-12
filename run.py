import os
import time
os.system("clear")
while True:
	print("""
	1.User Grab
	2.User Chek
	3.Brute Force
	4.User Grab with hastag
	exit tekan ( volume down + Z )
	""")
	pilih = input("no :")
	if pilih == "0":
		exit()
		os.system("CTRL + Z")
	elif pilih == "1":
		os.system("clear")
		os.system("python data/ug_enc.py")
	elif pilih == "2":
		os.system("clear")
		os.system("python data/uc_enc.py")
	elif pilih == "3":
		os.system("clear")
		os.system("python data/bf_enc.py")
	elif pilih == "4":
		os.system("clear")
		os.system("bash data/brute.sh")
	else:
		print("pilihan tidak ada")
		time.sleep(0.50)
		os.system("clear")
