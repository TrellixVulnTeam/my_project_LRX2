import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter
from variables import can_convert


class CurrencyConvert(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConvert, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.widget.hide()
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('arrow.png'))

        self.ui.input_valute_from.setPlaceholderText('Из валюты')
        self.ui.input_money.setPlaceholderText('Сколько')
        self.ui.input_valute_to.setPlaceholderText('В валюту')
        self.ui.result.setPlaceholderText('Получите:')
        self.ui.convert_button.clicked.connect(self.converter)
        self.ui.error_push_button.clicked.connect(self.close_error)

    def close_error(self):
        self.ui.widget.hide()

    def converter(self):
        try:
            valute_from = self.ui.input_valute_from.text()
            money = int(self.ui.input_money.text())
            valute_to = self.ui.input_valute_to.text()
            if (valute_to in can_convert) and (valute_from in can_convert) and (money > 0):
                converter = CurrencyConverter()
                result = round(converter.convert(money, valute_from, valute_to), 2)
                self.ui.result.setText(str(result))
        except:
            self.ui.widget.show()
            self.ui.input_valute_from.setText('')
            self.ui.input_money.setText('')
            self.ui.input_valute_to.setText('')
            self.ui.result.setText('')
            self.ui.error_label.setText('Неправильные данные')



app = QtWidgets.QApplication([])
apllication = CurrencyConvert()
apllication.show()

sys.exit(app.exec_())
