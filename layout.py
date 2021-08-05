from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QGridLayout, QTextEdit, QComboBox
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QPlainTextEdit
import sys
import ComputingSoftware
import SQLHandler



class SkewDiagramField(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)

class BioinformaticTool(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        opis = QLabel('''This is a DNA analyzing bioinformatic tool made based on Finding Hidden Messages in DNA (Bioinformatics I) course on Coursera provided
by University of California San Diego, and my own effort. Current features include transcription, translation, enzymatic retriction and finding origin of replication.''', self)
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
        self.setWindowTitle("DNAnalyzer")
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
        self.restricsButton = QPushButton("Restrict", self)
        self.secOutputWidnow = QLineEdit("", self)
        self.placeLabel = QLabel("Restriction location:", self)

        self.enzymesList.addItems(SQLHandler.ListPopulation())

        ukladT = QGridLayout()
        self.setLayout(ukladT)
        ukladT.setColumnStretch(0, 1)
        ukladT.setColumnStretch(1, 1)
        ukladT.setColumnStretch(2, 1)
        ukladT.setColumnStretch(3, 1)
        ukladT.addWidget(opis, 0, 0, 1, 4)
        ukladT.addWidget(self.inputWindow, 1, 0, 4, 2)
        ukladT.addWidget(self.outputWindow, 1, 2, 5, 2)
        ukladT.addWidget(self.enzymesList, 5, 0, 1, 2)
        ukladT.addWidget(self.restricsButton, 6, 0, 1, 2)
        ukladT.addWidget(self.secOutputWidnow, 6, 3, 1, 1)
        ukladT.addWidget(self.placeLabel, 6, 2, 1, 1)

        self.setLayout(ukladT)

        self.setGeometry(100, 60, 1000, 800)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("DNAnalyzer")

        self.restricsButton.clicked.connect(self.RetrictionButtonSoftware)

    def RetrictionButtonSoftware(self):
        singleCharCode = ["A","G","C","T","D","B","H","K","M","N","R","S","V","W","Y"]
        nadawca4 = self.sender()
        if nadawca4.text() == "Restrict":
            x = str(self.enzymesList.currentText())
            seq = SQLHandler.Quering(x)
            for letter in seq:
                if letter not in singleCharCode:
                    seq = seq.replace(letter, '')
            self.outputWindow.setPlainText()

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
        ukladT.setColumnStretch(0, 1)
        ukladT.setColumnStretch(1, 1)
        ukladT.setColumnStretch(2, 1)
        ukladT.setColumnStretch(3, 1)
        ukladT.setColumnStretch(4, 1)
        ukladT.setColumnStretch(5, 1)
        ukladT.setColumnStretch(6, 1)
        #ukladT.setColumnStretch(7, 1)
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
        self.setWindowTitle("DNAnalyzer")

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
        self.setWindowTitle("DNAnalyzer")

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
        self.diagram = SkewDiagramField()
        self.oriButton = QPushButton("Find Ori", self)
        self.saveButton = QPushButton("Save diagram", self)
        self.diagNameWidnow = QLineEdit("", self)
        self.minSkewLabel = QLabel("Approximate Ori:", self)
        self.minSkewWindow = QLineEdit("", self)

        ukladT = QGridLayout()
        ukladT.addWidget(opis, 0, 0, 1, 2)
        ukladT.addWidget(self.inputWindow, 1, 0, 4, 2)
        ukladT.addWidget(self.diagram, 1, 2, 4, 2)
        ukladT.addWidget(self.oriButton, 7, 0, 1, 4)
        ukladT.addWidget(self.saveButton, 6, 3, 1, 1)
        ukladT.addWidget(self.diagNameWidnow, 6, 2, 1, 1)
        ukladT.addWidget(self.minSkewLabel, 5, 2, 1, 1, alignment=Qt.AlignRight)
        ukladT.addWidget(self.minSkewWindow, 5, 3, 1, 1)
        ukladT.setColumnStretch(0, 1)
        ukladT.setColumnStretch(1, 1)
        ukladT.setColumnStretch(2, 1)
        ukladT.setColumnStretch(3, 1)

        self.setLayout(ukladT)

        self.resize(1600, 800)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("DNAnalyzer")

        self.oriButton.clicked.connect(self.software4)
        self.saveButton.clicked.connect(self.software4)

    def set_image(self, diagram):
        self.diagram.setPixmap(QPixmap(diagram))

    def software4(self):
        nadawca4 = self.sender()
        sequence = self.inputWindow.toPlainText()
        diagName = self.diagNameWidnow.text()
        if nadawca4.text() == "Find Ori":
            self.minSkewWindow.setText(str(ComputingSoftware.SkewDiagram(sequence)))
            self.set_image("SkewDiagram.png")
        elif nadawca4.text() == "Save diagram":
            ComputingSoftware.SaveDiagram(diagName, sequence)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = BioinformaticTool()
    sys.exit(app.exec_())
