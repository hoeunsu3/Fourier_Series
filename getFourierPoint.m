function point = getFourierPoint(time, coeffs)
    % Compute a single point on the Fourier path at a given time.
    % Input:  time (scalar) - Normalized time value (0 to 1)
    %         N (scalar) - Number of Fourier coefficients used
    %         NumPathPoints (scalar) - Number of points in the path
    %         coeffs ((N+1)x1 vector) - Fourier coefficients
    % Output: point (complex scalar) - Point on the Fourier path at the given time

    Nf = length(coeffs);

    % Compute frequency indices
    idx = zeros(Nf, 1);
    idx(1:2:end) = floor((0:2:(Nf-1))/2);       % Even indices (positive)
    idx(2:2:end) = -floor((1:2:(Nf-1))/2) - 1;  % Odd indices (negative)

    % Compute the angle for all Fourier components
    angle = 2 * pi * idx * time; % (Nf)

    % Compute the Fourier point using vectorized operations
    point = sum(coeffs .* exp(1i * angle)); % Complex scalar
end