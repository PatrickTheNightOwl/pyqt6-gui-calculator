from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6 import uic
import sys
import os

class Calculator(QMainWindow) :
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/calculator.ui",self)
        self.output.setText("")
        self.error_state = False
        # self.buttonname = [
        #     "decimal","divide","multiply",
        #     "minus","num0","num1","num2",
        #     "num3","num4","num5","num6",
        #     "num7","num8","num9","plus"
        # ]
        # self.buttonlist = []
        # for name in self.buttonname:
        #     btn = self.findChild(QPushButton, name)
        #     if btn:
        #         self.buttonlist.append(btn)
        #         btn.clicked.connect(lambda checked, b=name: self.AddText(b))
        self.buttonlist = [
            self.num0, self.num1, self.num2, self.num3,
            self.num4,self.num5, self.num6, self.num7, self.num8, 
            self.num9
        ]
        # self.num0.clicked.connect(lambda _, b="0":self.AddText(b))
        # self.num1.clicked.connect(lambda _, b="1":self.AddText(b))
        # self.num2.clicked.connect(lambda _, b="2":self.AddText(b))
        # self.num3.clicked.connect(lambda _, b="3":self.AddText(b))
        # self.num4.clicked.connect(lambda _, b="4":self.AddText(b))
        # self.num5.clicked.connect(lambda _, b="5":self.AddText(b))
        # self.num6.clicked.connect(lambda _, b="6":self.AddText(b))
        # self.num7.clicked.connect(lambda _, b="7":self.AddText(b))
        # self.num8.clicked.connect(lambda _, b="8":self.AddText(b))
        # self.num9.clicked.connect(lambda _, b="9":self.AddText(b))
        for b in self.buttonlist:
            b.clicked.connect(lambda _, x=b.text()[-1]: self.AddText(x))
        self.decimal.clicked.connect(lambda _, b=".":self.AddText(b))
        self.divide.clicked.connect(lambda _, b="/":self.AddText(b))
        self.multiply.clicked.connect(lambda _, b="*":self.AddText(b))
        self.minus.clicked.connect(lambda _, b="-":self.AddText(b))
        self.plus.clicked.connect(lambda _, b="+":self.AddText(b))
        self.modulo.clicked.connect(lambda _, b="%":self.AddText(b))
        self.calc.clicked.connect(self.Solve)
        self.shutdown.clicked.connect(self.ShutdownChoice)
        self.del_all.clicked.connect(self.DeleteAll)
        self.del_one.clicked.connect(self.DeleteText)
    def AddText(self, new):
        if self.error_state == True :
            self.output.setText("")
            self.error_state = False
        current = self.output.text()
        current += new # 'num0' -> '0'
        self.output.setText(current)
    def DeleteText(self) :
        current = self.output.text()
        current = current[:-1]
        self.output.setText(current)
    def ShutdownChoice(self) :
        self.close()
    def DeleteAll(self) :
        self.output.setText("")
    def Solve(self) :
        expression = self.output.text()
        try:
            result = eval(expression)
            if isinstance(result, float) and result.is_integer() :
                result = int(result)
            self.output.setText(str(result))
        except Exception:
            self.output.setText("Error")
            self.error_state = True
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main = Calculator()
    main.show()
    app.exec()
    