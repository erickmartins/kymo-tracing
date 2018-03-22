import numpy as np


def find_minima(data):
    """return a list with all minima in the first row.

    args:
    data - a numpy matrix read from the image file.

    returns:
    minima - a list with [x, y] lists for each minimum
    """

    minima = []
    window = 30  # window where minimum is searched
    noise_level = 0.5  # anything above this level is considered noise

    # now we pad the input data so we can do windowing correctly
    data_padded = np.pad(data, window, mode='edge')
    # print(data_padded[window][:])
    for i in range(data.shape[1]):
        # print(i)

        # this is the range on which we check the minimum
        checking = data_padded[window, i:i+2*window]
        # print(checking)

        # we remove the central element...
        checking = np.delete(checking, window)
        # print(checking)

        # ...and compare everything else to it.
        if data[0, i] <= min(checking) and \
                above_noise(data[0, i], noise_level):
            print("minimum!", data[0, i], i)
            minima.append([0, i])
    length = len(minima)
    count = 0
    while count < length-1:

        # we also remove minima on consecutive pixels, since they are
        # normally from the same track
        if minima[count][1]+1 == minima[count+1][1]:
            del(minima[count])
            # print(minima)
            count -= 1 
            length -= 1
        count += 1
    print(minima)
    return minima
    # row = data[y_value, :]
    # index_min = [y_value, np.argmin(row)]
    # min_value = data[index_min[0], index_min[1]]
    # new_y = y_value
    # return [[index_min, min_value], new_y]


def above_noise(point, noise):
    """simple check for whether a point is above noise level or not.

    args:
    point - numerical value
    noise - numerical value

    returns:
    boolean value
    """

    if point < noise:
        return 1
    else:
        return 0

def next_minimum(minima, used_minima):

    """returns the next minimum on a list of minima.

    args:
    minima - list of [x,y] lists
    used_minima - list of [x,y] lists

    returns:
    single [x,y] list
    """

    currminimum = len(used_minima)
    if currminimum < len(minima):

        return minima[currminimum]
    else:
        return -999

# to do: find minima in first line, then calculate vertical gradients and use maxima
# (or highest abs values of a negative) as starting points)

if __name__ == '__main__':
    from read_file import read_file
    from get_array import get_array
    filename = read_file()
    data = get_array(filename)
    minima = find_minima(data)
    print(minima)
