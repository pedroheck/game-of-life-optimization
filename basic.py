# -------------------- Imports --------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------- Initial settings ----------------
grid_size = 100
initial_state = np.random.choice([0, 1], size=(grid_size, grid_size))

fig, ax = plt.subplots(figsize=(10, 10))
image = ax.imshow(initial_state, cmap='gray', vmin=0, vmax=1)
ax.axis('off')

# Removing extra padding
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# -------------------- Functions --------------------
def update_state(state):
    new_state = state.copy()
    
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
                else: # If the cell is sorrounded by 2 or 3 alive cells, it remains alive
                    new_state[y, x] = 1
            else: # If the cell is dead
                if total == 3: # If the cell is sorrounded by 3 alive cells, it becomes alive
                    new_state[y, x] = 1
    
    return new_state

def update(frame):
    global initial_state
    initial_state = update_state(initial_state)
    image.set_array(initial_state)
    return [image]

ani = FuncAnimation(fig, update, blit=True, interval=100, cache_frame_data=False)

plt.show()
