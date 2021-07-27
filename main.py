
import numpy as np

def compute_hypotenuse(a, b):
    """Computes hypotenuse given the size of the other two sides"""

    return np.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    print(compute_hypotenuse(3, 4))