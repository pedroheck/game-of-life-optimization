# -------------------- Imports --------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------- Initial settings ----------------
grid_size = 100
initial_state = np.random.rand(grid_size, grid_size) > 0.8

fig, ax = plt.subplots(figsize=(10, 10))
image = ax.imshow(initial_state, cmap='gray', vmin=0, vmax=1)
ax.axis('off')


# -------------------- Functions --------------------
def update_state(state):
    new_state = np.zeros_like(state)
    
    for y in range(1, state.shape[0] - 1):
        for x in range(1, state.shape[1] - 1):
            total = (
                state[y-1, x-1] + state[y-1, x] + state[y-1, x+1] + state[y, x-1] + 0 + state[y, x+1] + state[y+1, x-1] + state[y+1, x] + state[y+1, x+1])
            
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

ani = FuncAnimation(fig, update, blit=True, interval=100)

plt.show()
