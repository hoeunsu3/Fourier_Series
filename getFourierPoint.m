function point = getFourierPoint(time, N, MaxLength, coeffs)
    % Compute a single point on the Fourier path at a given time.
    %
    % Inputs:
    %   time       - Time value (0 to 1, normalized time).
    %   N          - Number of Fourier coefficients used.
    %   MaxLength  - Length of the path (number of points).
    %   coeffs     - Fourier coefficients (complex vector of size (N+1)x1).
    %
    % Outputs:
    %   point      - Complex point on the Fourier path at the given time.

    % Initialize the point
    point = 0 + 0i;

    % Compute index based on time
    i = time * MaxLength;

    % Compute the Fourier point
    for n = 0:N
        % Determine index for positive or negative frequency
        if mod(n, 2) == 0
            idx = n / 2;
        else
            idx = -(floor(n / 2) + 1);
        end

        % Compute angle for the Fourier component
        angle = idx * 2 * pi * i / MaxLength;

        % Accumulate the Fourier component
        point = point + coeffs(n + 1) * exp(1i * angle);
    end
end