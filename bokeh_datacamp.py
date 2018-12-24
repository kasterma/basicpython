# Notes datacamp bokeh course

from bokeh.io import output_file, show
from bokeh.plotting import figure

# can do the tool selection in the creation of the figure
# also the place to configure axis labels
plot = figure(plot_width=600, plot_height=400, tools="pan, box_zoom", x_axis_label='a-axis', y_axis_label='y-axis')
# use standard datastructures for creating plots, but see below can also use ColumnDataSource which is custom
# made for this
plot.circle([1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 1, 2])
plot.x(x=[1, 2, 3], y=[6, 7, 8], size=20)
plot.annulus(x=[2, 3, 4], y=[5, 6, 7], inner_radius=0.1, outer_radius=0.5)


from bokeh.models import ColumnDataSource, CategoricalColorMapper

# example with the ColunnDataSource
source = ColumnDataSource(data={'aaa':  [1, 2, 3, 4], 'bbb': [1, 2, 1, 5]})
p2 = figure(plot_width=600, plot_height=400, tools="pan, box_zoom", x_axis_label='aaa-axis', y_axis_label='bbb-axis')
p2.circle('aaa', 'bbb', source=source)

output_file("circle.html")
show(p2)

# for using custom colors can use the CategoricalColorMapper
source = ColumnDataSource(data={'aaa':  [1, 2, 3, 4], 'bbb': [1, 2, 1, 5], 'ccc': ['11', '11', '13', '12']})
color_mapper = CategoricalColorMapper(factors=['11', '12', '13'],
                                      palette=['red', 'green', 'blue'])
p3 = figure(plot_width=600, plot_height=400, x_axis_label='aaa-axis', y_axis_label='bbb-axis')
p3.circle('aaa', 'bbb', source=source, color={'field': 'ccc', 'transform': color_mapper})

output_file("circle.html")
show(p3)