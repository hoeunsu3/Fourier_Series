import numpy as np

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

        _coeffs = np.zeros(N + 1, dtype=complex)
        for n in range(N + 1):
            for i in range(z_len):
                idx = n // 2 if n % 2 == 0 else -(n // 2 + 1)
                angle = idx * 2 * np.pi * i / z_len
                _coeffs[n] += z[i] * np.exp(-1j * angle) / z_len

        return _coeffs
    

    def get_function(self):
        N = self.N
        z_len = self.z_len
        coeffs = self.coeffs
        
        _function = np.zeros(z_len, dtype=complex)
        for i in range(z_len):
            for n in range(N + 1):
                idx = n // 2 if n % 2 == 0 else -(n // 2 + 1)
                angle = idx * 2 * np.pi * i / z_len
                _function[i] += coeffs[n] * np.exp(1j * angle)

        return _function
    

    def get_point(self, time):
        N = self.N
        z_len = self.z_len
        coeffs = self.coeffs
        _point = 0 + 0j

        i = time * self.z_len
        for n in range(N + 1):
            idx = n // 2 if n % 2 == 0 else -(n // 2 + 1)
            angle = idx * 2 * np.pi * i / z_len
            _point += coeffs[n] * np.exp(1j * angle)

        return _point

    def get_lines(self, time):
        N = self.N
        z_len = self.z_len
        coeffs = self.coeffs
        
        _lines = np.zeros(N + 1, dtype=complex)

        i = time * self.z_len
        for n in range(N + 1):
            idx = n // 2 if n % 2 == 0 else -(n // 2 + 1)
            angle = idx * 2 * np.pi * i / z_len
            if n != 0:
                _lines[n] = _lines[n - 1] + coeffs[n] * np.exp(1j * angle)
            else:
                _lines[n] = coeffs[n] * np.exp(1j * angle)

        return _lines