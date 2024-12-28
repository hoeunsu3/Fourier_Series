% simulation.m
% Fourier series path animation with proper AnimationType selection

%% Clear Workspace and Command Window
clear;
close all;
clc;

%% Data Import
PathData = csvread('./paths/yongin.csv'); % Replace with your file path
x = PathData(:, 1); % X-coordinates
y = PathData(:, 2); % Y-coordinates

%% Path Interpolation
ds = 1; % Desired arc-length interval
InterpolatedPath = getInterpolatedPath(PathData, ds);
ArcLengths = getArcLength(InterpolatedPath);

%% Fourier Series Computation
N = 100; % Number of Fourier coefficients
ComplexPath = getComplexPath(InterpolatedPath);
NumPathPoints = length(ArcLengths); % Total number of path points
FourierCoeffs = getFourierCoeffs(N, ComplexPath, NumPathPoints);
ReconstructedPath = getFourierPath(N, length(ComplexPath), FourierCoeffs);

disp(['Arc Length: ', num2str(ArcLengths(end)), ' [m]']);
disp(['Number of path points: ', num2str(NumPathPoints)]);

%% Animation Type
AnimationType = 'Lines'; % Default to 'Circles', can change to 'Lines'

%% Plot Setup
figure;
hold on;
grid on;
axis equal;
xlabel('X');
ylabel('Y');
title(['Fourier Series Animation with ', AnimationType]);
plot(x, y, 'k-', 'DisplayName', 'Original Path'); % Original path
plot(real(ReconstructedPath), imag(ReconstructedPath), '--', 'DisplayName', 'Approximated Path'); % Approximated path

% Add scatter point for FourierPoint
FourierPointScatter = scatter(nan, nan, 50, 'r', 'filled', 'DisplayName', 'Fourier Point'); % Fourier point

if strcmp(AnimationType, 'Lines')
    % Add line handles for Fourier components
    LineHandles = gobjects(N + 1, 1); % Handles for lines connecting Fourier components
    for k = 1:N + 1
        LineHandles(k) = plot(nan, nan, 'b-', 'LineWidth', 0.5); % Initialize lines
        LineHandles(k).Annotation.LegendInformation.IconDisplayStyle = 'off'; % Remove legend for lines
    end
elseif strcmp(AnimationType, 'Circles')
    % Add circle handles for Fourier components (starting from the second)
    theta = linspace(0, 2 * pi, 100); % Angles for the circles
    CircleHandles = gobjects(N - 1, 1); % Handles for multiple circles
    for k = 1:N-1
        CircleHandles(k) = plot(nan, nan, 'b-', 'LineWidth', 0.5); % Initialize circles
        CircleHandles(k).Annotation.LegendInformation.IconDisplayStyle = 'off'; % Remove legend for circles
    end
else
    error('Invalid AnimationType. Choose either "Lines" or "Circles".');
end

legend;

%% Animation Parameters
fps = 60; % Frames per second
duration = 5; % Animation duration in seconds
num_frames = fps * duration;
time_values = linspace(0, 1, num_frames); % Normalized time values

%% Fourier Point Animation
for t = time_values
    % Compute lines for Fourier components
    Lines = getFourierLines(t, N, FourierCoeffs, NumPathPoints);

    if strcmp(AnimationType, 'Lines')
        % Update line plots
        for k = 1:N
            LineHandles(k).XData = [real(Lines(k)), real(Lines(k + 1))];
            LineHandles(k).YData = [imag(Lines(k)), imag(Lines(k + 1))];
        end
    elseif strcmp(AnimationType, 'Circles')
        % Update circle plots (starting from the second Fourier coefficient)
        CurrentCenter = FourierCoeffs(1); % Start from the first Fourier coefficient
        theta = linspace(0, 2 * pi, 100); % Circle angles
        for k = 2:N
            % Compute radius and center
            Radius = abs(FourierCoeffs(k));
            CircleX = real(CurrentCenter) + Radius * cos(theta);
            CircleY = imag(CurrentCenter) + Radius * sin(theta);
            CircleHandles(k - 1).XData = CircleX;
            CircleHandles(k - 1).YData = CircleY;

            % Update center
            CurrentCenter = Lines(k + 1);
        end
    end

    % Update Fourier Point Scatter
    FourierPointScatter.XData = real(Lines(end));
    FourierPointScatter.YData = imag(Lines(end));

    % Control animation speed
    pause(1 / fps);
end