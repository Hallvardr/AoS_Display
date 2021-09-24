from PyQt5 import QtWidgets
from adios import army_selection


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    army = QtWidgets.QMainWindow()
    ui = army_selection()
    ui.setupUi(army)
    army.show()
    sys.exit(app.exec_())