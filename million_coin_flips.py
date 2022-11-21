import random

Heads = Tails = diff = 0
hiar =0 #Heads in a row
tiar =0 #Tails in a row
shiar=0 #Store
stiar=0 #Store
vis =''

for i in range(1000000):
	coin = random.randint(0,1)
	#print(coin)
	if coin == 1:
		vis+='H'
		Heads = Heads + 1
		hiar  = hiar  + 1
		if(tiar>stiar):
			stiar = tiar
		tiar = 0
	else:
		vis+='T'
		Tails = Tails + 1
		tiar = tiar + 1
		if(hiar>shiar):
			shiar = hiar
		hiar = 0

print(vis)
print('''



	******************************************************************************************************************************************************************
	******************************************************************************************************************************************************************''')
print("% of Heads =",Heads/10000)
print("% of Tails =",Tails/10000)
diff = Heads-Tails
print("Difference in Heads and Tails =",diff)
print("Most Heads in a row =",shiar)
print("Most Tails in a row =",stiar)



	