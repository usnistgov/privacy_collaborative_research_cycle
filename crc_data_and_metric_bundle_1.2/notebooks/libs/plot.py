from typing import Optional, Dict, Tuple
from typing import List
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot
from matplotlib.ticker import FuncFormatter
# import mpimg module from matplot lib to load
# pca plot pngs
import matplotlib.image as mpimg
import math

from libs.color import get_colors


def bar(data: pd.DataFrame, height_column: str, color_by: str, color_map: Dict,
        y_err_column: Optional[str] = None,
        x_axis_size: Optional[int] = None, 
        y_axis_size: Optional[int] = None,
        y_axis_range: Optional[Tuple[int, int]] = None,
        hide_x_ticks: bool = True,
        title: str = "",
        figsize: Tuple[int, int] = (8, 5)):
    """
    Wrapper for matplotlib bar plot but with limited functionality.
    This function makes it easy to plot counts from any dataset available
    in the crc data and metric bundle.

    data: pd.DataFrame - the data to plot
    height_column: str - the column to plot the height of the bar
    color_by: str - name of the column used to distinguish the bars
    color_map: Dict - a dictionary mapping the values in the color_by column to colors
    y_err_column: Optional[str] - mame of the column to use for error bars
    x_axis_size: Optional[int] - number of ticks on x axis. If ticks are more than the
        number of bars then this helps in moving all bars to the left and avoids overlapping
        with the legend.
    y_axis_size: Optional[int] - mumber of ticks on y axis. If ticks are more than the
        number of bars then this helps squeezing the bar heights to avoid overlapping
        with the legend.
    y_axis_range: Optional[Tuple[int, int]] - range of values for y axis ticks.
    title: str - Title of the plot
    figsize: Tuple[int, int] - size of the matplotlib figure
    """

    # Create a matplotlib figure and axes objects
    fig, ax = plt.subplots(figsize=figsize)

    # Sort data by color_by column and then by height_column
    # and then reset the index
    data = data.sort_values(by=[color_by, height_column])
    data = data.reset_index(drop=True)

    # For each value in the color_by column, plot a bar
    for val in data[color_by].unique():
        mask = data[color_by] == val
        df = data[mask]
        bar_pos = df.index.tolist()
        # If error column is provided, plot the bar with error bars
        if y_err_column is not None and y_err_column in df.columns:
            ax.bar(x=bar_pos, height=df[height_column], color=color_map[val], yerr=df[y_err_column], label=val)
        else:
            ax.bar(x=bar_pos, height=df[height_column], color=color_map[val], label=val)

    # Set x axis ticks if provided
    if x_axis_size is not None:
        ax.set_xticks(range(x_axis_size))

    # Set y axis ticks if provided
    if y_axis_range is not None:
        ax.set_ylim(y_axis_range)

    # Set y axis label
    ax.set_ylabel(height_column)
    # Set positions of bars on x axis
    bar_positions = data.index.tolist()
    # Set x axis ticks
    ax.set_xticks(bar_positions)
    
    if hide_x_ticks:
        ax.xaxis.set_ticklabels([])
        
        
    # Enable legend for the plot
    ax.legend(title=color_by)
    ax.set_title(title)
    plt.show()


def scatter(data: pd.DataFrame,
            x: str,
            y: str,
            color_by: Optional[str] = None,
            color_map: Optional[Dict] = None,
            fit_curve: bool = False,
            title: str = "",
            figsize: Optional[Tuple[int, int]] = (10, 5)):
    """
    Wrapper for matplotlib scatter plot but with limited functionality.
    This function makes it easy to plot relation between two metrics
    from any dataset available in the crc data and metric bundle.

    data: pd.DataFrame - the data to plot
    x: str - name of the column to plot on x axis.
    y: str - name of the column to plot on y axis.
    color_by: Optional[str] - name of the column used to distinguish the points
    color_map: Optional[Dict] - a dictionary mapping the values in the color_by column to colors
    title: str - title of the plot
    figsize: Optional[Tuple[int, int]] - size of the matplotlib figure
    """
    # Create a matplotlib figure and axes objects
    fig, ax = plt.subplots(figsize=figsize)
    # If color_by column is not provided, plot all points with same color
    if color_by is None:
        ax.scatter(data[x], data[y])
    else:
        # Get unique values in color_by column
        u_color_by = data[color_by].unique().tolist()
        # Get colors for each unique value in color_by column
        colors = get_colors(len(u_color_by))
        # For each unique value in color_by column, plot the points for that value
        for u_val in u_color_by:
            d = data[data[color_by] == u_val]
            # If color_map is provided, use it to get color for each point
            if color_map is not None:
                color_data = d[color_by].apply(lambda x: color_map[x]).tolist()
            else:
                color_data = d[color_by].apply(lambda x: colors[u_color_by.index(x)]).tolist()
            # Plot the points
            ax.scatter(d[x], d[y], c=color_data, label=f'{u_val}')
            # Enable legend for the plot
            legend = ax.legend(bbox_to_anchor=(1, 1))
            # Set the legend background to transparent
            legend.get_frame().set_alpha(None)
            # Set the legend background color to white
            legend.get_frame().set_facecolor((1, 1, 1, 0.6))

    if fit_curve == True:
        # define the true objective function
        # def objective(x_val, a, b, c):
        #     return a * x_val + b * x_val ** 2 + c
        def objective(x_val, a, b, c, d):
            return a * x_val + b * x_val ** 2 + c * x_val ** 3 + d

        # choose the input and output variables
        x_vals, y_vals = data.loc[:, x].values, data.loc[:, y].values
        # curve fit
        popt, _ = curve_fit(objective, x_vals, y_vals)
        # summarize the parameter values
        a, b, c, d = popt

        # define a sequence of inputs between the smallest and largest known inputs
        x_line = np.arange(min(x_vals), max(x_vals), 1)
        # calculate the output for the range
        y_line = objective(x_line, a, b, c, d)
        # create a line plot for the mapping function
        ax.plot(x_line, y_line, '--', color='black', linewidth=3)
        # pyplot.show()
    # Set x and y axis labels
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)
    ax.legend(title=color_by)
    plt.show()


