# The actual graphs
import numpy as np
import matplotlib.pyplot as plt


def get_list(a, b, c):
    values = [n for n in range(a, b + c, c)]
    return values


def len_vector(x, y):
    len_out = np.sqrt(abs((x ** 2) + (y ** 2)))
    return len_out


def transform_mesh_grid(x_mesh, y_mesh):
    accumulator_list = []
    imaginary_parts = []
    real_parts = []
    for i, j in zip(np.array(x_mesh).flatten(), np.array(y_mesh).flatten()):
        n = complex(i, j)
        n = (n - 5) ** 2
        accumulator_list.append(n)
    for i in accumulator_list:
        real_parts.append(i.real)
        imaginary_parts.append(i.imag)
    return real_parts, imaginary_parts


def create_arrow_arrays():
    x_window = get_list(-10, 10, 2)
    y_window = get_list(-10, 10, 2)
    x, y = np.meshgrid(x_window, y_window)
    u, v = transform_mesh_grid(x, y)
    u = np.array(u)
    v = np.array(v)
    return x, y, u, v


def normalize_vectors(u, v):
    u_out = []
    v_out = []
    for i, j in zip(u, v):
        vec = np.array([i, j])
        if np.linalg.norm(vec) != 0:
            vec = vec/np.linalg.norm(vec)
            u_out.append(vec[0])
            v_out.append(vec[1])
        else:
            u_out.append(0)
            v_out.append(0)
    u_out = np.array(u_out)
    v_out = np.array(v_out)
    return u_out, v_out


def color_list(u, v):
    colors_out = []
    for i, j in zip(u, v):
        colors_out.append(len_vector(i, j))
    return colors_out


def draw_graph(x, y, u, v):
    u -= x.flatten()
    v -= y.flatten()
    c = color_list(u, v)
    u, v = normalize_vectors(u, v)
    plt.quiver(x, y, u, v, c)
    plt.xlabel("Real Numbers")
    plt.ylabel("Imaginary Numbers")
    plt.show()


def main():
    X, Y, U, V = create_arrow_arrays()
    draw_graph(X, Y, U, V)


main()
