import os, sys 
 
from pyplot import * 

colors = [
    RedDark(), 
    BlueDark(),
    GreenDark(),
    YellowDark()
]

def get_csv_filenames_in_directory(directory):
    filenames = []
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            filename = os.path.join(directory, file)
            filenames.append(filename)
    return filenames

def read_csv(filepath): 
    filename = filepath
    names = []
    times = []

    # Extract the data for each benchmark
    current_name = ""
    current_times = []
    with open(filename) as f: 
        for line in f.readlines():
            line = line.strip()

            if line.startswith("benchmark"):

                # Cache the existing result if not the first time we hit this loop
                if len(current_times) > 0:
                    names.append(current_name)
                    times.append(current_times)
                    current_times = []

                current_name = line

            else:
                current_times.append(int(line) / 1000)

    # Add the last result
    names.append(current_name)
    times.append(current_times)
    return zip(names, times)
 
def render_suite_at_scale(directory, scale):

    # Start the graph
    Figure.new(2400, 600) 
    Axes.set_x_label("Number of Executions") 
    Axes.set_y_label("Execution Time (milliseconds)") 
    Axes.set_title("Multiple Comparison") 
    Axes.set_axes_color(GrayMid()) 
    Axes.grid(GrayLight(), style='--') 

    # Draw the execution times for each benchmark
    benchmark_names = []
    benchmark_colors = []
    index = 0

    min_x, max_x = float('inf'), -float('inf')
    min_y, max_y = float('inf'), -float('inf')
    for filename in get_csv_filenames_in_directory(directory):

        for (name, times) in read_csv(filename):
            color = colors[index]
            benchmark_names.append("%s-%s" % (os.path.basename(filename).split(".")[0], name))
            benchmark_colors.append(color)

            ys = times
            xs = [i + 1 for i in range(len(ys))] 
            ps = [[x, y] for (x, y) in zip(xs, ys)] 
            Draw.lines(ps, color=color) 

            if min(xs) < min_x: min_x = min(xs)
            if max(xs) > max_x: max_x = max(xs)
            if min(ys) < min_y: min_y = min(ys)
            if max(ys) > max_y: max_y = max(ys)


            index += 1

    # Set the legend
    Axes.add_legend(benchmark_names, benchmark_colors)

    # Set bounds for x-axis
    Axes.set_x_range(min_x, max_x) 

    # set bounds for y-axis
    bot = min_y
    top = min_y + (max_y - min_y) * (scale)
    Axes.set_y_range(bot, top) 
    
    # Save
    filename = "resultx%2.1f" % (1 + scale)
    Figure.save(directory, filename, transparent=False) 


for i in range(5):
    directory = sys.argv[1]
    scale = (i + 1) / 10.0
    render_suite_at_scale(directory, scale) 
