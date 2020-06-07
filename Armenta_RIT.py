from tabulate import tabulate #Tabulate es una libreria que permite imprimir listas de listas como matrices 

def fileToTable(fileString):
	table = []	
	table = fileString.split('\n')	
	for i in range(0, len(table)):
		table[i] = table[i].split(',')

	for i in range(len(table)):
		for j in range(len(table[i])):
			table[i][j] = eval(table[i][j])	

	return table

def createTable(n, m, value):
	table = []
	for i in range(n):
		cols = []
		for j in range(m):
			cols.append(value)
		table.append(cols)
	return table

def copyTable(s_table):
	c_table = []
	for i in range(len(s_table)):
		c_table.append(s_table[i])
	return c_table

def kneighbours(table_neig, k ):
	table_d=[]
	for i in range(len(table_neig)):
		table_d.append(table_neig[i][:k])
	return table_d


file = open("matrix4.csv", "r")
fileString = file.read()


t5 = fileToTable(fileString)
print("\nTABLE 5\n")
print(tabulate(t5))



#creacion de la tabla 6 
t6 = createTable(5,5, 0)
for i in range(len(t5)):
	for j in range(len(t5)):
		if i != j:
			a = 0 
			msd = 0
			for k in range(len(t5[j])):				
				if ( (t5[i][k] != 0) and (t5[j][k] != 0) ):
					a = a + 1
					msd = msd + ((t5[i][k] - t5[j][k])** 2)
			t6[i][j] = round((pow(a,-1)*msd),2)
		else:
				t6[i][j] = 0

print("\nTABLE 6\n")
print(tabulate(t6))

t7 = copyTable(t6)
t71= copyTable(t6)

#ordenando vecinos por cercania
for i in range(len(t6)):
	t71[i].sort()

for i in range(len(t6)):
	t71[i].remove(t71[i][0])

print("\nTABLE 7.1\n")
print(tabulate(t71))



t8 = kneighbours(t71 , 2)	
print("\nTABLE 8\n")
print(tabulate(t8))



t9=[[0,0,1,1,1],
	[1,0,0,1,1],
	[1,0,0,1,1],
	[1,0,1,0,1],
	[0,1,1,1,0]]

t10 = createTable(5,14,0)

for i in range(len(t9)):
	for j in range(len(t5[i])):
		g_u_i = 0
		a = 0
		for k in range(len(t5)):
			if (t9[i][k] * t5[k][j]) != 0 :
				a = a + 1
				g_u_i = g_u_i + (t9[i][k] * t5[k][j])
		if a == 0:
			a = 1
			
		t10[i][j]=round(pow(a,-1)*g_u_i,2)

print("\nTABLE 10\n")
print(tabulate(t10))


#formula 17

#calculamos msdn con 1/16

t7_new = createTable(5,5,0)


for i in range(len(t5)):
	for j in range(len(t5)):
		if i != j:
			a = 0
			msd = 0
			for k in range(len(t5[j])):
				if t5[i][k] != 0 and t5[j][k] != 0:
					a = a + 1
					msd = msd + ((t5[i][k] - t5[j][k]) ** 2)
			t7_new[i][j] = round((pow(a,-1)*msd)/16,2)			
		else:
				t7_new[i][j] = 0

print("\nNEW TABLE 7\n")
print(tabulate(t7_new))

# calculamos 1 - msdn 


t7_new1 = createTable(5,5,0)

for i in range(len(t5)):
	for j in range(len(t5)):
		a = 0
		msd = 0
		for k in range(len(t5[j])):			
			if t5[i][k] != 0 and t5[j][k] != 0:
				a = a + 1
				msd = msd + ((t5[i][k] - t5[j][k])** 2)
		t7_new1[i][j] =round((1-(pow(a,-1)*msd)/16),2)



#print(tabulate(t7_new1, headers=["U1","U2", "U3","U4","U5"]))

#calculamos nuevos k-vecinos con k = 3

for i in range(len(t7_new1)):
	t7_new1[i].sort()

print("\nNEW TABLE 7_1\n")
print(tabulate(t7_new1))

#print(tabulate(t7_new1))
t8_new = kneighbours(t7_new1 , 3)	

print("\nNEW TABLE 8\n")
print(tabulate(t8_new))


#print(tabulate(t8_new))

tnew_neig = [[0,0.59,0,0.98,0.88],
		[0.59,0,0.58,0.69,0],
		[0,0.58,0,0.97,0.95],
		[0,0.69,0.97,0,0.94],
		[0.88,0.94,0,0.94,0]]


#finalmente calculamos la formula 17 con lo calculado anteriormente
t10_new = createTable(5,14,0)

for i in range(len(t10_new)):
	for j in range(len(t5[i])):
		g_u_i = 0
		a = 0
		for k in range(len(t5)):
			if tnew_neig[i][k] * t5[k][j] != 0:
				a = a + (tnew_neig[i][k])
				g_u_i = g_u_i + (tnew_neig[i][k]*t5[k][j])
		if a == 0:
			a = 1		
		t10_new[i][j]=round(pow(a,-1)*g_u_i,2)

print("\nNEW TABLE 10\n")
print(tabulate(t10_new))
#Calculo de la formula 18

t11_new = createTable(5,14,0)

for i in range(len(t10_new)):
	for j in range(len(t5[i])):
		g_u_i = 0
		a = 0
		b = 0
		c = 0
		for k in range(len(t5)):
			if tnew_neig[i][k]*t5[k][j]!=0:
				if t5[k][j] != 0:
					c += 1
					b = b+((t5[k][j])/c)
				a = a +(tnew_neig[i][k])
				g_u_i = g_u_i + ((tnew_neig[i][k]*t5[k][j])-b)

		if a == 0:
			a = 1

		t11_new[i][j] = round(b+(pow(a,-1)*(g_u_i)),2)


print("\nNEW TABLE 11\n")
print(tabulate(t11_new))



