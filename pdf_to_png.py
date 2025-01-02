# import module
from pdf2image import convert_from_path

name_file = 'file'
path = f'files\{name_file}.pdf'
# Store Pdf with convert_from_path function
images = convert_from_path(path, poppler_path = r"C:\Users\Username\path\to\venv\poppler-version\Library\bin" )

for i in range(len(images)):
  
      # Save pages as images in the pdf
    name_file = path.split("\\")[1]
    images[i].save(f'image_{name_file}'+ str(i) +'.jpg', 'JPEG')