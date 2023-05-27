import numpy as np
from pytictoc import TicToc
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Interparc:
    def __init__(self):
        pass

    def fnc_arclength(self, Path):
        Xd = np.diff(Path[:,0])
        Yd = np.diff(Path[:,1])
        dist = np.sqrt(Xd**2 + Yd**2)
        
        # accumulate segment distance
        dist_stack = np.cumsum(dist)
        
        return dist_stack

    def fnc_interparc(self, Path, N):        
        # Original Linear distance stack 
        dist_stack = self.fnc_arclength(Path)
        dist_stack = np.insert(dist_stack, 0, 0)
        
        # Interpolation into N array and same distance
        N_arr = np.linspace(0, dist_stack[-1], N)
        xn = np.interp(N_arr, dist_stack, Path[:,0])
        yn = np.interp(N_arr, dist_stack, Path[:,1])

        Path_I = np.vstack([xn, yn]).T
        
        return Path_I
    
    def fnc_interparc_1m(self, Path):        
        # Original Linear distance stack 
        dist_stack = self.fnc_arclength(Path)
        dist_stack = np.insert(dist_stack, 0, 0)
        
        # Interpolation into N array and same distance
        N_arr = np.linspace(0, dist_stack[-1], int(dist_stack[-1]))
        xn = np.interp(N_arr, dist_stack, Path[:,0])
        yn = np.interp(N_arr, dist_stack, Path[:,1])

        Path_I = np.vstack([xn, yn]).T
        
        return Path_I

class Fourier_series:
    def __init__(self, N=1, data=None):
        self.N = N
        self.z = self.get_complex_data(data)
        self.z_len = len(self.z)
        self.coeffs = self.get_fourier_coeffs()

    def get_complex_data(self, data):
        x = data[:, 0] 
        y = data[:, 1]
        z = x + y * 1j

        return z

    def get_fourier_coeffs(self):
        N = self.N
        z = self.z
        z_len = self.z_len

        _coeffs = np.zeros(2 * N + 1, dtype=complex)
        for n in range(-N, N + 1):
            for i in range(z_len):
                angle = n * 2 * np.pi * i / z_len
                _coeffs[n + N] += z[i] * np.exp(-1j * angle) / z_len

        return _coeffs
    
    def get_function(self):
        N = self.N
        z_len = self.z_len
        coeffs = self.coeffs
        
        _function = np.zeros(z_len, dtype=complex)
        for i in range(z_len):
            for n in range(-N, N + 1):
                angle = n * 2 * np.pi * i / z_len
                _function[i] += coeffs[n + N] * np.exp(-1j * angle)

        return _function
    
    def get_point(self, time):
        N = self.N
        z_len = self.z_len
        coeffs = self.coeffs
        _point = 0 + 0j

        i = time * self.z_len
        for n in range(-N, N + 1):
            angle = n * 2 * np.pi * i / z_len
            _point += coeffs[n + N] * np.exp(-1j * angle)

        return _point


if __name__ == "__main__":
    # ==================== Tictoc ====================
    t = TicToc()

    # ==================== Data import ====================
    data = np.loadtxt('./paths/path_interp.csv', delimiter=',')
    x = data[:, 0]
    y = data[:, 1]

    # ==================== Same Euclidian distance interpolation ====================
    spline = Interparc()
    # path_interp = spline.fnc_interparc(data, 500)
    path_interp = spline.fnc_interparc_1m(data)

    # ==================== Fourier series ====================
    Fourier = Fourier_series(N=100, data=path_interp)
    function = Fourier.get_function()
    t.tic()
    point = Fourier.get_point(0.3)
    t.toc()

    # ==================== Plot ====================
    fig = plt.figure()
    ax = fig.add_subplot(111)
    scatter = ax.scatter([], [], color='red')

    def update(frame):
        dt = 0.01
        t = frame * dt  # time index
        point = Fourier.get_point(t)
        scatter.set_offsets([[point.real, point.imag]])
        return scatter,

    ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)
    plt.plot(x, y, label='original')
    plt.plot(function.real, function.imag, label='approximated')
    plt.legend()

    plt.show()
    
