# The actual graphs
import numpy as np
import matplotlib.pyplot as plt


def get_list(a, b, c):
    values = [n for n in range(a, b + c, c)]
    return values


x_window = get_list(0, 10, 1)
y_window = get_list(0, 10, 1)
X, Y = np.meshgrid(x_window, y_window)
plt.quiver(X, Y, X, Y)
plt.show()
