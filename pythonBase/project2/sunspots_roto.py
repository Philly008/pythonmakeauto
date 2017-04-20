'''
Created on 2017年1月9日

@author: admin
'''
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
    # Year Month Predicted High Low
    (2007, 8, 107.5, 114.2, 98.2),
    (2007, 9, 106.3, 111.2, 106.2),
    (2007, 10, 105.2, 112.2, 107.2),
    (2007, 11, 111.2, 99.2, 105.2),
    (2007, 12, 111.2, 98.2, 104.2),
    (2008, 1, 99.6, 99.6, 123),
    (2008, 2, 98, 99.3, 107.5),
    (2008, 3, 100.6, 97.6, 109.6),
    (2008, 4, 94.5, 102.2, 108.5),
    (2008, 5, 91.2, 111.2, 108.6)
    ]

drawing = Drawing(200, 150)

pred = [row[2]-40 for row in data]
high = [row[3]-40 for row in data]
low = [row[4]-40 for row in data]
times = [200*((row[0] + row[1]/12.0) - 2007)-110 for row in data]

drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))
drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')



