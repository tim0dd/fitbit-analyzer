from ast import In
import click
from fitbit_analyzer.load.load_sleep import load_sleep_data
from fitbit_analyzer.plot.plot_sleep import plot_sleep_data

@click.command()
@click.option('--in_path', prompt='Path to CSV file', help='Path to the sleep score CSV file.')
@click.option('--out_path', default=None, help='Path to output directory for the plots.')
@click.option('--cols', default='', help='Comma-separated list of columns to plot.')
def main(in_path: str, out_path: str, cols: str):
    """
    Generate plots for sleep data. Plots all columns by default or specified columns if provided.
    """
    data = load_sleep_data(in_path)

    if out_path:
        column_list = [c.strip() for c in cols.split(',')]
    else:
        column_list = list(data.columns)

    plot_sleep_data(data, column_list, out_path)
    click.echo(f"Plots saved in {out_path}")

if __name__ == '__main__':
    main()