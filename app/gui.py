from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

import config as cfg


class IntInput(QLineEdit):
    def __init__(self, default_text=None, *args, **kwargs):
        super(QLineEdit, self).__init__(*args, **kwargs)
        self.setFixedWidth(25)
        self.setPlaceholderText(default_text)
        self.setAlignment(Qt.AlignHCenter)


# class ReadOnlyTxt(QLineEdit): # gave up on this v quickly as existing QLabel is better
#     def __init__(self, *args, **kwargs):
#         super(QLineEdit, self).__init__(*args, **kwargs)
#         self.isReadOnly = True


class NewMedWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.setWindowTitle("Add medication")
        self.initUI()

    def initUI(self):
        # wrapper for entire form
        wrapper = QVBoxLayout()
        self.setLayout(wrapper)

        # medication name
        row_med_name = QFormLayout()
        lbl_name = QLabel("Medication name")
        txt_name = QLineEdit()
        row_med_name.addRow(lbl_name, txt_name)
        wrapper.addLayout(row_med_name)

        # medication strength
        # quantity in
        row_strength = QHBoxLayout()
        lbl_strength = QLabel("Strength")
        txt_strength = IntInput()
        txt_strength.setMinimumWidth(100)
        cbo_strength_unit = QComboBox()
        for unit in cfg.valid_strength_units:
            cbo_strength_unit.addItem(unit)
        cbo_strength_unit.setMaximumWidth(50)
        lbl_qty = QLabel("Qty In")
        txt_qty = QLineEdit()
        row_strength.addWidget(lbl_strength)
        row_strength.addWidget(txt_strength)
        row_strength.addWidget(cbo_strength_unit)
        row_strength.addWidget(lbl_qty)
        row_strength.addWidget(txt_qty)
        wrapper.addLayout(row_strength)

        # dosage
        row_dosage = QHBoxLayout()
        lbl_dosage = QLabel("Dosage")
        cbo_dosage_type = QComboBox()
        for type in cfg.freqs:
            cbo_dosage_type.addItem(cfg.freqs[type])
        txt_i = IntInput("i")
        txt_n = IntInput("n")
        row_dosage.addWidget(lbl_dosage)
        row_dosage.addWidget(cbo_dosage_type)
        row_dosage.addWidget(txt_i)
        row_dosage.addWidget(txt_n)
        wrapper.addLayout(row_dosage)

        # statement
        row_statement = QHBoxLayout()
        dosage_statement = QLabel("...")
        dosage_statement.setMinimumWidth(300)
        dosage_statement.setAlignment(Qt.AlignHCenter)
        btn_check = QPushButton("Check")
        btn_check.setMaximumWidth(150)
        row_statement.addWidget(dosage_statement)
        row_statement.addWidget(btn_check)
        wrapper.addLayout(row_statement)

        # submit
        row_buttons = QHBoxLayout()
        btn_reset = QPushButton("Reset")
        btn_submit = QPushButton("Submit")
        row_buttons.addWidget(btn_reset)
        row_buttons.addWidget(btn_submit)
        wrapper.addLayout(row_buttons)

        self.setLayout(wrapper)


def main():
    app = QApplication(sys.argv)
    window = NewMedWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
