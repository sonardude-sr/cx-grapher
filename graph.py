# The actual graphs
import numpy as np
import matplotlib.pyplot as plt


def get_list(a, b, c):
    values = [n for n in range(a, b + c, c)]
    return values


def transform_mesh_grid(x_mesh, y_mesh):
    accumulator_list = []
    imaginary_parts = []
    real_parts = []
    for i, j in zip(np.array(x_mesh).flatten(), np.array(y_mesh).flatten()):
        n = complex(i, j)
        n = n ** 2
        accumulator_list.append(n)
    for i in accumulator_list:
        real_parts.append(i.real)
        imaginary_parts.append(i.imag)
    return real_parts, imaginary_parts


x_window = get_list(-100, 100, 20)
y_window = get_list(-100, 100, 20)
X, Y = np.meshgrid(x_window, y_window)
U, V = transform_mesh_grid(X, Y)
U = np.array(U)
V = np.array(V)
plt.quiver(X, Y, U - X.flatten(), V - Y.flatten())
plt.xlabel("Real Numbers")
plt.ylabel("Imaginary Numbers")
plt.show()
