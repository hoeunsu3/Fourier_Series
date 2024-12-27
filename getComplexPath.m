function ComplexPath = getComplexPath(PathData)
    % Convert 2D path data (x, y) into complex numbers.
    %
    % Inputs:
    %   PathData    - Nx2 matrix containing [x, y] coordinates.
    %
    % Outputs:
    %   ComplexPath - Complex representation of the path (Nx1 complex vector).

    % Extract x and y coordinates
    x = PathData(:, 1); % First column: x-coordinates
    y = PathData(:, 2); % Second column: y-coordinates

    % Convert to complex numbers
    ComplexPath = x + 1i * y;
end