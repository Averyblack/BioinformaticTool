from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout, QTextEdit, QComboBox
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QPlainTextEdit
import sys
import ComputingSoftware
import SQLHandler
class BioinformaticTool(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        opis = QLabel("Placeholder opisu", self)
        oriButton = QPushButton("Ori", self)
        transcriptionButton = QPushButton("Transcription", self)
        translationButton = QPushButton("Translation", self)
        restrictionSiteButton = QPushButton("Restriction Site", self)

        ukladT = QGridLayout()
        ukladT.addWidget(opis, 0, 0, 1, 2)
        ukladT.addWidget(oriButton, 1, 0, 1, 1)
        ukladT.addWidget(transcriptionButton, 2, 0, 1, 1)
        ukladT.addWidget(translationButton, 3, 0, 1, 1)
        ukladT.addWidget(restrictionSiteButton, 4, 0, 1, 1)

        self.setLayout(ukladT)

        self.setGeometry(20, 20, 1000, 300)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Bioinformatic tool placeholder")
        self.show()

        oriButton.clicked.connect(self.software)
        transcriptionButton.clicked.connect(self.software)
        translationButton.clicked.connect(self.software)
        restrictionSiteButton.clicked.connect(self.software)

    def software(self):

        nadawca = self.sender()

        if nadawca.text() == "Transcription":
            self.okno = TranscriptionWindow()
            self.okno.show()
        elif nadawca.text() == "Translation":
            self.okno = TranslationWindow()
            self.okno.show()
        elif nadawca.text() == "Ori":
            self.okno = OriWindow()
            self.okno.show()
        elif nadawca.text() == "Restriction Site":
            self.okno = RestrictionWindow()
            self.okno.show()

class RestrictionWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        opis = QLabel("Placeholder opisu", self)
        self.inputWindow = QTextEdit("", self)
        self.outputWindow = QTextEdit("", self)
        self.enzymesList = QComboBox(self)
        restricsButton = QPushButton("Restrict", self)
        self.secOutputWidnow = QTextEdit("", self)
        self.placeLabel = QLabel("Restriction location:", self)

        self.enzymesList.addItems(SQLHandler.ListPopulation())

        ukladT = QGridLayout()
        ukladT.addWidget(opis, 0, 0, 1, 4)
        ukladT.addWidget(self.inputWindow, 1, 0, 4, 2)
        ukladT.addWidget(self.outputWindow, 1, 2, 5, 2)
        ukladT.addWidget(self.enzymesList, 5, 0, 1, 2)
        ukladT.addWidget(restricsButton, 6, 0, 2, 2)
        ukladT.addWidget(self.secOutputWidnow, 6, 3, 2, 1)
        ukladT.addWidget(self.placeLabel, 6, 2, 2, 1)

        self.setLayout(ukladT)

        self.setGeometry(20, 20, 1000, 300)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Bioinformatic tool placeholder")

        restricsButton.clicked.connect(self.RetrictionButtonSoftware)

    def RetrictionButtonSoftware(self):
        singleCharCode = ["A","G","C","T","D","B","H","K","M","N","R","S","V","W","Y"]
        nadawca4 = self.sender()
        if nadawca4.text() == "Restrict":
            x = str(self.enzymesList.currentText())
            seq = SQLHandler.Quering(x)
            for letter in seq:
                if letter not in singleCharCode:
                    seq = seq.replace(letter, '')
            self.outputWindow.setPlainText(seq)





class TranscriptionWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):
        self.inputWindow = QTextEdit("", self)
        opis = QLabel("Placeholder opisu", self)
        transcribeButton = QPushButton("Transcribe", self)
        self.outputWindow = QTextEdit("", self)
        GClabel = QLabel("G/C percentage:", self)
        ATlabel = QLabel("A/T percentage:", self)
        self.GCwindow = QLineEdit("", self)
        self.ATwindow = QLineEdit("", self)
        NctNumlabel = QLabel("Number of nucleotides:", self)
        self.NctNumwindow = QLineEdit("", self)

        ukladT = QGridLayout()
        ukladT.addWidget(opis, 0, 0, 1, 8)
        ukladT.addWidget(self.inputWindow, 1, 0, 6, 4)
        ukladT.addWidget(self.outputWindow, 1, 4, 3, 4)
        ukladT.addWidget(transcribeButton, 7, 0, 1, 8)
        ukladT.addWidget(GClabel, 4, 4, 1, 1)
        ukladT.addWidget(ATlabel, 5, 4, 1, 1)
        ukladT.addWidget(self.GCwindow, 4, 5, 1, 3)
        ukladT.addWidget(self.ATwindow, 5, 5, 1, 3)
        ukladT.addWidget(NctNumlabel, 6, 4, 1, 3)
        ukladT.addWidget(self.NctNumwindow, 6, 6, 1, 2)


        self.setLayout(ukladT)

        self.setGeometry(20, 20, 1000, 300)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Bioinformatic tool placeholder")

        transcribeButton.clicked.connect(self.software2)

    def software2(self):

        nadawca2 = self.sender()
        sequence = self.inputWindow.toPlainText()
        if nadawca2.text() == "Transcribe":
            output1 = ComputingSoftware.Transcription(sequence)
            self.outputWindow.setPlainText(output1)
            output2 = ComputingSoftware.NumberOfNucleotides(output1)
            self.NctNumwindow.setText(str(output2))
            output3 = ComputingSoftware.GCPercentageCount(output1)
            self.GCwindow.setText(str(output3))
            output4 = ComputingSoftware.ATPercentageCount(output3)
            self.ATwindow.setText(str(output4))

class TranslationWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

                # etykiety
        opis = QLabel("Placeholder opisu", self)
        self.inputWindow = QTextEdit("", self)
        translateButton = QPushButton("Translate", self)
        self.outputWindow = QTextEdit("", self)
        masLabel = QLabel("Mol. mass: ", self)
        self.mas = QLineEdit("", self)

        ukladT = QGridLayout()
        ukladT.addWidget(opis, 0, 0, 1, 4)
        ukladT.addWidget(self.inputWindow, 1, 0, 3, 3)
        ukladT.addWidget(translateButton, 4, 0, 1, 6)
        ukladT.addWidget(self.outputWindow, 1, 3, 2, 3)
        ukladT.addWidget(masLabel, 3, 3, 1, 1)
        ukladT.addWidget(self.mas, 3, 4, 1, 2)

        self.setLayout(ukladT)

        self.setGeometry(20, 20, 1000, 300)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Bioinformatic tool placeholder")

        translateButton.clicked.connect(self.software3)

    def software3(self):

        nadawca3 = self.sender()
        sequence = self.inputWindow.toPlainText()
        if nadawca3.text() == "Translate":
            output = ComputingSoftware.Translation(sequence)
            molecularWeight = ComputingSoftware.MolecularWeight(output)
            self.outputWindow.setPlainText(output)
            self.mas.setText(str(molecularWeight))

class OriWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        opis = QLabel("Placeholder opisu", self)
        self.inputWindow = QTextEdit("", self)

        ukladT = QGridLayout()
        ukladT.addWidget(opis, 0, 0, 1, 2)
        ukladT.addWidget(self.inputWindow, 1, 0, 4, 1)

        self.setLayout(ukladT)

        self.setGeometry(20, 20, 1000, 300)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Bioinformatic tool placeholder")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    okno = BioinformaticTool()
    sys.exit(app.exec_())
