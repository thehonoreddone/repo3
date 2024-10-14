import pyqrcode

url=input("Enter your url for qrcode: ")
qr_code=pyqrcode.create(url)
qr_code.svg("qrcode.svg",scale=5)   #farklı uzantılarla eps png ile olur ismini verip scale verirsin.