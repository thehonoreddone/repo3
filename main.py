from rembg import remove      #resmi indir kopyala python projectse yapıştır.

input_path="image.jpg"
output_path="output.png"

with open(input_path, 'rb') as image:   # rb readbinary
    with open(output_path, 'wb') as o:     #wb write binary
        inputfile=image.read() # image dosyayı okur
        outputfile=remove(inputfile)   # remove görüntü işleme ile arka planı silen fonks
        o.write(outputfile)    #actıgı dosyaya yazar