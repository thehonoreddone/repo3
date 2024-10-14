from rembg import remove     

input_path="image.jpg"
output_path="output.png"
with open(input_path, 'rb') as image: 
    with open(output_path, 'wb') as o:     
        inputfile=image.read() 
        outputfile=remove(inputfile)   
        o.write(outputfile)    