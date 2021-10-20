age=input("entrer l'age de l'enfant: ")
age=int(age)
if age<6:
	print("pas de categorie")
elif age<8:
	print("poussin")
if age<10:
	print("pupille")
elif age<12:
	print("minime")
else:
	print("cadet")	