def draw_pca_images(died_path: str, target_path: str, name: str):
    """
    This function draws two pca plots side by side.
    The first plot is the pca plot of the target dataset
    and the second plot is the pca plot of the deid dataset.
    deid_path: str - path to the deid pca plot image
    target_path: str - path to the target pca plot image
    name: str - label for the dataset
    return: None
    """
    # Load deid pca plot image into deid_plot variable
    deid_plot = mpimg.imread(died_path)

    # Load target pca plot image into target_plot variable
    target_plot = mpimg.imread(target_path)

    # create matplotlib figure and axes for plotting
    # deid pca plot image
    # Provide nrows as 1 and ncols as 2 to show
    # target and deid plots on same row and in
    # two different columns of a figure
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))


    # Get axes at column 0 of the figure. We plot
    # target dataset on left side of the figure.
    ax_target = ax[0]

    # Get axes at column 1 of the figure. We plot
    # deid dataset on right side of the figure.
    ax_deid = ax[1]

    # Turn off the default x and y axis of the plot
    # since the image we are loading already got
    # both axis
    ax_target.set_axis_off()
    ax_deid.set_axis_off()

    # Show the pca plot image using matplotlib axes
    # We are directing output of imshow to ax_img variable
    # to avoid printing axes object in the output.
    ax_target_img = ax_target.imshow(target_plot)
    ax_deid_img = ax_deid.imshow(deid_plot)
    fig_txt = fig.suptitle(f'{name} \n '
                           f'For both target and deid data, people with '
                           f'MSP feature value \'N\' are highlighted in Red')


def draw_single_image(image_path: str, name: str):
    # Load deid pca plot image into deid_plot variable
    plot_img = mpimg.imread(image_path)

    # create matplotlib figure and axes for plotting
    # plot image
    fig, ax = plt.subplots(figsize=(14, 10))

    # Turn off the default x and y axis of the plot

    ax.set_axis_off()
    # Show the pca plot image using matplotlib axes
    # We are directing output of imshow to ax variable
    # to avoid printing axes object in the output.
    ax_img = ax.imshow(plot_img, aspect='equal')
    ax_title = ax.set_title(name)


def correlation_plot(correlations_data: List):
    """
    Plots correlation data of each deid dataset in correlations_data list.
    :param correlations_data: List of tuples. Each tuple contains a label and a pandas dataframe.
    :return: None
    """
    n_reports = len(correlations_data)
    n_rows = math.ceil(n_reports / 3)
    n_cols = 3
    n_features = len(correlations_data[0][1].columns)
    if n_features < 12:
        cell_size = 0.45
    else:
        cell_size = 0.23
    fig_width = cell_size * n_features * n_cols
    fig_height = cell_size * n_features * n_rows
    fig, ax = plt.subplots(n_rows, n_cols + 1, figsize=(fig_width + 10, fig_height + 10))
    # correlations_data = sorted(correlations_data, key=lambda x: x[0])
    v_max = 0.15
    ax_c = None
    for i, (v_label, corr_df) in enumerate(correlations_data):
        r_i = i // n_cols
        r_j = i % n_cols
        if n_rows > 1:
            ax_i = ax[r_i, r_j]
        else:
            ax_i = ax[i]

        corr_df = corr_df.iloc[::-1]
        corr_df = corr_df.round(2)
        ax_c = ax_i.pcolor(corr_df, cmap='Blues', vmin=0, vmax=v_max)
        if r_j > 0:
            ax_i.set_yticks([float(t) + 0.5 for t in range(corr_df.shape[0])],
                            [''] * len(corr_df.index))
        if r_j == 0:
            ax_i.set_yticks([float(t) + 0.5 for t in range(corr_df.shape[0])],
                            corr_df.index)

        ax_i.set_xticks([float(t) + 0.5 for t in range(corr_df.shape[1])],
                        corr_df.columns, rotation=90)
        ax_i.tick_params(axis='both', which='major', labelsize=10)
        ax_i.set_title(v_label, fontdict={'fontsize': 10, 'fontweight': 'bold'})

    for i in range(n_rows):
        j = n_cols if n_rows > 1 else -1
        if i == n_rows - 1:
            temp_j = n_reports % n_cols
            j = temp_j if temp_j > 0 else j
        if n_rows > 1:
            ax_i = ax[i, j]
        else:
            ax_i = ax[j]
        fmt = lambda x, pos: '{:.2}'.format(x)

        fig.colorbar(ax_c, ax=ax_i, orientation='vertical', pad=.05, fraction=1, format=FuncFormatter(fmt))
        ax_i.axis('off')
        if j > -1 and j != n_cols:
            j = n_cols
            if n_rows > 1:
                ax_i = ax[i, j]
            else:
                ax_i = ax[j]
            cb = fig.colorbar(ax_c, ax=ax_i, orientation='vertical', pad=.05, fraction=1)
            cb.remove()
            ax_i.axis('off')

    for j in range(n_cols):
        idx = n_reports + n_rows
        last_j = idx % (n_cols + 1)

        if 0 < last_j <= j:
            if n_rows > 1:
                ax[n_rows - 1, j].axis('off')
            else:
                ax[j].axis('off')
    fig.subplots_adjust(wspace=0.4, hspace=0.5)
    # fig.tight_layout()
    plt.show()
    # plt.savefig(plot_save_path, bbox_inches='tight')
    # plt.close()
