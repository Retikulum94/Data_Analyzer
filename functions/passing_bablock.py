# original version written by: https://github.com/Buhin-Mara/Passing-Bablok
# downloaded 2022-11-03
# adapted by Cornelia Hofmann, 2022-11 & 2024-11-01

import numpy as np
import matplotlib.pyplot as plt
import statistics
import pandas as pd
from scipy import stats

# CSV-Datei einlesen (passen Sie 'your_file.csv' an Ihre Datei an)
df = pd.read_csv('haemoglobin_geraetevergleich_2Spalten.csv', sep=None, engine='python')

# Alle numerischen Spalten finden
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

if len(numeric_cols) == 2:
    x = np.array(df[numeric_cols[0]])
    y = np.array(df[numeric_cols[1]])
    x_label = numeric_cols[0]
    y_label = numeric_cols[1]
    print(f"Verwende Spalten: {x_label} und {y_label}")

# Fallback: Benutzer abfragen
else:
    print("Verfügbare Spalten:", df.columns.tolist())
    x_label = input("Geben Sie den Namen der X-Spalte ein: ")
    y_label = input("Geben Sie den Namen der Y-Spalte ein: ")
    x = np.array(df[x_label])
    y = np.array(df[y_label])

N=len(x)
 
# Passing-Bablok Slope Function
def Passing_Bablok(x,y):
    ng_count=0
    PB_list=[]
 
    for i in range(N):
        for j in range(N):
            if i < j:
                slope=(y[i]-y[j])/(x[i]-x[j])
                PB_list.append(slope)
                if slope<-1:
                    ng_count+=1
            else :
                pass
 
    shift=ng_count
    PB_list.sort()
 
    print(shift)
    del PB_list[:shift]
 
    #Passing-Bablok prep for confidence interval
    C_alpha=(1-0.95/2)*np.sqrt(N*(N-1)*(2*N+5)/18)
    N_PB_list=len(PB_list)
    M1=int(round((N_PB_list-C_alpha)/2))
    M2=N_PB_list-M1+1
     
    #Passing-Bablok slope calculation
    PB_coef=statistics.median(PB_list)
    PB_upper=PB_list[M2]
    PB_lower=PB_list[M1]
 
    return PB_coef,PB_upper,PB_lower

#Passing-Bablock intercept:
def Passing_BablokIntercept(xlist,ylist,slope):
    interceptlist = ylist-slope*xlist
    PB_intercept = statistics.median(interceptlist)
    
    return PB_intercept
 

# calculating slope with least-square-method
m, b, r_value, p_value, std_err = stats.linregress(x,y)

#calculate Passing-Bablock method:
m_PB, m_PB_upper, m_PB_lower=Passing_Bablok(x,y)
b_PB = Passing_BablokIntercept(x, y, m_PB)

 
print(m)
print(m_PB, m_PB_upper, m_PB_lower)
 
#Plotting the results of the least squares method and the PB method
plt.scatter(x, y, color="k")
plt.plot([x.min(), x.max()], [b+m*x.min(), b+m*x.max()],
         color="b",label="least square")
plt.plot([x.min(), x.max()], [b+m*x.min(), b+m*x.max()],
         color="b",label="slope is " + str("{:.3f}".format(m)))
plt.plot([x.min(), x.max()], [b_PB+m_PB*x.min(), b_PB+m_PB*x.max()],
         color="r", label="Passing-Bablok")
plt.plot([x.min(), x.max()], [b_PB+m_PB*x.min(), b_PB+m_PB*x.max()],
         color="r", label="slope is " + str("{:.3f}".format(m_PB)) 
         + " (" + str("{:.3f}".format(m_PB_lower)) + ", " 
         + str("{:.3f}".format(m_PB_upper)) + ")")

# Achsenbeschriftung
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.title("Least Square vs Passing-Bablok: linear Regression")
plt.legend()
plt.show()