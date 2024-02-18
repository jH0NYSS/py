import qrcode

data = 'slapo' 

img = qrcode.make(data)

img.save('C:/Users/Jhony/Desktop/py/qrcode/myqrcode.png')    