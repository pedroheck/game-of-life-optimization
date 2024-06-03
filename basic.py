# -------------------- Imports --------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap

# ---------------- Initial settings ----------------
grid_size = 100
initial_state = np.random.choice([0, 1], size=(grid_size, grid_size))
age_grid = np.zeros((grid_size, grid_size), dtype=int)

# Custom colormap with fading effect
max_age = 30
alive_color = np.array([200/255, 255/255, 240/255, 1])  # Brighter color for alive cells #64FFC8
fade_colors = np.array([
    [8/255, 238/255, 138/255, 1],   # #08EE8A
    [27/255, 30/255, 70/255, 1],    # #1B0E56
    [23/255, 3/255, 37/255, 1]      # #170325
])

# Interpolating the fade colors
fade_steps = np.linspace(0, 1, max_age)
fade_colors_interpolated = np.array([np.interp(fade_steps, [0, 0.5, 1], [fade_colors[0, i], fade_colors[1, i], fade_colors[2, i]]) for i in range(4)]).T

# Combining alive color and fade colors
colors = np.vstack((alive_color, fade_colors_interpolated[1:]))  # skip the first color (it is used for alive cells)
# Adding #170325 for cells that haven't been alive yet
colors = np.vstack(([23/255, 3/255, 37/255, 1], colors))
cmap = LinearSegmentedColormap.from_list("my_colormap", colors)

fig, ax = plt.subplots(figsize=(10, 10))
image = ax.imshow(age_grid, cmap=cmap, vmin=0, vmax=max_age)
ax.axis('off')

# Removing extra padding
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# -------------------- Functions --------------------
def update_state(state, age_grid):
    new_state = state.copy()
    new_age_grid = age_grid.copy()

    for y in range(grid_size):
        for x in range(grid_size):
            total = (state[y, (x-1)%grid_size] + state[y, (x+1)%grid_size] +
                     state[(y-1)%grid_size, x] + state[(y+1)%grid_size, x] +
                     state[(y-1)%grid_size, (x-1)%grid_size] + state[(y-1)%grid_size, (x+1)%grid_size] +
                     state[(y+1)%grid_size, (x-1)%grid_size] + state[(y+1)%grid_size, (x+1)%grid_size])

            # Applying the rules of the Game of Life
            if state[y, x] == 1: # If cell is alive
                if total < 2 or total > 3: # If the cell is undercrowded (< 2) or overcrowded (> 3), the cell dies
                    new_state[y, x] = 0
                    new_age_grid[y, x] = 1  # Recently dead starts slightly less bright than alive
                else: # If the cell is sorrounded by 2 or 3 alive cells, it remains alive
                    new_state[y, x] = 1
                    new_age_grid[y, x] = 1  # Alive cells set to 1 for distinct color
            else: # If the cell is dead
                if total == 3: # If the cell is sorrounded by 3 alive cells, it becomes alive
                    new_state[y, x] = 1
                    new_age_grid[y, x] = 1  # New alive cells set to 1
                else: # If the cell is not sorrounded by 3 alive cells, it remains dead
                    if age_grid[y, x] > 0:
                        new_age_grid[y, x] = age_grid[y, x] + 1  # Increasing the age for fading effect

    return new_state, new_age_grid

def update(frame):
    global initial_state, age_grid
    initial_state, age_grid = update_state(initial_state, age_grid)
    image.set_array(age_grid)
    return [image]

ani = FuncAnimation(fig, update, blit=True, interval=100, cache_frame_data=False)

plt.show()
