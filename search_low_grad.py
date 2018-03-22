import numpy as np
import matplotlib
from skimage import io

matplotlib.use("TkAgg")
matplotlib.interactive(True)


def search_low_grad(data, minimum):
    """Calculate trajectory of kymograph track starting at a minimum point by
    moving towards the lower values of gradient magnitude in a neighbourhood

    args:
    data - numpy matrix containing normalized kymograph
    minimum - [x,y] list with starting point for track

    returns:
    trajectory - list of [x,y] lists containing each pixel in the trajectory
    """

    print("searching grad")

    # calculate gradient magnitude of kymograph
    grad = np.gradient(data)
    gradmag = np.sqrt(grad[0]**2 + grad[1]**2)

    # save it as a figure just in case
    print(gradmag)
    io.imsave("grad.png", gradmag)
    grad_y = grad[0].shape[0]

    # define noise level that will cause stop at end of track
    noise_level = 0.04

    # initialise some necessary variables
    x = minimum[0]
    y = minimum[1]
    trajectory = []
    trajectory.append([x, y])
    outside_counter = 0

    # we'll have an infinite loop and break when a stop condition is reached
    while 1:

        # print(gradmag[x][y], data[x][y], lastvisited)
        # for i in range(len(lastvisited)):
        #     gradmag[lastvisited[i][0]][lastvisited[i][1]] = 99999

        # the search area is the 8-neighbourhood except for the
        #3 pixels above the current one. Here, we get the grad magnitude
        search_area = gradmag[max(int(x), 0):min(int(x+2), gradmag.shape[0]),
                              max(int(y-1), 0):min(int(y+2), gradmag.shape[1])]

        # I think this line is just me confusing myself with debug variables?
        search = search_area

        # here, we get the actual values of the image in the search area
        data_area = data[max(int(x), 0):min(int(x + 2), data.shape[0]),
                         max(int(y-1), 0):min(int(y+2), data.shape[1])]

        # depending on the shape of the search area/borders, we need indices to
        # indicate where in data_area/search_area the current pixel is
        currx = 0
        if y < 1:
            curry = 0
        else:
            curry = 1

        # we flat the current pixel so that it's never chosen as a destination
        search[currx][curry] = 9999

        # this is just messing with debug variables again, I could probably
        # just copy search_area here
        picking = np.copy(search)

        # normalising data_area
        area = data_area/np.sum(data_area)

        # grad mag should be normalised, data is normalised as well,
        # we sum both
        picking = picking + area
        # print(picking)

        # we move to the minimum of the sum grad mag + data
        moveto = np.argmin(picking)

        newpos = np.unravel_index(moveto, search.shape)
        # print(newpos)

        # we need to make sure x and y are never outside the bounds
        x = newpos[0] + max(int(x), 0)
        y = newpos[1] + max(int(y-1), 0)
        # append new point to the trajectory
        trajectory.append([x, y])
        print([x, y])

        # stop condition 1: trajectory is more than 3 times bigger than
        # the height of the image
        if len(trajectory) > 3 * grad_y:
            break

        # if the data value in the current point is considered to be noise
        # for 20 consecutive points, stop as well
        if data[x][y] > noise_level:
            outside_counter += 1
            if outside_counter > 20:
                break
        else:
            outside_counter = 0

    print(trajectory)
    return trajectory
