

from pdf2docs import Converter  #pdf indirip masaustunden kopyala pythonprojectse yapıştır.


pdf_path="sample.pdf"
docx_path="sample.docx"

cv=Converter(pdf_file=pdf_path)    #convert=dönüştürücü
cv.convert(docx_filename=docx_path)
cv.close()
