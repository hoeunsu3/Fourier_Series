import numpy as np
from pytictoc import TicToc
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from fourier_series import Interparc, Fourier_series


# ==================== Tictoc ====================
t = TicToc()

# ==================== Data import ====================
data = np.loadtxt('./paths/interpolated_path.csv', delimiter=',')
x = data[:, 0]
y = data[:, 1]


# ==================== Same Euclidian distance interpolation ====================
spline = Interparc()
# path_interp = spline.fnc_interparc(data, 500)
path_interp = spline.fnc_interparc_1m(data)
# arc length
arc_length = spline.fnc_arclength(path_interp)
print(arc_length[-1])

# ==================== Fourier series ====================
Fourier = Fourier_series(N=100, data=path_interp)
function = Fourier.get_function()


# ==================== Plot ====================
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter([], [], color='r')
line, = ax.plot([], [], color='g', label='fourier lines')

def update(frame):
    dt = 0.01 # 100 Hz, 1 second plot
    t = frame * dt  # time index
    
    _point = Fourier.get_point(t)
    scatter.set_offsets([[_point.real, _point.imag]])

    _lines = Fourier.get_lines(t)
    line.set_data([_lines.real, _lines.imag])

    return scatter, line


ani = animation.FuncAnimation(fig, update, frames=100, interval=200, blit=True)
plt.plot(x, y, label='original')
plt.plot(function.real, function.imag, label='approximated')
plt.grid()
plt.legend()

plt.show()

