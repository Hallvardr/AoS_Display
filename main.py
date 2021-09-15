import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


def press_it():
    pass


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #Añadir título
        self.setWindowTitle("Warhammer AoS Game Display")

        #Set layout
        self.setLayout(qtw.QVBoxLayout())

        #Crear label
        my_label = qtw.QLabel("Test label")

        # CHange font size of label
        my_label.setFont(qtg.QFont("Helvetica", 18))

        self.layout().addWidget(my_label)

        #Create entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("0")
        self.layout().addWidget(my_entry)

        #Create a button
        my_button = qtw.QPushButton("+", clicked=lambda: sumar_cp())
        self.layout().addWidget(my_button)

        #Printear GUI
        self.show()

        def sumar_cp():
            my_label.setText(f"Hello {my_entry.text()}")
            my_entry.setText("1")

app = qtw.QApplication([])
mw = MainWindow()

#Run app
app.exec_()
