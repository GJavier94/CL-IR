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
def msd_calc(in_tab, out_tab):
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
def msd_inverse_calc(in_tab, out_tab):
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

def formula_17_20(in_ta1, in_ta2, out_tab, flag ):
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
def formula_17_20_recalculate(in_ta1, in_ta2, t_new_neig, flag):
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
def formula_18_22(in_ta1, in_ta2, t_new_neig, out_tab, flag):
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

def calc_errors(errors, in_table, keys):
	for error in errors:
		print("\n-----------")
		num_err = error[0]
		terror = error_func(in_table, error[1])
		MAE = createMAE(keys, terror)
		print("Errores absolutos medios para  para la formula "+ num_err)
		print(tabulate(MAE.items()))
		print("El MAE usando la formula"+ num_err +" es: ",calc_MAE(terror))
		print("accuracy= ",pow(calc_MAE(terror),-1))
		print("-----------\n")

def print_tables(tables):
	for table in tables:
		print("\nTABLE " + table[0] + "\n")
		print(tabulate(table[1]))

file = open("matrix4.csv", "r")
fileString = file.read()

t5 = fileToTable(fileString)
#creacion de la tabla 6 
t6 = createTable(5,5, 0)
t6 = msd_calc(t5, t6)
t7 = copyTable(t6)
t71= copyTable(t6)
t71 = sort_neighbours(t71, len(t6), True) #with removal of values
t8 = kneighbours(t71 , 2)	
t9=[[0,0,1,1,1],
	[1,0,0,1,1],
	[1,0,0,1,1],
	[1,0,1,0,1],
	[0,1,1,1,0]]
t10 = createTable(5,14,0)
t10 = formula_17_20(t9, t5, t10,0) #1st time (no new neighbour)
#formula 17
#calculamos msdn con 1/16

t7_new = createTable(5,5,0)
t7_new = msd_calc(t5, t7_new)

# calculamos 1 - msdn 

t7_new1 = createTable(5,5,0)
t7_new1 = msd_inverse_calc(t5, t7_new1)

#calculamos nuevos k-vecinos con k = 3

t7_new1 = sort_neighbours(t7_new1, len(t7_new1), True)

t8_new = kneighbours(t7_new1 , 3)	
tnew_neig = [[0,0.59,0,0.98,0.88],
		[0.59,0,0.58,0.69,0],
		[0,0.58,0,0.97,0.95],
		[0,0.69,0.97,0,0.94],
		[0.88,0.94,0,0.94,0]]

#finalmente calculamos la formula 17 con lo calculado anteriormente
t10_new = createTable(5,14,0)
t10_new = formula_17_20_recalculate(t10_new, t5, tnew_neig,0)

#Calculo de la formula 18
t11_new = createTable(5,14,0)
t11_new = formula_18_22(t10_new, t5, tnew_neig, t11_new,0)

#Calculo de la formula 20

t20n = createTable(5,14,0)
t20n3 = createTable(5,14,0)
t20n31 = createTable(5,14,0)
t7de1 = createTable(5,5,1)

#formula 20

t20n = formula_17_20(t7de1,t5, t20n, 1)

#Calculo de la formula 20 con la restriccion si y solo si 
t24n = createTable(5,14,0)
t24n = formula_20_iff(t20n, t10, t24n)

#Calcullo de la formula 21
t21n = createTable(5,5,0)

#calculamos msdn multiplicando la tabla del articulo por 1/16
t7nueva = createTable(5,5,0)
t7nueva = msdn_calc(t7, t7nueva)

#calculamos 1- msdn 

t7nueva1 = createTable(5,5,0)
t7nueva1 = invert_values(t7, t7nueva, t7nueva1)

t10n1 = createTable(5,14,0)
t10n1 = formula_17_20_recalculate(t10n1, t5,t7nueva1 , 1 )

#Calculo de la formula 21 con la restriccion si y solo si 
t21n1 = createTable(5,14,0)
t21n1 = formula_20_iff(t20n, t10_new ,t21n1 )

#Calculo de la formula 22

t11n1 = createTable(5,14,0)
t11n1 = formula_18_22(t5,t5,t7nueva1,t11n1,1)
#print(tabulate(t11n1))

#Calculo de la formula 21 con la restriccion si y solo si 
t22n1 = createTable(5,14,0)
t22n1 = formula_20_iff(t11n1,t11_new, t22n1)

keys=["U1","U2","U3","U4","U5"]	

tables = [
	["15",t10],
	["16",t10_new],
	["17",t11_new],
	["20",t24n],
	["21",t21n1],
	["22",t22n1]
]

print_tables(tables)

calc_errors(tables, t5, keys)

