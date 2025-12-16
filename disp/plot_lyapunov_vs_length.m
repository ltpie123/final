% Plot Lyapunov Exponent vs Sequence Length
%
% Reads lyapunov_data.csv from ../obsv/logs/ and creates scatter plot
% showing how Lyapunov exponent varies with sequence length.
%
% Color-coded by classification:
%   - Blue: regular (λ < 0.1)
%   - Orange: sensitive (0.1 ≤ λ < ln(2))
%   - Red: chaotic (λ ≥ ln(2))

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
    colors = struct('regular', [0.2, 0.4, 0.8], ...
                   'sensitive', [1.0, 0.6, 0.0], ...
                   'chaotic', [0.9, 0.2, 0.2]);

    for cls = {'regular', 'sensitive', 'chaotic'}
        cls_name = cls{1};
        mask = strcmp(data.classification, cls_name);

        if any(mask)
            scatter(data.sequence_length(mask), data.lyapunov_exponent(mask), ...
                   100, colors.(cls_name), 'filled', 'DisplayName', cls_name);
        end
    end

    % Add threshold lines
    ln2 = log(2);
    yline(ln2, '--r', 'LineWidth', 1.5, 'Alpha', 0.5, ...
          'DisplayName', '\lambda = ln(2) (chaotic threshold)');
    yline(0.1, '--', 'Color', [1.0, 0.6, 0.0], 'LineWidth', 1.5, ...
          'Alpha', 0.5, 'DisplayName', '\lambda = 0.1 (sensitive threshold)');

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