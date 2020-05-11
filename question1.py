import numpy as np
import matplotlib.pyplot as plt

def complexiter(max_iter, x, y):
    """Finds whether or not a point on the complex xy plane remains bounded 
    in the absolute value of z squared after iterating the equation z = z*z +c 
    or runs off to infinity within the maximum number of interations
    
    Parameters:
    max_iter - Integer
    x - numeric sequence of form np.linspace(start, end, number of breakpoints)
    y - numeric sequence of form np.linspace(start, end, number of breakpoints)
    
    Returns:
    True if iterations at that point remain bounded, False otherwise
    """
    x = np.linspace(-2, 2, 500)
    y = np.linspace(-2, 2, 500)
    
    c = x[:,np.newaxis] + y[np.newaxis,:]*1j
    #start from 0
    z = 0
    
    for i in range(max_iter):
        z = z*z + c
    c_set = (abs(z) < 2)
    return(c_set)

#complex plane from -2 to 2
x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)
#determining which points in the complex plane remain bounded within 200 iterations
c_set = complexiter(200, x, y)

#plotting the image
plt.imshow(c_set.T, extent=[-2, 2, -2, 2])
plt.title("Mandelbrot Set")
plt.xlabel("x")
plt.ylabel("y")
plt.gray()
plt.show()

###now zooming into a portion of the image and trying again
#complex plane from -1 to 0
x = np.linspace(-1, 0, 500)
y = np.linspace(-1, 0, 500)
#determining which points in the complex plane remain bounded within 200 iterations
c_set = complexiter(200, x, y)

#plotting the image
plt.imshow(c_set.T, extent=[-1, 0, -1, 0])
plt.title("Zoomed In Madelbrot Set")
plt.xlabel("x")
plt.ylabel("y")
plt.gray()
plt.show()

