def signoZodiacal(mesNacimiento, diaNacimiento):
	signo = ""

	if (mesNacimiento < 1 or mesNacimiento > 12) or (diaNacimiento < 1 or diaNacimiento > 31):
	    signo = "Fecha de nacimiento inválida"
	else:
		if ((mesNacimiento==3)and(diaNacimiento>=21)) or ((mesNacimiento==4)and(diaNacimiento<=19)):
			signo = "Aries"
		elif ((mesNacimiento==4)and(diaNacimiento>=20)) or ((mesNacimiento==5)and(diaNacimiento<=20)):
			signo = "Tauro"
		elif ((mesNacimiento==5)and(diaNacimiento>=21)) or ((mesNacimiento==6)and(diaNacimiento<=20)):
			signo = "Geminis"
		elif ((mesNacimiento==6)and(diaNacimiento>=21)) or ((mesNacimiento==7)and(diaNacimiento<=22)):
			signo = "Cancer"
		elif ((mesNacimiento==7)and(diaNacimiento>=23)) or ((mesNacimiento==8)and(diaNacimiento<=22)):
			signo = "Leo"
		elif ((mesNacimiento==8)and(diaNacimiento>=23)) or ((mesNacimiento==9)and(diaNacimiento<=22)):
			signo = "Virgo"
		elif ((mesNacimiento==9)and(diaNacimiento>=23)) or ((mesNacimiento==10)and(diaNacimiento<=22)):
			signo = "Libra"
		elif ((mesNacimiento==10)and(diaNacimiento>=23)) or ((mesNacimiento==11)and(diaNacimiento<=21)):
			signo = "Escorpio"
		elif ((mesNacimiento==11)and(diaNacimiento>=22)) or ((mesNacimiento==12)and(diaNacimiento<=21)):
			signo = "Sagitario"
		elif ((mesNacimiento==12)and(diaNacimiento>=22)) or ((mesNacimiento==1)and(diaNacimiento<=19)):
			signo = "Capricornio"
		elif ((mesNacimiento==1)and(diaNacimiento>=20)) or ((mesNacimiento==2)and(diaNacimiento<=18)):
			signo = "Acuario"
		elif ((mesNacimiento==2)and(diaNacimiento>=19)) or ((mesNacimiento==3)and(diaNacimiento<=20)):
			signo = "Piscis"
		return signo

if __name__ == "__main__":
	mesNacimiento = int(input("Introduce tu mes de nacimiento: "))
	diaNacimiento = int(input("Introduce tu día de nacimiento: "))
	print(f"Tu signo es {signoZodiacal(mesNacimiento, diaNacimiento)}")


