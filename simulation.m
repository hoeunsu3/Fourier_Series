% simulation.m
% Fourier series path animation in MATLAB

%% Clear Workspace and Command Window
clear;
close all;
clc;

%% Data Import
PathData = csvread('./paths/yongin_path_corner.csv'); % Replace with your file path
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

%% Plot Setup
figure;
hold on;
grid on;
axis equal;
xlabel('X');
ylabel('Y');
title('Fourier Series Animation');
plot(x, y, 'k-', 'DisplayName', 'Original Path'); % Original path
plot(real(ReconstructedPath), imag(ReconstructedPath), '--', 'DisplayName', 'Approximated Path'); % Approximated path
scatterPoint = scatter(real(ComplexPath(1)), imag(ComplexPath(1)), 50, 'r', 'filled', 'DisplayName', 'Fourier Point'); % Fourier point
legend;

%% Animation Parameters
fps = 60; % Frames per second
duration = 5; % Animation duration in seconds
num_frames = fps * duration;
time_values = linspace(0, 1, num_frames); % Normalized time values

%% Fourier Point Animation
AnimationType = 'line'; % line or circle

for t = time_values
    % Compute the Fourier point at the current time
    FourierPoint = getFourierPoint(t, N, NumPathPoints, FourierCoeffs);

    % Update the animated scatter point
    scatterPoint.XData = real(FourierPoint);
    scatterPoint.YData = imag(FourierPoint);

    % Control animation speed
    pause(1 / fps);
end 