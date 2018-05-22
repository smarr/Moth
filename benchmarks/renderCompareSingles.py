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
    times = []
    with open(filepath) as f: 
        for line in f.readlines()[1:]:
            times.append(int(line) / 1000)
    return times
 
def render_suite_at_scale(directory, scale):

    # Start the graph
    Figure.new(2400, 600) 
    Axes.set_x_label("Number of Executions") 
    Axes.set_y_label("Execution Time (milliseconds)") 
    Axes.set_title(directory.split("/")[-1]) 
    Axes.set_axes_color(GrayMid()) 
    Axes.grid(GrayLight(), style='--') 

    # Draw the execution times for each benchmark
    benchmark_names = []
    benchmark_colors = []
    index = 0

    min_x, max_x = float('inf'), -float('inf')
    min_y, max_y = float('inf'), -float('inf')
    for index, filename in enumerate(get_csv_filenames_in_directory(directory)):
        times = read_csv(filename)
        color = colors[index]
        benchmark_names.append(os.path.basename(filename).split(".")[0])
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
    Axes.set_x_range(0, max_x) 

    # set bounds for y-axis
    if len(sys.argv) > 2:
        bot = int(sys.argv[2])
        top = int(sys.argv[3])
        Axes.set_y_range(bot, top)
    else:
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
