import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

matplotlib.use('TkAgg')


def __create_shuffled_square_matrix(dimension):
    array_range = np.arange(dimension**2).astype(float)
    np.random.shuffle(array_range)
    return array_range.reshape(dimension, dimension)


def __plot_analysis_bar(x, y, title='', has_griding=False):
    plt.title(title)
    plt.bar(x, y)
    plt.grid(has_griding)
    plt.show()


def analyze():
    matrices = [matrix := __create_shuffled_square_matrix(5), matrix.copy()]
    array = list(map(lambda x: -x if 2 < x < 5 else x, list(range(2, 17))))
    difference = np.mean(array)
    matrices[-1][:, :] -= difference

    __plot_analysis_bar(['source', 'drain'], [linalg.det(m) for m in matrices],
                        title='Determinant changing', has_griding=True)


if __name__ == '__main__':
    analyze()
