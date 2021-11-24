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
        self.lbl_name = QLabel("Medication name")
        self.txt_name = QLineEdit()
        row_med_name.addRow(self.lbl_name, self.txt_name)
        wrapper.addLayout(row_med_name)

        # medication strength
        # quantity in
        row_strength = QHBoxLayout()
        self.lbl_strength = QLabel("Strength")
        self.txt_strength = IntInput()
        self.txt_strength.setMinimumWidth(100)
        self.cbo_strength_unit = QComboBox()
        for unit in cfg.valid_strength_units:
            self.cbo_strength_unit.addItem(unit)
        self.cbo_strength_unit.setMaximumWidth(50)
        self.lbl_qty = QLabel("Qty In")
        self.txt_qty = QLineEdit()
        row_strength.addWidget(self.lbl_strength)
        row_strength.addWidget(self.txt_strength)
        row_strength.addWidget(self.cbo_strength_unit)
        row_strength.addWidget(self.lbl_qty)
        row_strength.addWidget(self.txt_qty)
        wrapper.addLayout(row_strength)

        # dosage
        row_dosage = QHBoxLayout()
        self.lbl_dosage = QLabel("Dosage")
        self.cbo_dosage_type = QComboBox()
        for type in cfg.freqs:
            self.cbo_dosage_type.addItem(cfg.freqs[type])
        self.txt_i = IntInput("i")
        self.txt_n = IntInput("n")
        row_dosage.addWidget(self.lbl_dosage)
        row_dosage.addWidget(self.cbo_dosage_type)
        row_dosage.addWidget(self.txt_i)
        row_dosage.addWidget(self.txt_n)
        wrapper.addLayout(row_dosage)

        # statement
        row_statement = QHBoxLayout()
        self.dosage_statement = QLabel("...")
        self.dosage_statement.setMinimumWidth(300)
        self.dosage_statement.setAlignment(Qt.AlignHCenter)
        self.btn_validate = QPushButton("Check")
        self.btn_validate.setMaximumWidth(150)
        self.btn_validate.clicked.connect(self.validate_clicked)
        row_statement.addWidget(self.dosage_statement)
        row_statement.addWidget(self.btn_validate)
        wrapper.addLayout(row_statement)

        # submit
        row_buttons = QHBoxLayout()
        self.btn_reset = QPushButton("Reset")
        self.btn_submit = QPushButton("Submit")
        self.btn_submit.setEnabled(False)  # disable until data validates
        row_buttons.addWidget(self.btn_reset)
        row_buttons.addWidget(self.btn_submit)
        wrapper.addLayout(row_buttons)

    def validate_clicked(self):
        is_input_valid = False
        # validate medication name
        # validate strength
        # validate dosage
        # validate qty in

        if is_input_valid:
            self.btn_submit.setEnabled(True)

    def reset_clicked(self):
        pass

    def submit_clicked(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = NewMedWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
