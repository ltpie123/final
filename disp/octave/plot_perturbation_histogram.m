% Plot Perturbation Sensitivity Distribution
%
% Shows histogram of period ratios from all perturbations tested.
% Reveals the "spectrum" of chaos - some perturbations cause massive
% period increases (up to 10,080×!) while others are mild.

function plot_perturbation_histogram(data_file, output_file)
    % Default paths
    if nargin < 1
        data_file = '../obsv/logs/perturbation_distribution.csv';
    end
    if nargin < 2
        output_file = 'figures/perturbation_histogram.png';
    end

    % Read CSV data
    data = csvread(data_file, 1, 0);  % Skip header
    ratios = data(:, 1);

    % Create figure
    figure('Position', [100, 100, 1000, 600]);

    % Create logarithmic histogram
    % Use log-spaced bins to show the wide range
    edges = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000];

    % Count values in each bin
    counts = histc(ratios, edges);

    % Create bar plot with log scale
    subplot(1, 2, 1);
    barh(1:length(edges), counts, 'FaceColor', [0.2, 0.4, 0.8], 'EdgeColor', 'k');
    set(gca, 'YTick', 1:length(edges));
    set(gca, 'YTickLabel', arrayfun(@(x) sprintf('%.0f', x), edges, 'UniformOutput', false));
    set(gca, 'YDir', 'reverse');
    xlabel('Count', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel('Period Ratio Threshold', 'FontSize', 12, 'FontWeight', 'bold');
    title('Perturbation Sensitivity Histogram', 'FontSize', 14, 'FontWeight', 'bold');
    grid on;
    set(gca, 'FontSize', 11);

    % Cumulative distribution
    subplot(1, 2, 2);
    sorted_ratios = sort(ratios);
    n = length(sorted_ratios);
    plot(sorted_ratios, (1:n)/n * 100, 'LineWidth', 2, 'Color', [0.9, 0.2, 0.2]);
    set(gca, 'XScale', 'log');
    xlabel('Period Ratio (log scale)', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel('Cumulative Percentage', 'FontSize', 12, 'FontWeight', 'bold');
    title('Cumulative Distribution', 'FontSize', 14, 'FontWeight', 'bold');
    grid on;
    set(gca, 'FontSize', 11);
    ylim([0, 100]);

    % Add reference lines
    hold on;
    xlims = xlim();
    plot(xlims, [50, 50], '--k', 'LineWidth', 1);
    text(xlims(1)*2, 52, 'median', 'FontSize', 10);

    % Find and mark key percentiles
    p50 = sorted_ratios(round(n*0.5));
    p90 = sorted_ratios(round(n*0.9));
    p99 = sorted_ratios(round(n*0.99));
    fprintf('Median ratio: %.1f\n', p50);
    fprintf('90th percentile: %.1f\n', p90);
    fprintf('99th percentile: %.1f\n', p99);
    hold off;

    % Save figure
    [output_dir, ~, ~] = fileparts(output_file);
    if ~exist(output_dir, 'dir')
        mkdir(output_dir);
    end

    print(output_file, '-dpng', '-r300');
    fprintf('Saved: %s\n', output_file);

    % Print statistics
    fprintf('\nPerturbation Sensitivity Statistics:\n');
    fprintf('  Total perturbations: %d\n', length(ratios));
    fprintf('  Range: %.1f to %.1f\n', min(ratios), max(ratios));
    fprintf('  Mean: %.1f\n', mean(ratios));
    fprintf('  Median: %.1f\n', median(ratios));
    fprintf('  Ratios > 100×: %d (%.1f%%)\n', sum(ratios > 100), 100*sum(ratios > 100)/length(ratios));
    fprintf('  Ratios > 1000×: %d (%.1f%%)\n', sum(ratios > 1000), 100*sum(ratios > 1000)/length(ratios));
end
