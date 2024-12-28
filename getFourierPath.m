function reconstructed_path = getFourierPath(N, NumPathPoints, coeffs)
    % Reconstruct the path using Fourier series.
    %
    % Inputs:
    %   N              - Number of Fourier coefficients used.
    %   NumPathPoints  - Number of points in the path.
    %   coeffs         - Fourier coefficients (complex vector of size (N+1)x1).
    %
    % Outputs:
    %   reconstructed_path - Reconstructed path as a complex vector (NumPathPoints x 1).

    % Initialize the reconstructed path
    reconstructed_path = zeros(NumPathPoints, 1); % Complex path

    % Reconstruct the path using Fourier series
    for i = 1:NumPathPoints
        for n = 0:N
            % Determine index for positive or negative frequency
            if mod(n, 2) == 0
                idx = n / 2;
            else
                idx = -(floor(n / 2) + 1);
            end

            % Compute angle for the Fourier component
            angle = idx * 2 * pi * (i - 1) / NumPathPoints;

            % Accumulate the Fourier component
            reconstructed_path(i) = reconstructed_path(i) + coeffs(n + 1) * exp(1i * angle);
        end
    end
end