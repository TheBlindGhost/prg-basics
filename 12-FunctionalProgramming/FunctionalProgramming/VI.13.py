import matplotlib.pyplot as plt
import numpy as np

score = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

count = list(map(lambda x:x["country"],score))
medals = list(map(lambda x: x["gold"]+x['silver']+x['bronze'],score))




x = np.array(count)
y = np.array(medals)
plt.title('Countries at the Olimpics')
plt.xlabel('Countrie')
plt.ylabel('Medals')
plt.bar(x,y)
plt.show()