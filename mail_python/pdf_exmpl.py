#!/usr/bin/env python
from reportlab.platypus import SimpleDocTemplate #templates for showing reports
from reportlab.platypus import Paragraph, Spacer, Table ,Image #for Flowables chunks for creting Paragrpahs, Spacer, Tables and Images
from reportlab.lib.styles import getSampleStyleSheet #for style of the sheets and tables
from reportlab.lib import colors #for colors of the table
from reportlab.graphics.shapes import Drawing #for shapes of ghraph
from reportlab.graphics.charts.piecharts import Pie #for Pie charts shape
from reportlab.lib.units import inch, cm #for unitws in the charts and tables




fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

'''created a list of Fruits that we gonna use for our pdf doc'''

report = SimpleDocTemplate('./pdf_file/report.pdf')

'''we are using SimpleDocTemplate to create the pdf file in from us definiert directory'''

styles = getSampleStyleSheet()

''' we import Flowables- chunks of document that reportlib can arrange to get the complet document we can import
diffrent classes like Paragraph, Spacer, Table Image'''

report_title = Paragraph('A complete inventory of my fruits', styles['h1'])

'''we use Paragraph to make a Title with "h1" as formating style'''

report.build([report_title]) 

'''with .build method we build the pdf file'''

table_data = []
for k, v in fruit.items():
  table_data.append([k,v])

'''to create a Table data we need to create "list-of-lists" or "two-dimensional array" 
we do that with iterating trough dict with for loop creating two values
and then append them to the list. We get list with two values '''
#print(table_data)
#report_table = Table(data=table_data)
#report.build([report_title, report_table])
''' commentet because we use them down again'''
table_style=[('GRID', (0,0), (-1,-1), 1, colors.red)]

''' we define the table_style to be "GRID" and alligment and color of the 
table on the sheeet'''

report_table= Table(data=table_data, style=table_style, hAlign="RIGHT")

''' here is defined how the Table will look loke what content will hacve, 
Style and allighment to the paper sheet LEFT or RIGHT'''

report.build([report_title, report_table])

''' the report pdf is build with the .build method'''

report_pie = Pie(width=3*inch, height=3*inch)

'''here is defined dimensions of the PIE Chart'''


report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
  report_pie.data.append(fruit[fruit_name])
  report_pie.labels.append(fruit_name)

'''we iterate trough dict and take the value from the key "fruit_name" value pair
and for label takes the key '''
print(report_pie.data)
print(report_pie.labels)
report_chart = Drawing()
report_chart.add(report_pie)
report.build([report_title, report_table, report_chart])
'''here are created Drawing and the added report_pie as picture
and at the end all are .build together'''
