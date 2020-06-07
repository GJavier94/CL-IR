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
	c_table = createTable(len(s_table), len(s_table[0]), 0)

	for i in range(len(s_table)):
		for j in range(len(s_table[i])):
			c_table[i][j] = s_table[i][j]
	return c_table

def sort_neighbours(sourceTab, length , removal):
	#ordenando vecinos por cercania
	t_2sort = copyTable(sourceTab)

	for i in range(length):
		t_2sort[i].sort()

	if removal == True:
		for i in range(length):
			t_2sort[i].remove(t_2sort[i][0])	
	return t_2sort

def kneighbours(table_neig, k ):
	table_d=[]
	for i in range(len(table_neig)):
		table_d.append(table_neig[i][:k])
	return table_d

#msd
def funcion_1(in_tab, out_tab):
	for i in range(len(in_tab)):
		for j in range(len(in_tab)):
			if i != j:
				a = 0 
				msd = 0
				for k in range(len(in_tab[j])):				
					if ( (in_tab[i][k] != 0) and (in_tab[j][k] != 0) ):
						a = a + 1
						msd = msd + ((in_tab[i][k] - in_tab[j][k])** 2)
				out_tab[i][j] = round((pow(a,-1)*msd),2)
			else:
					out_tab[i][j] = 0
	return out_tab	
#1-msd
def funcion_3(in_tab, out_tab):
	for i in range(len(in_tab)):
		for j in range(len(in_tab)):
			if i != j:
				a = 0 
				msd = 0
				for k in range(len(in_tab[j])):				
					if ( (in_tab[i][k] != 0) and (in_tab[j][k] != 0) ):
						a = a + 1
						msd = msd + ((in_tab[i][k] - in_tab[j][k])** 2)
				out_tab[i][j] = round((1-(pow(a,-1)*msd)/16),2)
			else:
					out_tab[i][j] = 0
	return out_tab	


#formula 17  y 20
#flag = 0 17 
#flag = 1 20

def funcion_2(in_ta1, in_ta2, out_tab, flag ):
	for i in range(len(in_ta1)):
		for j in range(len(in_ta2[i])):
			g_u_i = 0
			a = 0
			for k in range(len(in_ta2)):
				if(flag == 0):
					if (in_ta1[i][k] * in_ta2[k][j]) != 0 :
						a = a + 1
						g_u_i = g_u_i + (in_ta1[i][k] * in_ta2[k][j])
				else:
					if(i != k):
						if (in_ta1[i][k] * in_ta2[k][j]) != 0 :
							a = a + 1
							g_u_i = g_u_i + (in_ta1[i][k] * in_ta2[k][j])
					
			if a == 0:
				a = 1
				
			out_tab[i][j]=round(pow(a,-1)*g_u_i,2)
	return out_tab

#formula 17  siguientes iteraciones con nuevos vecinos 
def funcion_2_recalculate(in_ta1, in_ta2, t_new_neig, flag):
	if(flag == 0): sizei = len(in_ta1)
	else: sizei = len(in_ta2)

	for i in range(sizei):
		for j in range(len(in_ta2[i])):
			g_u_i = 0
			a = 0
			for k in range(len(in_ta2)):
				if(flag == 0):
					if t_new_neig[i][k] * in_ta2[k][j] != 0:
						a = a + (t_new_neig[i][k])
						g_u_i = g_u_i + (t_new_neig[i][k]*in_ta2[k][j])
				else:
					if(i != k):
						if t_new_neig[i][k] * in_ta2[k][j] != 0:
							a = a + (t_new_neig[i][k])
							g_u_i = g_u_i + (t_new_neig[i][k]*in_ta2[k][j])
			if a == 0:
				a = 1		
			in_ta1[i][j]=round(pow(a,-1)*g_u_i,2)	
	return in_ta1

