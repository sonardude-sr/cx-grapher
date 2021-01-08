# The actual graphs
import numpy as np
import matplotlib.pyplot as plt


def get_list(a, b, c):
    values = [n for n in range(a, b + c, c)]
    return values


def transform_array(a, add, multiply):
    out_list = []
    for i in a:
        accumulator = []
        for j in i:
            accumulator.append((multiply * j) + add)
        out_list.append(accumulator)
    return out_list


x_window = get_list(0, 50, 5)
y_window = get_list(0, 50, 5)
X, Y = np.meshgrid(x_window, y_window)


plt.quiver(X, Y, transform_array(X, 0, 1), transform_array(Y, 0, 1))
plt.show()
