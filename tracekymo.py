from read_file import read_file
from get_array import get_array
from find_minimum import find_minima, next_minimum
from search_low_grad import search_low_grad
from display_trajectories import display_trajectories

if __name__ == '__main__':

    """main function - run this with python3!

    """

    filename = read_file()
    data = get_array(filename)
    trajectories = []

    used_minima = []
    # get list of minima
    minima = find_minima(data)

    while 1:
        # iterate over minima, next_minimum returns -999 in case it's the last
        minimum = next_minimum(minima, used_minima)
        print(minimum)
        if minimum == -999:
            break

        used_minima.append(minimum)
        # trajectory = roll_ball(data, minimum, slope)

        # use search_low_grad to calculate each trajectory
        trajectory = search_low_grad(data, minimum)
        trajectories.append(trajectory)

        # print("on while")
    # print(trajectories)
    display_trajectories(data, trajectories)
