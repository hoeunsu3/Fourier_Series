function ArcLengths = getArcLength(PathData)
    % Compute cumulative arc-length of the path.
    %
    % Input:
    %   PathData    - Nx2 matrix containing [x, y] coordinates.
    %
    % Output:
    %   ArcLengths  - Cumulative arc-lengths.

    % Compute differences between consecutive points
    DeltaX = diff(PathData(:, 1));
    DeltaY = diff(PathData(:, 2));

    % Compute distances between consecutive points
    SegmentLengths = sqrt(DeltaX.^2 + DeltaY.^2);

    % Cumulative sum of segment lengths
    ArcLengths = [0; cumsum(SegmentLengths)];
end