cpt=0
for i in range(0,2):
       n=input("entrer le nombre de matiere contenu dans l'UV:  ")
       n=int(n)
       for a in range(0,n):
              Dev=input("entrer la note de devoir :  ")
              Dev=int(Dev)
              Dev=Dev*0.4
              exam=input ("entrer la note d'examen : ")
              exam=int(exam)
              exam=exam*0.6
              note=(Dev+exam)
              if note<6:
                cpt=cpt+1
if cpt>=1:
 print ("ECHOUE")
else:
 print ("ADMIS")
		
