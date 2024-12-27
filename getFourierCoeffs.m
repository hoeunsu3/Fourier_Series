function coeffs = getFourierCoeffs(N, ComplexPath, MaxLength)
    % Compute Fourier coefficients for a complex path.
    %
    % Inputs:
    %   N          - Number of Fourier coefficients to compute.
    %   ComplexPath - Complex representation of the path (Nx1 vector).
    %   MaxLength  - Length of the path (scalar).
    %
    % Outputs:
    %   coeffs     - Fourier coefficients (complex vector of size (N+1)x1).

    % Initialize coefficients
    coeffs = zeros(N + 1, 1); % Complex coefficients

    % Compute Fourier coefficients
    for n = 0:N
        % Determine index for positive or negative frequency
        if mod(n, 2) == 0
            idx = n / 2;
        else
            idx = -(floor(n / 2) + 1);
        end

        % Sum contributions from each point in the ComplexPath
        for i = 1:MaxLength
            angle = idx * 2 * pi * (i - 1) / MaxLength; % Angle for the Fourier transform
            coeffs(n + 1) = coeffs(n + 1) + ComplexPath(i) * exp(-1i * angle);
        end

        % Normalize by path length
        coeffs(n + 1) = coeffs(n + 1) / MaxLength;
    end
end