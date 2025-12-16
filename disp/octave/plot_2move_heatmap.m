% Plot 2-Move Sequence Heat Map
%
% Creates a 12×12 heat map showing Lyapunov exponents for all
% two-move combinations. Reveals which move pairs are most chaotic.
%
% Requires: All 144 2-move sequences to be analyzed first
%           (run obsv/scripts/collect_2move_heatmap.py)

function plot_2move_heatmap(data_file, output_file)
    % Default paths
    if nargin < 1
        data_file = '../obsv/logs/lyapunov_data.csv';
    end
    if nargin < 2
        output_file = 'figures/2move_heatmap.png';
    end

    % All 12 moves in order
    moves = {'FR', 'FL', 'FU', 'FO', 'RF', 'RO', 'UR', 'UF', 'UO', 'UL', 'OR', 'OL'};
    n_moves = length(moves);

    % Read CSV data
    data = read_lyapunov_csv(data_file);

    % Initialize matrix with NaN (missing data)
    heatmap_data = nan(n_moves, n_moves);

    % Create move index map
    move_idx = containers.Map(moves, 1:n_moves);

    % Fill matrix with 2-move sequences
    for i = 1:length(data.sequence)
        % Parse sequence
        seq_str = data.sequence{i};
        parts = strsplit(seq_str, ' → ');

        % Only process 2-move sequences
        if length(parts) == 2
            move1 = strtrim(parts{1});
            move2 = strtrim(parts{2});

            % Check if both moves are in our list
            if isKey(move_idx, move1) && isKey(move_idx, move2)
                row = move_idx(move1);
                col = move_idx(move2);
                heatmap_data(row, col) = data.lyapunov_exponent(i);
            end
        end
    end

    % Count how many are filled
    n_filled = sum(~isnan(heatmap_data(:)));
    n_total = n_moves * n_moves;

    if n_filled < n_total
        fprintf('Warning: Only %d/%d 2-move sequences available\n', n_filled, n_total);
        fprintf('Run: cd ../obsv && uv run python scripts/collect_2move_heatmap.py\n');
    end

    % Create figure
    figure('Position', [100, 100, 1000, 900]);

    % Plot heatmap
    imagesc(heatmap_data);
    colorbar;
    colormap('hot');  % Octave-compatible colormap

    % Set axis labels
    set(gca, 'XTick', 1:n_moves);
    set(gca, 'YTick', 1:n_moves);
    set(gca, 'XTickLabel', moves);
    set(gca, 'YTickLabel', moves);
    set(gca, 'FontSize', 11);

    % Rotate x labels
    xtickangle(45);

    % Labels and title
    xlabel('Second Move', 'FontSize', 14, 'FontWeight', 'bold');
    ylabel('First Move', 'FontSize', 14, 'FontWeight', 'bold');
    title(sprintf('2-Move Sequence Heat Map (%d/%d collected)', n_filled, n_total), ...
          'FontSize', 16, 'FontWeight', 'bold');

    % Add text annotations for values
    for row = 1:n_moves
        for col = 1:n_moves
            val = heatmap_data(row, col);
            if ~isnan(val)
                % Choose text color based on value
                if val > 3.0
                    text_color = 'w';
                else
                    text_color = 'k';
                end
                text(col, row, sprintf('%.1f', val), ...
                     'HorizontalAlignment', 'center', ...
                     'VerticalAlignment', 'middle', ...
                     'FontSize', 8, ...
                     'Color', text_color);
            end
        end
    end

    % Set color limits for better contrast
    caxis([0, max(6, max(heatmap_data(:)))]);

    % Save figure
    [output_dir, ~, ~] = fileparts(output_file);
    if ~exist(output_dir, 'dir')
        mkdir(output_dir);
    end

    print(output_file, '-dpng', '-r300');
    fprintf('Saved: %s\n', output_file);

    % Print statistics
    fprintf('\n2-Move Heat Map Statistics:\n');
    fprintf('  Sequences collected: %d/%d (%.1f%%)\n', n_filled, n_total, 100*n_filled/n_total);

    if n_filled > 0
        valid_data = heatmap_data(~isnan(heatmap_data));
        fprintf('  λ range: %.3f to %.3f\n', min(valid_data), max(valid_data));
        fprintf('  Mean λ: %.3f\n', mean(valid_data));

        % Find most chaotic pair
        [max_val, max_idx] = max(valid_data);
        [max_row, max_col] = ind2sub([n_moves, n_moves], ...
                                     find(heatmap_data == max_val, 1));
        fprintf('  Most chaotic: %s → %s (λ=%.3f)\n', ...
                moves{max_row}, moves{max_col}, max_val);
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