% main.m
% Function handle for the given functions
f1 = @(x) log(x);
f2 = @(x) tan(x);
f3 = @(x) sin(x^2 + (1/3)*x);

% Test the program with the given functions
n = 5; % Number of iterations for Richardson extrapolation
result1 = richardson_extrapolation(f1, 3, n);
result2 = richardson_extrapolation(f2, asin(0.8), n);
result3 = richardson_extrapolation(f3, 0, n);

fprintf('Results:\n');
fprintf('a. ln(x) at x = 3: %f\n', result1);
fprintf('b. tan(x) at x = sin^(-1)(0.8): %f\n', result2);
fprintf('c. sin(x^2 +(1/3)x) at x = 0: %f\n', result3);

% Richardson extrapolation algorithm
function result = richardson_extrapolation(f, x, n)
    R = zeros(n, n);
    h = 1;

    for i = 1:n
        h = h / 2;
        R(i, 1) = fd(f, x, h);

        for j = 2:i
            R(i, j) = R(i, j-1) + (R(i, j-1) - R(i-1, j-1)) / (4^(j-1) - 1);
        end
    end

    result = R(n, n);
end

% First derivative using central difference formula
function result = fd(f, x, h)
    result = (f(x + h) - f(x - h)) / (2 * h);
end
