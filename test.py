
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

bad = [np.random.randint(0,4) for i in range(24)]
good = [np.random.randint(4,6) for i in range(154)]
vgood = [np.random.randint(6,8) for i in range(24)]

sample = bad+good+vgood
print(sample)

y = [i for i in range(len(sample))]
plt.scatter(sample,y)
plt.show()
