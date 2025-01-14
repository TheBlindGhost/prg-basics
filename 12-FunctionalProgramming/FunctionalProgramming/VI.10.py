import matplotlib.pyplot as plt
import numpy as np

town = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

temp = list(map(lambda x: x,town.values()))
town = list(map(lambda x: x, town))





x = np.array(town)
y = np.array(temp)
plt.title('Temperatures in poland')
plt.xlabel('Towns')
plt.ylabel('Temperature')
plt.bar(x,y)
plt.show()