import matplotlib.pyplot as plt
import numpy as np


# Creating dataset

data = np.random.normal(100, 20, 200)
print(data)



# Creating plot
plt.boxplot(data)

# show plot
plt.show()
