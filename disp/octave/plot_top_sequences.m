% Plot Top Sequences by Lyapunov Exponent
%
% Creates horizontal bar chart showing the sequences with highest
% Lyapunov exponents (most chaotic behavior).

function plot_top_sequences(data_file, output_file, top_n)
    % Default parameters
    if nargin < 1
        data_file = '../obsv/logs/lyapunov_data.csv';
    end
    if nargin < 2
        output_file = 'figures/top_chaotic_sequences.png';
    end
    if nargin < 3
        top_n = 10;
    end

    % Read CSV data
    data = read_lyapunov_csv(data_file);

    % Sort by Lyapunov exponent (descending)
    [sorted_lambda, idx] = sort(data.lyapunov_exponent, 'descend');

    % Take top N
    n = min(top_n, length(idx));
    top_idx = idx(1:n);
    top_sequences = data.sequence(top_idx);
    top_lambdas = sorted_lambda(1:n);
    top_classifications = data.classification(top_idx);

    % Assign colors based on classification
    colors = zeros(n, 3);
    color_map = struct('trivial', [0.5, 0.5, 0.5], ...          % gray
                      'weakly_chaotic', [0.2, 0.4, 0.8], ...    % blue
                      'strongly_chaotic', [1.0, 0.6, 0.0], ...  % orange
                      'extremely_chaotic', [0.9, 0.2, 0.2]);    % red

    for i = 1:n
        cls = top_classifications{i};
        colors(i,:) = color_map.(cls);
    end

    % Create figure
    figure('Position', [100, 100, 900, 700]);
    hold on;

    % Create horizontal bar chart
    y_pos = 1:n;
    for i = 1:n
        barh(y_pos(i), top_lambdas(i), 'FaceColor', colors(i,:), 'EdgeColor', 'k');
    end

    % Add threshold lines (Octave-compatible)
    ylims = ylim();
    plot([2.0, 2.0], ylims, '--b', 'LineWidth', 1.5);
    plot([4.0, 4.0], ylims, '--r', 'LineWidth', 1.5);
    text(2.1, n*0.1, '\lambda=2.0', 'FontSize', 10, 'Color', 'b');
    text(4.1, n*0.1, '\lambda=4.0', 'FontSize', 10, 'Color', 'r');

    % Labels and formatting
    set(gca, 'YTick', y_pos);
    set(gca, 'YTickLabel', top_sequences);
    set(gca, 'YDir', 'reverse');  % Highest at top
    ylim([0.5, n+0.5]);

    xlabel('Lyapunov Exponent \lambda', 'FontSize', 14, 'FontWeight', 'bold');
    title(sprintf('Top %d Most Chaotic Sequences', n), ...
          'FontSize', 16, 'FontWeight', 'bold');

    % Grid and styling
    grid on;
    grid minor;
    set(gca, 'FontSize', 11);
    set(gca, 'LineWidth', 1.2);
    box on;

    hold off;

    % Save figure
    [output_dir, ~, ~] = fileparts(output_file);
    if ~exist(output_dir, 'dir')
        mkdir(output_dir);
    end

    print(output_file, '-dpng', '-r300');
    fprintf('Saved: %s\n', output_file);
    fprintf('\nTop %d sequences:\n', n);
    for i = 1:n
        fprintf('  %2d. %-30s  \lambda=%.3f  (%s)\n', i, ...
                top_sequences{i}, top_lambdas(i), top_classifications{i});
    end
end

function data = read_lyapunov_csv(filename)
    % Read CSV file with header
    fid = fopen(filename, 'r');
    if fid == -1
        error('Cannot open file: %s', filename);
    end

    % Read header
    header = fgetl(fid);

    % Read data
    fmt = '%s %d %d %f %s %d %f %f %f %f %f';
    C = textscan(fid, fmt, 'Delimiter', ',');
    fclose(fid);

    % Package into struct
    data = struct();
    data.sequence = C{1};
    data.sequence_length = C{2};
    data.base_period = C{3};
    data.lyapunov_exponent = C{4};
    data.classification = C{5};
    data.perturbations_tested = C{6};
    data.mean_ratio = C{7};
    data.std_ratio = C{8};
    data.max_ratio = C{9};
    data.mean_divergence = C{10};
    data.max_divergence = C{11};
end