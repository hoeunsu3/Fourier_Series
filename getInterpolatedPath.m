function InterpolatedPath = getInterpolatedPath(PathData, ds)
    % Interpolate the path by same arc-length intervals.
    %
    % Inputs:
    %   PathData - Nx2 matrix containing [x, y] coordinates.
    %   ds       - Desired arc-length interval.
    %
    % Outputs:
    %   InterpolatedPath - Interpolated path with same arc-length intervals.

    % Compute cumulative arc-length using external function
    s = getArcLength(PathData);

    % Generate arc-lengths at equal intervals
    s_ds = 0:ds:s(end);

    % Interpolate x and y coordinates using linear interpolation
    InterpolatedX = interp1(s, PathData(:, 1), s_ds, 'linear');
    InterpolatedY = interp1(s, PathData(:, 2), s_ds, 'linear');

    % Combine into a single Nx2 matrix
    InterpolatedPath = [InterpolatedX', InterpolatedY'];
end