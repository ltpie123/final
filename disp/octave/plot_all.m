% Generate All Lyapunov Analysis Visualizations
%
% Master script that generates all publication-quality figures for
% the Lyapunov exponent analysis.
%
% Usage:
%   plot_all()                     % Use default data file
%   plot_all(data_file)            % Specify custom data file
%   plot_all(data_file, out_dir)   % Custom data and output directory
%
% Output:
%   All figures saved to figures/ directory (or specified out_dir)

function plot_all(data_file, output_dir)
    % Default paths
    if nargin < 1 || isempty(data_file)
        data_file = '../obsv/logs/lyapunov_data.csv';
    end
    if nargin < 2 || isempty(output_dir)
        output_dir = 'figures';
    end

    % Ensure output directory exists
    if ~exist(output_dir, 'dir')
        mkdir(output_dir);
        fprintf('Created output directory: %s\n', output_dir);
    end

    % Check if data file exists
    if ~exist(data_file, 'file')
        error(['Data file not found: %s\n\n' ...
               'Please run Lyapunov analysis first:\n' ...
               '  cd ../obsv\n' ...
               '  uv run python scripts/run_lyapunov.py\n'], data_file);
    end

    fprintf('\n========================================\n');
    fprintf('Generating Lyapunov Analysis Figures\n');
    fprintf('========================================\n');
    fprintf('Data file: %s\n', data_file);
    fprintf('Output directory: %s\n\n', output_dir);

    % Generate each plot
    plots = {
        'plot_lyapunov_vs_length', 'lyapunov_vs_length.png', ...
            'Lyapunov exponent vs sequence length';
        'plot_period_vs_lambda', 'period_vs_lambda.png', ...
            'Period vs Lyapunov exponent (log scale)';
        'plot_classification_pie', 'classification_pie.png', ...
            'Classification distribution pie chart';
        'plot_top_sequences', 'top_chaotic_sequences.png', ...
            'Top 10 most chaotic sequences';
        'plot_perturbation_histogram', 'perturbation_histogram.png', ...
            'Perturbation sensitivity distribution';
        'plot_divergence_correlation', 'divergence_correlation.png', ...
            'State space divergence vs Lyapunov correlation'
    };

    for i = 1:size(plots, 1)
        func_name = plots{i, 1};
        filename = plots{i, 2};
        description = plots{i, 3};

        fprintf('[%d/%d] %s...\n', i, size(plots, 1), description);

        output_file = fullfile(output_dir, filename);

        % Call the plotting function
        feval(func_name, data_file, output_file);

        fprintf('      Saved: %s\n\n', output_file);
    end

    fprintf('========================================\n');
    fprintf('All figures generated successfully!\n');
    fprintf('========================================\n\n');

    % Print summary
    fprintf('Generated files:\n');
    for i = 1:size(plots, 1)
        fprintf('  - %s\n', fullfile(output_dir, plots{i, 2}));
    end
    fprintf('\n');
end