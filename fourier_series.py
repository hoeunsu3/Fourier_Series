import numpy as np

class Interparc:
    def __init__(self):
        pass

    def fnc_arclength(self, path):
        return np.cumsum(np.sqrt(np.diff(path[:, 0])**2 + np.diff(path[:, 1])**2))

    def fnc_interparc(self, path, point_num):
        dist_stack = np.insert(self.fnc_arclength(path), 0, 0)
        
        if dist_stack[-1] < 100: 
            arr_num = np.linspace(0, dist_stack[-1], point_num) # Interpolate by number
        else: 
            arr_num = np.linspace(0, dist_stack[-1], int(dist_stack[-1])) # Interpolate by arc-length

        path_interpolated = np.column_stack([
            np.interp(arr_num, dist_stack, path[:, 0]),
            np.interp(arr_num, dist_stack, path[:, 1])
        ])
        
        return path_interpolated

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