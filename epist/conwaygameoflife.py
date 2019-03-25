import scipy.ndimage	
import numpy as np

kernel = np.array([[1,1,1],
                      [1,0,1],
                      [1,1,1]])

# we use convolution (from digital image processing) to
# compute functions based on an image's pixels
neighbors = scipy.ndimage.filters.convolve(array, kernel)
