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
path_interp = spline.fnc_interparc(data, 500)
arc_length = spline.fnc_arclength(path_interp)
print(arc_length[-1], '[m]')

# ==================== Fourier series ====================
N = 100
Fourier = Fourier_series(N, data=path_interp)
function = Fourier.get_function()

# ==================== Plot ====================
plot_fourier = 'circle' # line, circle

fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter([], [], color='r')
if plot_fourier == 'line':
    line, = ax.plot([], [], color='g', label='fourier lines')
else:
    circles = [plt.Circle((np.nan, np.nan), radius=np.nan, linewidth=1, fill=False, color='g', alpha=0.5) for _ in range(N)]
    for circle in circles:
        ax.add_patch(circle)

def update(frame):
    dt = 0.01 # 100 Hz, 1 second plot
    t = frame * dt  # time index
    
    _point = Fourier.get_point(t)
    scatter.set_offsets([[_point.real, _point.imag]])

    _lines = Fourier.get_lines(t)
    if plot_fourier == 'line':
        line.set_data([_lines.real, _lines.imag])
    
        return scatter, line
    else:
        for i, circle in enumerate(circles):
            circle.set_center([_lines[i].real, _lines[i].imag])
            circle.set_radius(np.linalg.norm(_lines[(i + 1) % len(_lines)] - _lines[i]))

        return scatter, *circles


ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)
plt.plot(x, y, label='original')
plt.plot(function.real, function.imag, color='#ff7f0e', linestyle='--', label='approximated')
plt.grid()
plt.legend()

plt.show()