#formula 18 y 22
#flag 0 formula 18
#flag 1 formula 22
def funcion_4(in_ta1, in_ta2, t_new_neig, out_tab, flag):
	for i in range(len(in_ta1)):
		for j in range(len(in_ta2[i])):
			g_u_i = 0
			a = 0
			b = 0
			c = 0
			for k in range(len(in_ta2)):				
				if(flag == 0 ):
					if t_new_neig[i][k]*in_ta2[k][j]!=0:
						if in_ta2[k][j] != 0:
							c += 1
							b = b+((in_ta2[k][j])/c)
						a = a +(t_new_neig[i][k])
						g_u_i = g_u_i + ((t_new_neig[i][k]*in_ta2[k][j])-b)
				else:
					if t_new_neig[i][k]*in_ta2[k][j]!=0:						
						if(i != k):
							if in_ta2[k][j] != 0:
								c += 1
								b = b+((in_ta2[k][j])/c)
							a = a + (t_new_neig[i][k])
							g_u_i = g_u_i + ((t_new_neig[i][k]*in_ta2[k][j])-b)
			if a == 0:
				a = 1

			out_tab[i][j] = round(b+(pow(a,-1)*(g_u_i)),2)	
	return out_tab

def createMAE(keys, values):
	MAE = {}
	MAE = dict(zip(keys,values))
	return MAE

def calc_MAE(terror):
	suma=0
	for i in terror:

		suma+=i

	return suma/len(terror)
def msdn_calc(in_t, out_t):
	for i in range(len(in_t)):
		for j in range(len(in_t[i])):
			out_t[i][j]=in_t[i][j]*(pow(16,-1))	
	return out_t


def formula_20_iff(in_t1, in_t2, out_tab):
	for i in range(len(in_t1)):
		for j in range(len(in_t2[i])):
			if in_t2[i][j]==0:
				out_tab[i][j]=abs(in_t2[i][j]+in_t1[i][j])
			else:
				out_tab[i][j]=in_t2[i][j] 	
	return out_tab

def invert_values(int_tab, int_tab1, out_tab):
	for i in range(len(int_tab)):
		for j in range(len(int_tab[i])):
			out_tab[i][j]=1-int_tab1[i][j]

	return out_tab
def error_func(tin_1, tin_2):
	terror = []
	for i in range(len(tin_1)):
		a=0
		gui=0
		for k in range(len(tin_1[i])):
					# ~ print(i,j)
			if tin_1[i][k]!=0 and tin_2[i][k]!=0:
				a = a + 1
				gui=gui+abs(tin_1[i][k] - tin_2[i][k])
		terror.append(round((pow(a,-1)*gui),2))	
	return terror


file = open("matrix4.csv", "r")
fileString = file.read()


t5 = fileToTable(fileString)
print("\nTABLE 5\n")
print(tabulate(t5))

#creacion de la tabla 6 
t6 = createTable(5,5, 0)

t6 = funcion_1(t5, t6)


print("\nTABLE 6\n")
print(tabulate(t6))

t7 = copyTable(t6)
print("\nTABLE 7\n")
print(tabulate(t7))

t71= copyTable(t6)


t71 = sort_neighbours(t71, len(t6), True) #with removal of values



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

t10 = funcion_2(t9, t5, t10,0) #1st time (no new neighbour)

print("\nTABLE 10\n")
print(tabulate(t10))

#formula 17

#calculamos msdn con 1/16



t7_new = createTable(5,5,0)
t7_new = funcion_1(t5, t7_new)

print("\nNEW TABLE 7\n")
print(tabulate(t7_new))

# calculamos 1 - msdn 

t7_new1 = createTable(5,5,0)

t7_new1 = funcion_3(t5, t7_new1)


#print(tabulate(t7_new1, headers=["U1","U2", "U3","U4","U5"]))

#calculamos nuevos k-vecinos con k = 3

t7_new1 = sort_neighbours(t7_new1, len(t7_new1), True)

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


t10_new = funcion_2_recalculate(t10_new, t5, tnew_neig,0)

print("\nNEW TABLE 10\n")
print(tabulate(t10_new))

#Calculo de la formula 18

t11_new = createTable(5,14,0)

t11_new = funcion_4(t10_new, t5, tnew_neig, t11_new,0)

print("\nNEW TABLE 11\n")
print(tabulate(t11_new))


