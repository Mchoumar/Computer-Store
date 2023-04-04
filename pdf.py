"""
This script creates pdf file.
"""
from fpdf import FPDF

# Initiate creation of pdf
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# Makes a cell for the text
pdf.set_font(family="Times", size=16, style="B")
pdf.cell(w=30, h=10, txt="adadaw", ln=1)

# Outputs the data into the pdf file
pdf.output("test.pdf")
