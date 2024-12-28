function Lines = getFourierLines(time, N, FourierCoeffs, NumPathPoints)
    % Compute the positions of Fourier components at a given time
    %
    % Inputs:
    %   time           - Normalized time value (0 to 1)
    %   N              - Number of Fourier coefficients
    %   FourierCoeffs  - Fourier coefficients (complex vector of size N+1)
    %   NumPathPoints  - Total number of path points (scalar)
    %
    % Output:
    %   Lines - Complex vector of Fourier component positions (N+1 x 1)

    Lines = zeros(N + 1, 1); % Initialize positions
    CurrentCenter = 0 + 0i; % Start at origin

    % Compute index for Fourier components
    i = time * NumPathPoints;

    for n = 0:N
        % Determine index for positive or negative frequency
        if mod(n, 2) == 0
            idx = n / 2; % Positive frequency
        else
            idx = -(floor(n / 2) + 1); % Negative frequency
        end

        % Compute angle for the current Fourier component
        angle = idx * 2 * pi * i / NumPathPoints;

        % Update the current center with the Fourier component
        CurrentCenter = CurrentCenter + FourierCoeffs(n + 1) * exp(1i * angle);

        % Store the updated center
        Lines(n + 1) = CurrentCenter;
    end
end