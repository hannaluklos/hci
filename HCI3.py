import pandas
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag



dane = pandas.read_csv(r"C:\Users\Mała\desktop\kck\sygnal.csv", delimiter=',', engine='python')

sygnal=dane ['syg1']
liczby=dane['cos']
t = np.linspace (0, 37.995, 200*37.995)
plt.plot(t, sygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()


przefiltrowany =ag.pasmowozaporowy(sygnal, 200, 49, 51)
przefiltrowanySygnal =ag.dolnoprzepustowy(przefiltrowany,200, 50)
plt.plot(t,przefiltrowanySygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()

plt.plot(liczby, przefiltrowanySygnal)
plt.xlabel("Liczby [-]")
plt.ylabel("Amplituda [-]")
plt.show()
