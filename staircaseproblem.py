#recursive solution to determining the number of way you can ascend a staircase with a give number of steps and a list of step sizes

def num_steps(steps, possiblesteps):
    if steps == 0:
        return 1
    counter = 0
    for stepsize in possiblesteps:
        if steps - stepsize >=0:
            counter += num_steps(steps - stepsize, possiblesteps)
    return counter
