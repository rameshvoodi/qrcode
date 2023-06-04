import qrcode

li_qrcode = qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_L,box_size=10,border=4)

strdata = str(input("enter url: "))

li_qrcode.add_data(strdata)

li_qrcode.make(fit=True)

img_qr = li_qrcode.make_image(fill_color = "cyan", back_color = "black")

img_qr.save("new.png")
