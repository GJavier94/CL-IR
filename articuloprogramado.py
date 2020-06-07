from tabulate import tabulate
# Abro archivo
f = open("matriz4.csv", "r")
# Leo archivo
f= f.read()
t5 = []
# Le hago split para cada salto de linea
t5 = f.split('\n')
t5.pop()

for i in range(len(t5)):
	t5[i] = t5[i].split(',')
	# Lo lee tal y como esta
for i in range(len(t5)):
	for j in range(len(t5[i])):
		t5[i][j] = eval(t5[i][j])

# ~ print(t5)
print(tabulate(t5))

t6=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]



#convertir a enteros
for i in range(len(t5)):
	for j in range(len(t5)):
		if i!=j:
			a=0
			msd = 0
			for k in range(len(t5[j])):
				# ~ print(i,j)
				if t5[i][k]!=0 and t5[j][k]!=0:
					a = a + 1
					msd = msd + ((t5[i][k] - t5[j][k])** 2)
			t6[i][j] =round((pow(a,-1)*msd),2)
			#t6[i][j] = a
		else:
				t6[i][j] = 0
# ~ print(tabulate(t6))

# ~ print(tabulate(t6, headers=["U1","U2", "U3","U4","U5"]))
t7=[]
for i in range(len(t6)):
	t7.append(t6[i])
# ~ print(t7)

t71=[]

for i in range(len(t6)):
	t71.append(t6[i])
# ~ print(t71)


for i in range(len(t6)):
	t71[i].sort()
# ~ print(t71)
for i in range(len(t6)):
	t71[i].remove(t71[i][0])
# ~ print(t71)
t8=[]
def kvecinos(x):
	for i in range(len(t7)):
		t8.append(t71[i][:x])
kvecinos(2)	
# ~ print(tabulate(t8))



	
				



t9=[[0,0,1,1,1],[1,0,0,1,1],[1,0,0,1,1],[1,0,1,0,1],[0,1,1,1,0]]
# ~ print(t9)
t10 = [ [ 0 for i in range(14) ] for j in range(5) ] 

for i in range(len(t9)):
	for j in range(len(t5[i])):
		gui=0
		a=0
		for k in range(len(t5)):
			if t9[i][k]*t5[k][j]!=0:
				a = a + 1
				gui = gui + (t9[i][k]*t5[k][j])
		if a==0:
			a=1
			
		# ~ print(a)
		t10[i][j]=round(pow(a,-1)*gui,2)
print(tabulate(t10))

#formula 17
#calculamos msdn multiplicando la tabla del articulo por 1/16
t7nueva = [ [ 0 for i in range(5) ] for j in range(5) ] 
for i in range(len(t5)):
	for j in range(len(t5)):
		if i!=j:
			a=0
			msd = 0
			for k in range(len(t5[j])):
				# ~ print(i,j)
				if t5[i][k]!=0 and t5[j][k]!=0:
					a = a + 1
					msd = msd + ((t5[i][k] - t5[j][k])** 2)
			t7nueva[i][j] =round((pow(a,-1)*msd)/16,2)
			#t6[i][j] = a
		else:
				t7nueva[i][j] = 0
# ~ print(t7nueva)


#calculamos 1- msdn 
t7nueva1 = [ [ 0 for i in range(5) ] for j in range(5) ] 
for i in range(len(t5)):
	for j in range(len(t5)):

		a=0
		msd = 0
		for k in range(len(t5[j])):
				# ~ print(i,j)
			if t5[i][k]!=0 and t5[j][k]!=0:
				a = a + 1
				msd = msd + ((t5[i][k] - t5[j][k])** 2)
		t7nueva1[i][j] =round((1-(pow(a,-1)*msd)/16),2)
			#t6[i][j] = a

# ~ print(t7nueva1)
# ~ print(tabulate(t7nueva1))
# ~ print(tabulate(t7nueva1, headers=["U1","U2", "U3","U4","U5"]))

#calculamos nuevos k-vecino con k =3
for i in range(len(t7nueva1)):
	t7nueva1[i].sort()
# ~ print(t7nueva1)
# ~ print(tabulate(t7nueva1))
t8nueva=[]
def kvecinos(x):
	for i in range(len(t7nueva1)):
		t8nueva.append(t7nueva1[i][:x])
kvecinos(3)	
# ~ print(t8nueva)

tnuevosv=[[0,0.59,0,0.98,0.88],[0.59,0,0.58,0.69,0],[0,0.58,0,0.97,0.95],[0,0.69,0.97,0,0.94],[0.88,0.94,0,0.94,0]]
# ~ print(tnuevosv)
print("\n")




print("\n")

#finalmente calculamos la formula 17 con lo calculado anteriormente
t10n = [ [ 0 for i in range(14) ] for j in range(5) ] 

for i in range(len(t10n)):
	for j in range(len(t5[i])):
		gui=0
		a=0
		for k in range(len(t5)):
			if tnuevosv[i][k]*t5[k][j]!=0:
				a =a+(tnuevosv[i][k])
				gui = gui + (tnuevosv[i][k]*t5[k][j])
		if a==0:
			a=1
		# ~ print(a)
		t10n[i][j]=round(pow(a,-1)*gui,2)

# ~ print(t10n)
print(tabulate(t10n))


#Calculo de la formula 18


t11n = [ [ 0 for i in range(14) ] for j in range(5) ] 

for i in range(len(t10n)):
	for j in range(len(t5[i])):
		gui=0
		a=0
		b=0
		c=0
		for k in range(len(t5)):
			if tnuevosv[i][k]*t5[k][j]!=0:
				if t5[k][j]!=0:
					c+=1
					b=b+((t5[k][j])/c)
				a =a+(tnuevosv[i][k])
				gui = gui + ((tnuevosv[i][k]*t5[k][j])-b)

		if a==0:
			a=1

		t11n[i][j]=round(b+(pow(a,-1)*(gui)),2)

# ~ print(t10n)
print(tabulate(t11n))


		


