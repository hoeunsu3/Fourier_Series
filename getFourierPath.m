function reconstructed_path = getFourierPath(numPath, coeffs)
    % Reconstruct the path using Fourier series (vectorized).
    %
    % Inputs:
    %   coeffs  - (N+1)x1 complex Fourier coefficients.
    %   numPath - (optional) number of points to reconstruct (default: 1000)
    %
    % Output:
    %   reconstructed_path - (Mx1) complex vector (path in complex plane)

    if nargin < 2
        numPath = 1000; % default number of points
    end

    N = length(coeffs) - 1;
    n = 0:N;
    k = (-1).^n .* ceil(n / 2);  % Frequency indices (1x(N+1))

    t = (0:numPath-1)' / numPath;            % Normalized time values (Mx1)
    angle_matrix = 2 * pi * t * k;  % Mx(N+1)

    reconstructed_path = exp(1i * angle_matrix) * coeffs;  % (Mx1)
end
