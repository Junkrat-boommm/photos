import base64
f= open("1.png", 'rb')
ls_f=base64.b64encode(f.read())
f.close()
print(ls_f)