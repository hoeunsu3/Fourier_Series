function lines = getFourierLines(time, N, NumPathPoints, coeffs)
    % Compute intermediate points (lines) for Fourier series at a given time.
    %
    % Inputs:
    %   time           - Time value (0 to 1, normalized time).
    %   N              - Number of Fourier coefficients.
    %   NumPathPoints  - Number of points in the path.
    %   coeffs         - Fourier coefficients (complex vector of size (N+1)x1).
    %
    % Outputs:
    %   lines          - Complex array of size (N+1)x1, representing intermediate points.

    % Initialize the lines array
    lines = zeros(N + 1, 1); % Complex array to store intermediate points

    % Compute the normalized index
    i = time * NumPathPoints;

    % Compute lines based on Fourier coefficients
    for n = 1:(N + 1)
        % Determine index for positive or negative frequency
        if mod(n - 1, 2) == 0
            idx = (n - 1) / 2;
        else
            idx = -(floor((n - 1) / 2) + 1);
        end

        % Compute angle for the Fourier component
        angle = idx * 2 * pi * i / NumPathPoints;

        % Accumulate the Fourier component
        if n == 1
            lines(n) = coeffs(n) * exp(1i * angle);
        else
            lines(n) = lines(n - 1) + coeffs(n) * exp(1i * angle);
        end
    end
end