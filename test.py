import numpy as np
from pytictoc import TicToc
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from fourier_series import Interparc, Fourier_series


# ==================== Tictoc ====================
t = TicToc()

# ==================== Data import ====================
data = np.loadtxt('./paths/yongin_path_corner.csv', delimiter=',')
x = data[:, 0]
y = data[:, 1]


# ==================== Same Euclidian distance interpolation ====================
spline = Interparc()
path_interp = spline.fnc_interparc(data, ds=1)
arc_length = spline.fnc_arclength(path_interp)
print(arc_length[-1], '[m]')

# ==================== Fourier series ====================
N = 150
Fourier = Fourier_series(N, data=path_interp)
function = Fourier.get_function()

N2 = 10
Fourier2 = Fourier_series(N2, data=path_interp)
function2 = Fourier2.get_function()

# ==================== Plot ====================

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x, y, color='tab:blue', linewidth=2, linestyle='-',  label='reference path')
plt.plot(function.real, function.imag, color='tab:red', linewidth=2, linestyle='--', label=r'$N_f=70$')
plt.plot(function2.real, function2.imag, color='tab:green', linewidth=2, linestyle='-.', label=r'$N_f=5$')
plt.grid()
plt.legend()
plt.xlabel(r'$x$ [m]')
plt.ylabel(r'$y$ [m]')
plt.savefig("./fourier_coefficients.pdf")

plt.show()