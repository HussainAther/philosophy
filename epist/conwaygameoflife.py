import scipy.ndimage	
import numpy as np
import matplotlib.pyplot as plt

"""
In Conway's game of Life (Conway GoL), we watch how a system of cellular
automata (CA) evolve over time.
"""

w = np.array([[1,1,1],[1,0,1],[1,1,1]])

n = 5 # grid size
m = "wrap" # used for numpy's convolve 
a = np.random.random_integers(0, 1, (n, n))

# we use convolution (from digital image processing) to
# compute functions based on an image's pixels
neighbors = scipy.ndimage.filters.convolve(array, kernel)

def step(a, w, m):
    """
    Step forward in time for some array a with weights w and mode m.
    """
    con = scipy.ndimage.filters.convolve(a, w, m)

def update(a, cmap):
    """
    Update the display with each step.
    """
    pcolor = plot.pcolor(a, cmap=cmap)
    fig.canvas.draw()

def animate_callback(a, w, m, steps):
    """
    Invoke the step function to update and update the display.
    """
    cmap = matplotlib.cm.gray_r # color map
    for i in range(steps):
         step(a, w, m)
         update(a, cmap)

fig = plt.figure()
plt.axis([0, n, 0, n])
plt.xticks([])
plt.yticks([])
pcolor = None

steps = 10 
fig.canvas.manager.window.after(1000, animate_callback)

"""
As Conway's GoL runs, patterns (Methuselahs) emerge. From most initial conditions,
GoL reaches a stable state. 

Conway's conjecture concerns whether the initial patterns stabilize. 
According to Stephen Wolfram's Principle of Computational Equivalence (as outlined in cellularautomata.py),
GoL should be (and is) Class 4 and Turing Complete. 
"""
