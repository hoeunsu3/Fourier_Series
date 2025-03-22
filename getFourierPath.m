function reconstructed_path = getFourierPath(N, NumPathPoints, coeffs)
    % Reconstruct the path using Fourier series (vectorized).
    %
    % Inputs:
    %   N              - Number of Fourier coefficients used.
    %   NumPathPoints  - Number of points in the path.
    %   coeffs         - (N+1)x1 complex Fourier coefficients.
    %
    % Outputs:
    %   reconstructed_path - (NumPathPoints x 1) complex path.

    % Frequency indices: 0, -1, 1, -2, 2, ...
    n = 0:N;
    k = (-1).^n .* ceil(n / 2);  % Frequency indices (1x(N+1))

    t = (0:NumPathPoints - 1)' / NumPathPoints;  % Normalized time values (Mx1)

    % Compute the full angle matrix: M x (N+1)
    angle_matrix = 2 * pi * t * k;

    % Evaluate Fourier sum: each row is a point in the reconstructed path
    reconstructed_path = exp(1i * angle_matrix) * coeffs;  % (M x 1)
end
