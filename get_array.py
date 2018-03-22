from skimage import io
from skimage import color
import numpy as np


def normalized(a, axis=-1, order=2):
    """Returns a normalised version of the input array/matrix,
    so that all elements sum to 1

    args:
    a: array or matrix
    axis, order: arguments used to calculate the norm of the
    array/matrix


    returns:
    array or matrix with sum of elements equal to 1
    """
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2 == 0] = 1
    return a / np.expand_dims(l2, axis)


def get_array(filename):
    """Reads an array from an image filename

    args:
    filename: string with the location of the input image


    returns:
    data: normalised array/matrix with data from the input image
    """
    data = io.imread(filename)
    data = color.rgb2grey(data)
    data = np.array(data)
    data = normalized(data)
    print(data)
    return(data)
