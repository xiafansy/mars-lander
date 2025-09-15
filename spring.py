# uncomment the next line if running in a notebook
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def simulate_spring():
    # mass, spring constant, initial position and velocity
    m = 1
    k = 1
    x = 0
    v = 1

    # simulation time, timestep and time
    t_max = 100
    dt = 0.1
    t_array = np.arange(0, t_max, dt)

    # initialise empty lists to record trajectories
    x_list = []
    v_list = []

    # Euler integration
    for t in t_array:

        # append current state to trajectories
        x_list.append(x)
        v_list.append(v)

        # calculate acceleration
        a = -k * x / m

        # update velocity and position
        v = v + a * dt
        x = x + v * dt

    return t_array, x_list, v_list

# run the simulation
t_array, x_list, v_list = simulate_spring()

# plot the results
plt.figure(figsize=(10, 5))
plt.plot(t_array, x_list, label='Position (x)')
plt.plot(t_array, v_list, label='Velocity (v)')
plt.xlabel('Time (t)')
plt.ylabel('State')
plt.legend()
plt.title('Mass-Spring System Simulation')
plt.show()
