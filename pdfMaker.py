from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch

canvas = Canvas('test.pdf', pagesize=A4)

canvas.setFont('Times-Roman',18)
with open('BG.png') as B:
    for b in B:
        print(b)
canvas.drawString(1*inch, 10*inch, "This is a test string")
canvas.save()
