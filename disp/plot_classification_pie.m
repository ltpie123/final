% Plot Classification Pie Chart
%
% Creates pie chart showing distribution of sequences by behavioral
% classification (regular, sensitive, chaotic).

function plot_classification_pie(data_file, output_file)
    % Default paths
    if nargin < 1
        data_file = '../obsv/logs/lyapunov_data.csv';
    end
    if nargin < 2
        output_file = 'figures/classification_pie.png';
    end

    % Read CSV data
    data = read_lyapunov_csv(data_file);

    % Count classifications
    regular_count = sum(strcmp(data.classification, 'regular'));
    sensitive_count = sum(strcmp(data.classification, 'sensitive'));
    chaotic_count = sum(strcmp(data.classification, 'chaotic'));

    counts = [regular_count, sensitive_count, chaotic_count];
    labels = {'Regular', 'Sensitive', 'Chaotic'};
    colors = [0.2, 0.4, 0.8; ...  % blue
              1.0, 0.6, 0.0; ...  % orange
              0.9, 0.2, 0.2];     % red

    % Create figure
    figure('Position', [100, 100, 700, 700]);

    % Create pie chart
    h = pie(counts);

    % Color the patches
    for i = 1:length(counts)
        set(h(2*i-1), 'FaceColor', colors(i,:));
    end

    % Add percentage labels with bold font
    for i = 1:length(counts)
        pct = 100 * counts(i) / sum(counts);
        set(h(2*i), 'FontSize', 13, 'FontWeight', 'bold');
    end

    % Title and legend
    title('Behavioral Classification of Sequences', ...
          'FontSize', 16, 'FontWeight', 'bold');
    legend(labels, 'Location', 'southoutside', 'FontSize', 12);

    % Save figure
    [output_dir, ~, ~] = fileparts(output_file);
    if ~exist(output_dir, 'dir')
        mkdir(output_dir);
    end

    print(output_file, '-dpng', '-r300');
    fprintf('Saved: %s\n', output_file);
    fprintf('  Regular: %d (%.1f%%)\n', regular_count, 100*regular_count/sum(counts));
    fprintf('  Sensitive: %d (%.1f%%)\n', sensitive_count, 100*sensitive_count/sum(counts));
    fprintf('  Chaotic: %d (%.1f%%)\n', chaotic_count, 100*chaotic_count/sum(counts));
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