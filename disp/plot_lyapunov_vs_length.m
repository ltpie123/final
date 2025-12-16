% Plot Lyapunov Exponent vs Sequence Length
%
% Reads lyapunov_data.csv from ../obsv/logs/ and creates scatter plot
% showing how Lyapunov exponent varies with sequence length.
%
% Color-coded by classification (data-driven thresholds):
%   - Gray: trivial (λ = 0, single moves)
%   - Blue: weakly_chaotic (0 < λ < 2.0)
%   - Orange: strongly_chaotic (2.0 ≤ λ < 4.0)
%   - Red: extremely_chaotic (λ ≥ 4.0)

function plot_lyapunov_vs_length(data_file, output_file)
    % Default paths
    if nargin < 1
        data_file = '../obsv/logs/lyapunov_data.csv';
    end
    if nargin < 2
        output_file = 'figures/lyapunov_vs_length.png';
    end

    % Read CSV data
    data = read_lyapunov_csv(data_file);

    % Create figure
    figure('Position', [100, 100, 800, 600]);
    hold on;
    grid on;

    % Plot by classification
    colors = struct('trivial', [0.5, 0.5, 0.5], ...          % gray
                   'weakly_chaotic', [0.2, 0.4, 0.8], ...    % blue
                   'strongly_chaotic', [1.0, 0.6, 0.0], ...  % orange
                   'extremely_chaotic', [0.9, 0.2, 0.2]);    % red

    for cls = {'trivial', 'weakly_chaotic', 'strongly_chaotic', 'extremely_chaotic'}
        cls_name = cls{1};
        mask = strcmp(data.classification, cls_name);

        if any(mask)
            % Format label for legend
            label = strrep(cls_name, '_', ' ');
            scatter(data.sequence_length(mask), data.lyapunov_exponent(mask), ...
                   100, colors.(cls_name), 'filled', 'DisplayName', label);
        end
    end

    % Add threshold lines
    yline(2.0, '--b', 'LineWidth', 1.5, 'Alpha', 0.5, ...
          'DisplayName', '\lambda = 2.0 (weakly chaotic threshold)');
    yline(4.0, '--r', 'LineWidth', 1.5, 'Alpha', 0.5, ...
          'DisplayName', '\lambda = 4.0 (extremely chaotic threshold)');

    % Labels and title
    xlabel('Sequence Length', 'FontSize', 14, 'FontWeight', 'bold');
    ylabel('Lyapunov Exponent \lambda', 'FontSize', 14, 'FontWeight', 'bold');
    title('Discrete Lyapunov Exponent vs Sequence Length', ...
          'FontSize', 16, 'FontWeight', 'bold');

    % Legend
    legend('Location', 'best', 'FontSize', 11);

    % Styling
    set(gca, 'FontSize', 12);
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