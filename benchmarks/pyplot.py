# https://github.com/richard-roberts/PyPlot

import os 
 
import matplotlib 
import matplotlib.patches as patches 
import matplotlib.pyplot as plt 
from matplotlib.ticker import MultipleLocator 
 
from colors import * 
 
 
class Utility: 
    tiny_float = 0.001 
 
    @staticmethod 
    def x(point): 
        return point[0] 
 
    @staticmethod 
    def y(point): 
        return point[1] 
 
    @staticmethod 
    def z(point): 
        return point[2] 
 
    @staticmethod 
    def xs(points): 
        return [Utility.x(p) for p in points] 
 
    @staticmethod 
    def ys(points): 
        return [Utility.y(p) for p in points] 
 
    @staticmethod 
    def zs(points): 
        return [Utility.z(p) for p in points] 
 
    @staticmethod 
    def generate_numerals_between(start, finish, increment, excluded_range): 
        vs = [] 
        v = start 
        while v < finish: 
            if v < (excluded_range[0] - Utility.tiny_float) or (excluded_range[1] + Utility.tiny_float) < v: 
                vs.append(v) 
            v += increment 
        return vs 
 
    @staticmethod 
    def stringify_numbers(vs): 
        return ["%2.1f" % v for v in vs] 
 
 
