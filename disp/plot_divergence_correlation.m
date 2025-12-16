% Plot Divergence vs Lyapunov Correlation
%
% Scatter plot showing relationship between state space divergence
% and Lyapunov exponent. Tests whether trajectory divergence in state
% space predicts sensitivity to perturbations.

function plot_divergence_correlation(data_file, output_file)
    % Default paths
    if nargin < 1
        data_file = '../obsv/logs/divergence_correlation.csv';
    end
    if nargin < 2
        output_file = 'figures/divergence_correlation.png';
    end

    % Read CSV data
    data = read_divergence_csv(data_file);

    % Create figure with two subplots
    figure('Position', [100, 100, 1200, 500]);

    % Define colors
    colors = struct('trivial', [0.5, 0.5, 0.5], ...
                   'weakly_chaotic', [0.2, 0.4, 0.8], ...
                   'strongly_chaotic', [1.0, 0.6, 0.0], ...
                   'extremely_chaotic', [0.9, 0.2, 0.2]);

    % Plot 1: Max Divergence vs Lambda
    subplot(1, 2, 1);
    hold on;
    grid on;

    for cls = {'trivial', 'weakly_chaotic', 'strongly_chaotic', 'extremely_chaotic'}
        cls_name = cls{1};
        mask = strcmp(data.classification, cls_name);

        if any(mask)
            label = strrep(cls_name, '_', ' ');
            scatter(data.max_divergence(mask), data.lambda(mask), ...
                   100, colors.(cls_name), 'filled', 'DisplayName', label);
        end
    end

    set(gca, 'XScale', 'log');
    xlabel('Max Divergence (log scale)', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel('Lyapunov Exponent \lambda', 'FontSize', 12, 'FontWeight', 'bold');
    title('State Space Divergence vs Sensitivity', 'FontSize', 14, 'FontWeight', 'bold');
    legend('Location', 'best', 'FontSize', 10);
    set(gca, 'FontSize', 11);
    box on;
    hold off;

    % Plot 2: Mean Divergence vs Lambda
    subplot(1, 2, 2);
    hold on;
    grid on;

    for cls = {'trivial', 'weakly_chaotic', 'strongly_chaotic', 'extremely_chaotic'}
        cls_name = cls{1};
        mask = strcmp(data.classification, cls_name);

        if any(mask)
            label = strrep(cls_name, '_', ' ');
            scatter(data.mean_divergence(mask), data.lambda(mask), ...
                   100, colors.(cls_name), 'filled', 'DisplayName', label);
        end
    end

    set(gca, 'XScale', 'log');
    xlabel('Mean Divergence (log scale)', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel('Lyapunov Exponent \lambda', 'FontSize', 12, 'FontWeight', 'bold');
    title('Average Divergence vs Sensitivity', 'FontSize', 14, 'FontWeight', 'bold');
    legend('Location', 'best', 'FontSize', 10);
    set(gca, 'FontSize', 11);
    box on;
    hold off;

    % Save figure
    [output_dir, ~, ~] = fileparts(output_file);
    if ~exist(output_dir, 'dir')
        mkdir(output_dir);
    end

    print(output_file, '-dpng', '-r300');
    fprintf('Saved: %s\n', output_file);

    % Find interesting cases
    fprintf('\nDivergence Analysis:\n');

    % High divergence, low lambda
    [~, idx] = sort(data.max_divergence, 'descend');
    fprintf('\nHighest state space divergence:\n');
    for i = 1:min(3, length(idx))
        fprintf('  %s: max_div=%.0f, lambda=%.3f (%s)\n', ...
                data.sequence{idx(i)}, data.max_divergence(idx(i)), ...
                data.lambda(idx(i)), data.classification{idx(i)});
    end

    % High lambda cases
    [~, idx] = sort(data.lambda, 'descend');
    fprintf('\nHighest Lyapunov exponents:\n');
    for i = 1:min(3, length(idx))
        fprintf('  %s: lambda=%.3f, max_div=%.0f (%s)\n', ...
                data.sequence{idx(i)}, data.lambda(idx(i)), ...
                data.max_divergence(idx(i)), data.classification{idx(i)});
    end
end

function data = read_divergence_csv(filename)
    % Read CSV file with header
    fid = fopen(filename, 'r');
    if fid == -1
        error('Cannot open file: %s', filename);
    end

    % Read header
    header = fgetl(fid);

    % Read data
    fmt = '%s %f %f %f %s';
    C = textscan(fid, fmt, 'Delimiter', ',');
    fclose(fid);

    % Package into struct
    data = struct();
    data.sequence = C{1};
    data.lambda = C{2};
    data.max_divergence = C{3};
    data.mean_divergence = C{4};
    data.classification = C{5};
end