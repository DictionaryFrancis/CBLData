from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from datetime import date
from reportlab.lib import colors

def create_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)

    image_path = "Helio-picture.png"  # Replace with the actual path to your image
    x_position = 255
    y_position = 655
    image_width = 100
    image_height = 100
    c.drawImage(image_path, x_position, y_position, width=image_width, height=image_height)

    array_match_home = ["1", "2", "3"]  # Replace with your data
    array_match_visitor = ["4", "5", "6"]  # Replace with your data
    array_team_home = ["TeamA", "TeamB", "TeamC"]  # Replace with your data
    array_team_visitor = ["TeamX", "TeamY", "TeamZ"]  # Replace with your data

    # Create a table style
    style = [
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]

    data = [['', 'Team A', 'X', 'Team B']]

    for match_home, match_visitor, team_home, team_visitor in zip(array_match_home, array_match_visitor, array_team_home, array_team_visitor):
        data.append(['', team_home, match_home, team_visitor])

    # Create the table
    table = Table(data, colWidths=[20, 100, 20, 100])

    # Apply the table style
    table.setStyle(TableStyle(style))

    # Draw the table on the canvas
    table.wrapOn(c, 200, 400)
    table.drawOn(c, 100, 500)

    c.save()

pdf_file = f"output_{date.today()}.pdf"

create_pdf(pdf_file)
print(f'PDF created: {pdf_file}')
