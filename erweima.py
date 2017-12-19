import qrcode  # 导入模块

def readcsv(filename):
    data = []
    with open(filename,encoding="utf8") as f:
        for i in f:
            hang = i.splitlines()[0].split(',')
            data.append(hang)
    return data
data = readcsv('data.csv')

for index,item in enumerate(data):
    print("正在生成第%s个二维码..." % (index+1))
    print("     二维码标题为——%s" % item[0])
    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(item[1])
    qr.make(fit=True)
    img = qr.make_image()
    img.save("./images/"+item[0]+".jpg")
