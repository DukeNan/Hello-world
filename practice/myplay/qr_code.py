import qrcode

img = qrcode.make('http://112.74.57.236/')

img.save("./test.png")