# Notes datacamp bokeh course

from bokeh.io import output_file, show
from bokeh.plotting import figure

plot = figure(plot_width=600, plot_height=400, tools="pan, box_zoom", x_axis_label='a-axis', y_axis_label='y-axis')
plot.circle([1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 1, 2])
plot.x(x=[1, 2, 3], y=[6, 7, 8], size=20)
plot.annulus(x=[2, 3, 4], y=[5, 6, 7], inner_radius=0.1, outer_radius=0.5)
output_file("circle.html")
show(plot)
