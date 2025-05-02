import segno

link = input("Link: ")
qrcode = segno.make_qr(link)

qrcode.save("qrcode.png", scale=5)