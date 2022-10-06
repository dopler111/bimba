
from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import QApplication,QFileDialog,QInputDialog,QLineEdit,QListWidget,QTextEdit,QButtonGroup,QHBoxLayout,QRadioButton,QGroupBox, QWidget, QPushButton, QLabel, QVBoxLayout
from random import *
from PIL import Image
from PyQt5.QtGui import QPixmap

class ImageProcessor():
    def __init__(self):
        self.Image = None
        self.filename = None
        self.Papka = "Modifed/"

    def loadImage(self,filename):
        self.filename = filename
        image_path = os.path.join(workdir,filename)
        self.image = Image.open(image_path) 

    def showImage(self,path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(),lb_image.height()
        pixmapimage = pixmapimage.scaled(w,h,Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
        
    def saveImage(self):
        path = os.path.join(workdir,self.Papka)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path,self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir,self.Papka,self.filename)
        self.showImage(image_path)

    def do_rite(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir,self.Papka,self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir,self.Papka,self.filename)
        self.showImage(image_path)

    





workdir = ''

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('doppler')
main_win.resize(700,500)
qlist = QListWidget()

lb_image = QLabel("картинка")
q1 = QPushButton("Папка")
q2 = QPushButton("лево")
q3 = QPushButton("право")
q4 = QPushButton("зеркало")
q5 = QPushButton("резкость")
q6 = QPushButton("ч/б")
l0 = QVBoxLayout()
l1 = QVBoxLayout()
l2 = QHBoxLayout()
l3 = QHBoxLayout()



l0.addWidget(q1) 
l0.addWidget(qlist) 

l2.addWidget(q2) 
l2.addWidget(q3) 
l2.addWidget(q4) 
l2.addWidget(q5) 
l2.addWidget(q6) 

l1.addWidget(lb_image,95)
l1.addLayout(l2)
l3.addLayout(l0,20)
l3.addLayout(l1,80)


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files,extensions):
    results = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                results.append(filename)
    return results

def showFilenamesList():
    extensions = ['jpg','jpeg','png','.gif','bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)
    qlist.clear()
    for filename in filenames:
        qlist.addItem(filename)

q1.clicked.connect(showFilenamesList)

workimage = ImageProcessor()
def showChosenImage():
    if qlist.currentRow()>=0:
        filename = qlist.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir,workimage.filename)
        workimage.showImage(image_path)
qlist.currentRowChanged.connect(showChosenImage)

q6.clicked.connect(workimage.do_bw)
q2.clicked.connect(workimage.do_rite)
q3.clicked.connect(workimage.do_left)

main_win.setLayout(l3)
main_win.show()
app.exec()

