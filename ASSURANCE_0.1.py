B=1000000
risq=input("entrer le type de risque:  ")
if risq=="tierce collision" :
  prim=B
else:
    prim=B*1.5
pui=input("entrer le type de puissance:  ")
pui=int(pui)
if pui>=9:
   prim=prim*1.4
elif pui<6:
     prim=prim*1
else:
    prim=prim*1.2
util=input("entrer le type d'utilisation:  ")
if util=="promenade":
   prim=prim*0.90
elif util=="trajet":
    prim=prim*1.10
else:
    prim=prim*1.25
print("le montant de la prime est" ,prim)
