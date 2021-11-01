import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter


class CurrencyConvert(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConvert, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('arrow.png'))

        self.ui.input_valute_from.setPlaceholderText('Из валюты')
        self.ui.input_money.setPlaceholderText('Сколько')
        self.ui.input_valute_to.setPlaceholderText('В валюту')
        self.ui.result.setPlaceholderText('Получите:')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        converter = CurrencyConverter()
        valute_from = self.ui.input_valute_from.text()
        money = int(self.ui.input_money.text())
        valute_to = self.ui.input_valute_to.text()

        result = round(converter.convert(money, valute_from, valute_to), 2)

        self.ui.result.setText(str(result))


app = QtWidgets.QApplication([])
apllication = CurrencyConvert()
apllication.show()

sys.exit(app.exec_())
