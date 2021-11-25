from types import NoneType
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

        # alternative dosage - radio boxes
        # TODO: implement QButtonGroup to allow use of .checkedButton()
        row_dosage_options = QVBoxLayout()
        self.lbl_dosage = QLabel("Dosage")
        row_dosage_options.addWidget(self.lbl_dosage)
        for type in cfg.list_freqs:
            this_type_row = QHBoxLayout()
            radio_option = QRadioButton(type)
            # TODO: connect to event which sets self.dosage_type
            radio_option.toggled.connect(
                lambda: self.set_dosage_option(radio_option))
            this_type_row.addWidget(radio_option)

            # add needed LineEdit widgets for i, n
            if "[i]" in type:
                txt_i = IntInput("i")
                txt_i.setEnabled(False)
                this_type_row.addWidget(txt_i)
            if "[n]" in type:
                txt_n = IntInput("n")
                txt_n.setEnabled(False)
                this_type_row.addWidget(txt_n)
            row_dosage_options.addLayout(this_type_row)
        custom_dosage = QLineEdit()
        custom_dosage.setPlaceholderText("Custom dosage (Caution!)")
        row_dosage_options.addWidget(custom_dosage)

        wrapper.addLayout(row_dosage_options)

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

        # submit/reset
        row_buttons = QHBoxLayout()
        self.btn_reset = QPushButton("Reset")
        self.btn_submit = QPushButton("Submit")
        self.btn_submit.setEnabled(False)  # disable until data validates
        row_buttons.addWidget(self.btn_reset)
        row_buttons.addWidget(self.btn_submit)
        wrapper.addLayout(row_buttons)

    def set_dosage_option(self, option):
        # TODO: link to radio buttons
        self.dosage_selected = option.text()
        print(self.dosage_selected)
        pass

    def validate_clicked(self):
        valid_data = {  # no need to validate fields derived from config.py
            self.txt_name: False,
            self.txt_strength: False,
            self.txt_qty: False
        }
        # validate medication name
        # validate strength
        # validate dosage
        # validate qty in

        # aggregate validation
        count_invalid = 0
        for field in valid_data:
            if not valid_data[field]:
                count_invalid += 1
                # TODO: store field for notification of invalid input to user
        if count_invalid != 0:
            self.btn_submit.setEnabled(True)
        else:
            pass  # TODO: indicate validation issues to user

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
