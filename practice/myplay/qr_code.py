import qrcode

img = qrcode.make('http://127.0.0.1/')

img.save("./test.png")
