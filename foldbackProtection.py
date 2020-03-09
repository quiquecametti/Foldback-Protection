# Foldback protection
# By Quik-e

from pandas import DataFrame
import numpy as np

Ra = 1.0 # Conectada a Rb y colector (ohms)
Rb = np.asarray([1,1.2,1.5,1.8,2.2,3.3,3.9,4.7,5.1,5.6,6.8,8.2]) # Conectada a Ra y base (kohms)
Vo = 15.0 # Tensión de salida (V)
Io = 1.5 # Corriente de salida (A)
VBEon = 0.7 # Tensión Base - Emisor
# Rc = np.zeros(12) # Conectada a base y tierra (kohm)
#
# fb['Rc'] = (((fb['Vo']+fb['Io']*fb['Ra'])/(fb['Io']*fb['Ra']-fb['VBEon']))-1.0)*fb['Rb']
Rc = np.round(((Vo + Io * Ra) / (Io*Ra - VBEon) - 1) * Rb, 3)

foldbackDF = DataFrame({'Ra (ohm)': Ra,'Rb (kohm)': Rb,'Rc (kohm)': Rc,'Vo (V)': Vo,'Io (A)': Io,'VBEon (V)': VBEon})
print('    Rb   ')
print('---------  =  {}'.format(np.round(Rb[0] / (Rb[0] + Rc[0]),3)))
print(' Rb + Rc \n')
print(foldbackDF.to_string(index = False) + '\n')
print("Elijo Rb = 5.6 kohm y Rc = 100kohm\n")
# Elijo Rb = 5.1 kohm y Rc = 100kohm porque son los valores más cercanos a los comerciales

# Ra = 1.0 # V
Rb = 5.1e3 # ohm
Rc = 100.0e3 # ohm
Vi = 22.0 # V
# VBEon = 0.7 # V
# Vo = 15.0 # V

Iomax = (Vo * Rb / (Rb + Rc) + VBEon) / (Ra * (1 - Rb / (Rb + Rc)))
Iocc = VBEon / (Ra * (1 - Rb / (Rb + Rc)))
IomaxT1 = (VBEon * (Rb + Rc) / Rb + Vi) / (2.0 * Ra * (Rb + Rc) / Rb)
VomaxT1 = Vo * (IomaxT1-Iocc) / (Iomax - Iocc)
RomaxT1 = VomaxT1 / IomaxT1
Idf = DataFrame({'Iomax (A)': Iomax, 'Iocc (A)': Iocc, 'Io max Pd T1 (A)': IomaxT1,'Vo max Pd T1': VomaxT1,'Ro max Pd T1': RomaxT1},index = [0])
print(Idf.to_string(index = False))
