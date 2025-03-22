function Lines = getFourierLines(time, FourierCoeffs)
    % Compute the positions of Fourier components at a given time.
    % Input:  time (scalar) - Normalized time value (0 to 1)
    %         N (scalar) - Number of Fourier coefficients
    %         FourierCoeffs ((N+1)x1 vector) - Fourier coefficients
    %         NumPathPoints (scalar) - Total number of path points
    % Output: Lines ((N+1)x1 vector) - Fourier component positions
    
    Nf = length(FourierCoeffs);

    % Compute frequency indices
    idx = zeros(Nf, 1);
    idx(1:2:end) = floor((0:2:(Nf-1))/2);       % Even indices (positive)
    idx(2:2:end) = -floor((1:2:(Nf-1))/2) - 1;  % Odd indices (negative)

    % Compute angles at the given time
    angle = 2 * pi * idx * time; % (N+1)x1

    % Compute cumulative Fourier component positions
    Lines = cumsum(FourierCoeffs .* exp(1i * angle)); % (N+1)x1
end
