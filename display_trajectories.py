import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
matplotlib.interactive(True)

def display_trajectories(data, trajectories):

    """plots calculated trajectories over a kymograph.

    args:
    data - numpy matrix with kymograph data
    trajectories - list of lists of lists (yes): one list per trajectory,
    each trajectory being a list of [x,y] lists

    """

    # grayscale LUT
    plt.imshow(data, cmap='Greys')

    # create iterator for trajectory colours
    color = iter(plt.cm.rainbow(np.linspace(0, 1, len(trajectories))))
    for i in range(len(trajectories)):
        c = next(color)
        traj = np.asarray(trajectories[i])
        # print(trajectories)
        x, y = traj.T
        plt.plot(y, x, c=c)
    plt.show()
    plt.savefig("data.png")
