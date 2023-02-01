from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QPlainTextEdit, QRadioButton, QMessageBox
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont
import base64
import sys

ERROR_MSG = "not a valid base64 string :("
ALT_KEY = 16777251

mainFontClasses = [QLabel, QRadioButton, QPlainTextEdit, QPushButton]
boldNames = ["modeText", "outputText"]

def decodeOrEncode(mode, text):
  try:
   if mode == "d":
      bytes = text.encode("ascii")
      base64_bytes = base64.b64decode(bytes)
      base64_string = base64_bytes.decode("ascii")

      return base64_string
   else: #encode
     bytes = text.encode("ascii")
     base64_bytes = base64.b64encode(bytes)
     base64_string = base64_bytes.decode("ascii")

     return base64_string
  except BaseException:
    return False



"""our window"""
class Window(QWidget):
    
    
    def __init__(self):
        
            

        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setWindowTitle("base64 utils")

        titleFont = QFont("Arial", 20)
        titleFont.setBold(True)

        mainFont = QFont("Arial", 12)

        boldMainFont = QFont("Arial", 12)
        boldMainFont.setBold(True)

        mainCodeFont = QFont("")

        title = QLabel("base64 utils", self)
        title.setFont(titleFont)
        title.setAccessibleName("title")
        title.setObjectName("title")
        title.move(10, 0)
        

        modeText = QLabel("mode:", self)
        modeText.setObjectName("modeText")
        modeText.move(10, 40)

        self.encodeRadio = QRadioButton("encode", self)
        self.encodeRadio.setChecked(True)
        self.encodeRadio.move(10, 60)

        self.decodeRadio = QRadioButton("decode", self)
        self.decodeRadio.move(10, 80)

        self.text = QPlainTextEdit(self)
        self.text.move(10, 120)
        self.text.setObjectName("text")
        self.text.setFixedSize(480, 100)

        self.modeText = QLabel("output:", self)
        self.modeText.setObjectName("outputText")
        self.modeText.move(10, 230)

        self.output = QPlainTextEdit(self)
        self.output.move(10, 260)
        self.output.setObjectName("output")
        self.output.setFixedSize(480, 100)
        self.output.setReadOnly(True)

        self.button = QPushButton(self)
        self.button.setText("encode/decode")
        self.button.move(10, 370)
        self.button.setFixedSize(480, 50)

        self.button.clicked.connect(self.onGoButtonClicked)

        self.errorWindow = QMessageBox()
        self.setWhatsThis("an error")
        self.errorWindow.setText(ERROR_MSG)
        self.errorWindow.setWindowTitle("error :(")
        


        for type in mainFontClasses:
            labels = self.findChildren(type)
            for child in labels:
                if not child.objectName() == "title":
                    child.setFont(mainFont)
                    for boldN in boldNames:
                        if child.objectName() == boldN:
                            child.setFont(boldMainFont)

    def onGoButtonClicked(self):
        text = self.text
        output = self.output
        mode = ""
        if self.encodeRadio.isChecked():
            mode = "e"
        else: # decode mode
            mode = "d"

        result = decodeOrEncode(mode, text.toPlainText())
        
        if result != False:
            output.setPlainText(result)
        else:
            self.errorWindow.show()

    def keyPressEvent(self, event):
        if event.key() == ALT_KEY:
            self.onGoButtonClicked()


        
                    
                     

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

