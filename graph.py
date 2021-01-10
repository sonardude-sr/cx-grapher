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
        n = n + 1
        accumulator_list.append(n)
    for i in accumulator_list:
        real_parts.append(i.real)
        imaginary_parts.append(i.imag)
    return real_parts, imaginary_parts


def create_plot():
    x_window = get_list(-5, 5, 1)
    y_window = get_list(-5, 5, 1)
    x, y = np.meshgrid(x_window, y_window)
    u, v = transform_mesh_grid(x, y)
    u = np.array(u)
    v = np.array(v)
    plt.quiver(x, y, u - x.flatten(), v - y.flatten())
    plt.xlabel("Real Numbers")
    plt.ylabel("Imaginary Numbers")
    plt.show()


create_plot()
