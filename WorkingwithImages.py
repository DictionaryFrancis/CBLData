from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

def add_image_to_pdf(pdf_path, image_path, x, y, width=None, height=None):
    # Create a PDF document
    pdf_canvas = canvas.Canvas(pdf_path, pagesize=letter)

    # Load the image using PIL
    image = Image.open(image_path)

    # Add the image to the PDF using drawImage method
    pdf_canvas.drawImage(image_path, x, y, width=width, height=height)

    # Save the PDF
    pdf_canvas.save()

# Example usage
pdf_path = "example.pdf"
image_path = "Helio-picture.png"
x_position = 255
y_position = 655
image_width = 100
image_height = 100

add_image_to_pdf(pdf_path, image_path, x_position, y_position, width=image_width, height=image_height)
