function coeffs = getFourierCoeffs(N, ComplexPath)
    % Compute Fourier coefficients for a complex path (vectorized version).
    %
    % Inputs:
    %   N           - Number of Fourier coefficients to compute.
    %   ComplexPath - Complex-valued path (vector of length M).
    %
    % Outputs:
    %   coeffs      - (N+1)x1 complex vector of Fourier coefficients.

    M = length(ComplexPath);     % Number of path samples
    t = (0:M-1) / M;             % Normalized time vector (row)

    % Generate frequency indices: 0, -1, 1, -2, 2, ...
    n = 0:N;
    k = (-1).^n .* ceil(n/2);    % Frequency indices (row)

    % Build the complex exponential matrix: each row is exp(-1i * k * t)
    E = exp(-1i * 2 * pi * (k(:) * t));  % Size (N+1) x M

    % Compute coefficients as row-wise dot product
    coeffs = (E * ComplexPath(:)) / M;  % (N+1)x1 complex vector
end
