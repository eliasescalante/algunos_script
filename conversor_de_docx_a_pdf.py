from docx2pdf import convert

# Ruta del archivo de Word a convertir
print(" Conversor de doc a pdf...")
input_docx_file = input("ingresa la ruta del archivo docx a convertir : ")

# Convierte el archivo de Word a PDF
convert(input_docx_file)