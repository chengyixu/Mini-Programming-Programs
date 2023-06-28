function taylor_series_order_4
    t0 = 0;
    t_final = 2;
    step_size = 0.01;
    num_steps = (t_final - t0) / step_size;
    t = t0:step_size:t_final;

    x = zeros(1, num_steps + 1);
    x(1) = 0;  % Initial condition x(0) = 0

    for i = 1:num_steps
        % Taylor series coefficients
        f0 = exp(-t(i)^2);
        f1 = -2 * t(i) * f0;
        f2 = (4 * t(i)^2 - 2) * f0;
        f3 = -4 * t(i) * (4 * t(i)^2 - 6) * f0;

        % Taylor series expansion of order 4
        x(i + 1) = x(i) + step_size * (f0 + step_size * (f1 / 2 + step_size * (f2 / 6 + step_size * f3 / 24)));
    end

    fprintf('The approximate value of x(2) using the Taylor-series method of order 4 is: %f\n', x(end));
end