#Calculo de los errores 15
terror15 = error_func(t5, t10)

#print(terror15)


keys=["U1","U2","U3","U4","U5"]
MAE15 = createMAE(keys, terror15)



print("Errores absolutos medios para Ui usando k=3 usando la formula 15")
print(tabulate(MAE15.items()))
print("El MAE usando la formula 15 es: ",calc_MAE(terror15))



#Calculo de los errores 16

terror16 = error_func(t5, t10_new)

MAE16 = createMAE(keys, terror16)

print("Errores absolutos medios para Ui usando k=3 usando la formula 16")
print(tabulate(MAE16.items()))
print("El MAE usando la formula 16 es: ",calc_MAE(terror16))


	
#Calculo de los errores 17
terror17 = error_func(t5, t11_new)
MAE17 = createMAE(keys, terror17)

print("Errores absolutos medios para Ui usando k=3 usando la formula 17")
print(tabulate(MAE17.items()))
print("El MAE usando la formula 16 es: ",calc_MAE(terror17))


#Calculo de la formula 20

t20n = createTable(5,14,0)
t20n3 = createTable(5,14,0)
t20n31 = createTable(5,14,0)
t7de1 = createTable(5,5,1)


#formula 20


t20n = funcion_2(t7de1,t5, t20n, 1)
#print(tabulate(t20n))



#Calculo de la formula 20 con la restriccion si y solo si 

t24n = createTable(5,14,0)


t24n = formula_20_iff(t20n, t10, t24n)



print("Calculo de la formula 20 con la restriccion si y solo si ")
print(tabulate(t24n))

# ~ #Calculo de los errores 20

terror20 = error_func(t5, t24n)

MAE20 = createMAE(keys, terror20)

print("Errores absolutos medios para Ui usando k=3 usando la formula 20")
print(tabulate(MAE20.items()))
print("El MAE usando la formula 24 para la formula 20 es: ",calc_MAE(terror20))


#Calcullo de la formula 21
t21n = createTable(5,5,0)


#calculamos msdn multiplicando la tabla del articulo por 1/16
t7nueva = createTable(5,5,0)
t7nueva = msdn_calc(t7, t7nueva)

print(tabulate(t7nueva))

#calculamos 1- msdn 

t7nueva1 = createTable(5,5,0)
t7nueva1 = invert_values(t7, t7nueva, t7nueva1)

print(tabulate(t7nueva1))


print("\n")

# ~ #finalmente calculamos la formula 21 con lo calculado anteriormente

t10n1 = createTable(5,14,0)


t10n1 = funcion_2_recalculate(t10n1, t5,t7nueva1 , 1 )
print(tabulate(t10n1))


#Calculo de la formula 21 con la restriccion si y solo si 
t21n1 = createTable(5,14,0)

t21n1 = formula_20_iff(t20n, t10_new ,t21n1 )
			
print("Calculo de la formula 21 con la restriccion si y solo si ")
print(tabulate(t21n1))


#Calculo de los errores 20
terror21 = error_func(t5, t21n1)

MAE21 = createMAE(keys, terror21)

print("Errores absolutos medios para Ui usando k=3 usando la formula 21")
print(tabulate(MAE21.items()))
print("El MAE usando la formula 21 es: ",calc_MAE(terror21))


#Calculo de la formula 22


t11n1 = createTable(5,14,0)

t11n1 = funcion_4(t5,t5,t7nueva1,t11n1,1)
print(tabulate(t11n1))


#Calculo de la formula 21 con la restriccion si y solo si 
t22n1 = createTable(5,14,0)

t22n1 = formula_20_iff(t11n1,t11_new, t22n1)

print("Calculo de la formula 22 con la restriccion si y solo si ")
print(tabulate(t22n1))


#Calculo del error para 22
terror22 = error_func(t5, t22n1)

MAE22 = createMAE(keys, terror22)

print("Errores absolutos medios para  para la formula 22")
print(tabulate(MAE22.items()))
print("El MAE usando la formula 21 es: ",calc_MAE(terror22))


print("accuracy= ",pow(calc_MAE(terror22),-1))
