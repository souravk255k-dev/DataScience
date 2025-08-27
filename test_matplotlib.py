import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x=np.linspace(0,10,100)
# y=np.sin(x)
# plt.plot(x,y,color='red',linestyle='--',marker='o')
# plt.title("line plot ")
# plt.xlabel("X.axis")
# plt.ylabel("Y.axis")
# plt.show()


x=np.random.rand(50)
y=np.random.rand(50)
plt.scatter(x,y,color='blue',marker='o')
plt.title("Scatter plot")
plt.show()