class Axes: 
    x = "x" 
    y = "y" 
    z = "z" 
 
    right = "right" 
    left = "left" 
    top = "top" 
    bottom = "bottom" 
 
    # ---------------------------------------------------------------------------------------------------------------- # 
    # Basic 
    # 
    # 
    # ---------------------------------------------------------------------------------------------------------------- # 
 
    @staticmethod 
    def set_axis_off(): 
        plt.axis('off') 
 
    @staticmethod 
    def set_font_size(v): 
        matplotlib.rcParams.update({'font.size': v}) 
 
    @staticmethod 
    def set_title(name): 
        plt.title(name) 
 
    @staticmethod 
    def set_axes_color(color): 
        c = color.get_hex() 
 
        def set_spine_colors(): 
            Figure.ax.spines['bottom'].set_color(c) 
            Figure.ax.spines['top'].set_color(c) 
            Figure.ax.spines['right'].set_color(c) 
            Figure.ax.spines['left'].set_color(c) 
 
        def set_tick_colors(): 
            Figure.ax.tick_params(axis='x', colors=c) 
            Figure.ax.tick_params(axis='y', colors=c) 
            Figure.ax.tick_params(axis='z', colors=c) 
 
        def set_label_colors(): 
            Figure.ax.yaxis.label.set_color(c) 
            Figure.ax.xaxis.label.set_color(c) 
 
        set_spine_colors() 
        set_tick_colors() 
        set_label_colors() 
 
    # ---------------------------------------------------------------------------------------------------------------- # 
    # Label configuration 
    # 
    # 
    # ---------------------------------------------------------------------------------------------------------------- # 
 
    @staticmethod 
    def set_label(axis, label): 
        if axis == Axes.x: 
            Figure.ax.set_xlabel(label) 
        elif axis == Axes.y: 
            Figure.ax.set_ylabel(label) 
        elif axis == Axes.z: 
            Figure.ax.set_zlabel(label) 
 
    @staticmethod 
    def set_x_label(label): 
        Axes.set_label(Axes.x, label) 
 
    @staticmethod 
    def set_y_label(label): 
        Axes.set_label(Axes.y, label) 
 
    @staticmethod 
    def set_z_label(label): 
        Axes.set_label(Axes.z, label) 
 
    # ---------------------------------------------------------------------------------------------------------------- # 
    # Range configuration 
    # 
    # 
    # ---------------------------------------------------------------------------------------------------------------- # 
 
    @staticmethod 
    def set_range(axis, a, b): 
        if axis == Axes.x: 
            Figure.ax.set_xlim([a, b]) 
        elif axis == Axes.y: 
            Figure.ax.set_ylim([a, b]) 
        elif axis == Axes.z: 
            Figure.ax.set_zlim([a, b]) 
 
    @staticmethod 
    def set_x_range(a, b): 
        Axes.set_range(Axes.x, a, b) 
 
    @staticmethod 
    def set_y_range(a, b): 
        Axes.set_range(Axes.y, a, b) 
 
    @staticmethod 
    def set_z_range(a, b): 
        Axes.set_range(Axes.z, a, b) 
 
    # ---------------------------------------------------------------------------------------------------------------- # 
    # Ticks configuration 
    # 
    # 
    # ---------------------------------------------------------------------------------------------------------------- # 
 
    @staticmethod 
    def set_major_ticks_x(major): 
        Figure.ax.xaxis.set_major_locator(MultipleLocator(major)) 
 
    @staticmethod 
    def set_major_ticks_y(major): 
        Figure.ax.yaxis.set_major_locator(MultipleLocator(major)) 
 
    @staticmethod 
    def set_major_ticks_z(major): 
        Figure.ax.zaxis.set_major_locator(MultipleLocator(major)) 
 
    @staticmethod 
    def remove_ticks(axis): 
        if axis == Axes.x: 
            plt.xticks([]) 
        elif axis == Axes.y: 
            plt.yticks([]) 
        elif axis == Axes.z: 
            raise ValueError("Matplotlib does not yet implement an accessor for the z axis's ticks") 
 
    @staticmethod 
    def remove_ticks_x(): 
        Axes.remove_ticks(Axes.x) 
 
    @staticmethod 
    def remove_ticks_y(): 
        Axes.remove_ticks(Axes.y) 
 
    @staticmethod 
    def remove_ticks_z(): 
        Axes.remove_ticks(Axes.z) 
 
    # ---------------------------------------------------------------------------------------------------------------- # 
    # Axes configuration 
    # 
    # 
    # ---------------------------------------------------------------------------------------------------------------- # 
 
    @staticmethod 
    def turn_off(list_of_directions): 
        for axis in list_of_directions: 
            Figure.ax.spines[axis].set_color('none') 
 
    @staticmethod 
    def _center(list_of_directions): 
        for axis in list_of_directions: 
            Figure.ax.spines[axis].set_position('center') 
 
    @staticmethod 
    def move_axis_to_center(): 
        Axes.turn_off([Axes.right, Axes.top]) 
        Axes._center([Axes.left, Axes.bottom]) 
        Figure.ax.xaxis.set_ticks_position('bottom') 
        Figure.ax.yaxis.set_ticks_position('left') 
 
    @staticmethod 
    def left_and_bottom_axes_only(): 
        Axes.turn_off([Axes.right, Axes.top]) 
 
    @staticmethod 
    def bottom_axis_only(): 
        Axes.turn_off([Axes.right, Axes.left, Axes.top]) 
        Axes.remove_ticks_y() 
 
    @staticmethod 
    def set_numbers(axis, start, finish, increment, excluded_range=(0, 0)): 
        xs = Utility.generate_numerals_between(start, finish, increment, excluded_range) 
        labels = Utility.stringify_numbers(xs) 
 
        if axis == Axes.x: 
            plt.xticks(xs, labels, rotation='horizontal') 
        elif axis == Axes.y: 
            plt.yticks(xs, labels, rotation='horizontal') 
        elif axis == Axes.z: 
            raise ValueError("Matplotlib does not yet implement an accessor for the z axis's ticks") 
 
    @staticmethod 
    def set_x_numbers(start, finish, increment, excluded_range=(0, 0)): 
        Axes.set_numbers(Axes.x, start, finish, increment, excluded_range=excluded_range) 
 
    @staticmethod 
    def set_y_numbers(start, finish, increment, excluded_range=(0, 0)): 
        Axes.set_numbers(Axes.y, start, finish, increment, excluded_range=excluded_range) 
 
    @staticmethod 
    def set_z_numbers(start, finish, increment, excluded_range=(0, 0)): 
        Axes.set_numbers(Axes.z, start, finish, increment, excluded_range=excluded_range) 
 
    @staticmethod 
    def grid(color, style='-'): 
        Figure.ax.grid(color=color.get_hex(), linestyle=style, linewidth=1) 
 
    @staticmethod 
    def add_legend(names, colors): 
        handles = [] 
        for (name, color) in zip(names, colors): 
            patch = patches.Patch(color=color.get_hex(), label=name) 
            handles.append(patch) 
        plt.legend(handles=handles) 
 
 
