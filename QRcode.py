import png
from pyqrcode import QRCode,pyqrcode


def QRCode_maker():
    QRstr="85483595959"
    url= pyqrcode.create(QRstr)
    url.png("../python/qr.png",scale=8)

QRCode_maker()
