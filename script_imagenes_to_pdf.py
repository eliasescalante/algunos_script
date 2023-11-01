import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib import pdfencrypt
from reportlab.pdfgen import canvas

# Ruta de la carpeta que contiene las imágenes de entrada
print(" este script solo convierte y une imagenes .jpg a pdf bajo el nombre imagenes.pdf...\n")
input_folder = input("ingresa la ruta de lacarpeta con imagenes a convertir: ")


# Nombre del archivo PDF de salida
output_pdf_ruta = "imagenes.pdf"

# Obtén la lista de archivos de la carpeta con extensión .jpg
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

# Crear un objeto PDF con ReportLab
c = canvas.Canvas(output_pdf_ruta, pagesize=letter)

# Recorre la lista de imágenes y agrega cada imagen al PDF
for image_file in image_files:
    # Ruta completa de la imagen de entrada
    input_image_path = os.path.join(input_folder, image_file)
    
    # Abre la imagen con PIL
    img = Image.open(input_image_path)
    
    # Obtiene el tamaño de la imagen en píxeles
    img_width, img_height = img.size
    
    # Calcula el factor de escala para ajustar la imagen al tamaño de la página
    scale_x = letter[0] / img_width
    scale_y = letter[1] / img_height
    scale = min(scale_x, scale_y)
    
    # Calcula las coordenadas para centrar la imagen en la página
    x_centered = (letter[0] - img_width * scale) / 2
    y_centered = (letter[1] - img_height * scale) / 2
    
    # Dibuja la imagen centrada y ajustada al tamaño de la página
    c.drawImage(input_image_path, x_centered, y_centered, width=img_width * scale, height=img_height * scale)
    
    # Agrega una nueva página al PDF
    c.showPage()

# Cierra el archivo PDF
c.save()

print(f"Se han convertido las imágenes en {output_pdf_ruta}")