class Draw: 
    @staticmethod 
    def points(points, size=5, color=GrayDark(), marker="o", zorder=1): 
        plt.scatter(Utility.xs(points), Utility.ys(points), 
                    s=size, color=color.get_hex(), marker=marker, 
                    zorder=zorder) 
 
    @staticmethod 
    def points_3d(points, size=5, color=GrayDark(), marker="."): 
        Figure.ax.scatter(Utility.xs(points), Utility.ys(points), Utility.zs(points), 
                          s=size, color=color.get_hex(), marker=marker) 
 
    @staticmethod 
    def lines(points, color=GrayDark(), linestyle="-", linewidth=1, marker=".", markersize=0.0, zorder=1): 
        plt.plot(Utility.xs(points), Utility.ys(points), 
                 color=color.get_hex(), linestyle=linestyle, linewidth=linewidth, 
                 marker=marker, markersize=markersize, zorder=zorder) 
 
    @staticmethod 
    def lines_3d(points, color=GrayDark(), linestyle="-", linewidth=1, marker=".", markersize=0.0, zorder=1): 
        Figure.ax.plot(Utility.xs(points), Utility.ys(points), Utility.zs(points), 
                       color=color.get_hex(), linestyle=linestyle, linewidth=linewidth, 
                       marker=marker, markersize=markersize, zorder=zorder) 
 
    @staticmethod 
    def wedge(point, radius, start, finish, color=GrayDark()): 
        shape = patches.Wedge(point, radius, start, finish, facecolor=color.get_hex()) 
        Figure.ax.add_patch(shape) 
 
    @staticmethod 
    def box(a, b, color=GrayDark()): 
        w = Utility.x(b) - Utility.x(a) 
        h = Utility.y(b) - Utility.y(a) 
        shape = patches.Rectangle(a, w, h, facecolor=color.get_hex()) 
        Figure.ax.add_patch(shape) 
 
    @staticmethod 
    def boxes(pairs, color=GrayDark()): 
        for (a, b) in pairs: 
            Draw.box(a, b, color=color) 
 
    @staticmethod 
    def annotate(point, label, color=GrayDark(), offset=(0.1, 0.1)): 
        text = r'$' + label + '$' 
        plt.text(Utility.x(point) + Utility.x(offset), Utility.y(point) + Utility.y(offset), 
                 text, color=color.get_hex()) 
 
    @staticmethod 
    def annotations(points, labels, color=GrayDark(), offset=(0.1, 0.1)): 
        for (point, label) in zip(points, labels): 
            Draw.annotate(point, label, color=color, offset=offset) 
 
 
class Figure: 
    fig = None 
    ax = None 
    dpi = 100 
 
    @staticmethod 
    def set_dpi(dpi): 
        Figure.dpi = dpi 
 
    @staticmethod 
    def new(resolution_x, resolution_y): 
        n_pixels_x = resolution_x / Figure.dpi 
        n_pixels_y = resolution_y / Figure.dpi 
        Figure.fig = plt.figure(figsize=(n_pixels_x, n_pixels_y), dpi=Figure.dpi) 
        Figure.ax = plt.gca() 
 
    @staticmethod 
    def convert_to_three_dimensional(): 
        Figure.ax = plt.gca(projection='3d') 
 
    @staticmethod 
    def show(*_): 
        plt.show() 
 
    @staticmethod 
    def save(directory, filename, extension="png", transparent=True): 
        potentially_relative_filepath = "%s/%s.%s" % (directory, filename, extension) 
        absolute_filepath = os.path.expanduser(potentially_relative_filepath) 
        plt.savefig(absolute_filepath, dpi=Figure.dpi, bbox_inches='tight', transparent=transparent)
