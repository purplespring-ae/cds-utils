from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

import config as cfg


class NewMedWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.setWindowTitle("Add medication")
        self.initUI()

    def initUI(self):
        wrapper = QFrame()
        grid = QGridLayout(wrapper)
        self.setLayout(grid)

        # set 3 column grid with 7 rows
        # for r in range(7):
        #     for c in range(3):
        #         # grid.addWidget(QLabel(f"{r},{c}"), r, c)
        #         grid.addWidget(QWidget())

        # medication name
        lbl_name = QLabel("Medication name")
        txt_name = QLineEdit()
        grid.addWidget(lbl_name, 0, 0)
        grid.addWidget(txt_name, 0, 1, 1, 3)

        # medication strength
        lbl_strength = QLabel("Strength")
        txt_strength_val = QLineEdit()
        grid.addWidget(lbl_strength, 1, 0)
        grid.addWidget(txt_strength_val, 1, 1)
        cbo_strength_unit = QComboBox()
        for unit in cfg.valid_strength_units:
            cbo_strength_unit.addItem(unit)
        grid.addWidget(cbo_strength_unit, 1, 2)

        # dosage

        # qty
        lbl_qty = QLabel("Qty In")
        txt_qty = QLineEdit()
        grid.addWidget(lbl_qty, 3, 0)
        grid.addWidget(txt_qty, 3, 1)


def main():
    app = QApplication(sys.argv)
    window = NewMedWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
