from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
# import re # may be needed for procedural dosage options, currently not working so import bypassed

import config as cfg


class IntInput(QLineEdit):
    def __init__(self, default_text=None, *args, **kwargs):
        super(QLineEdit, self).__init__(*args, **kwargs)
        self.setFixedWidth(25)
        self.setPlaceholderText(default_text)
        self.setAlignment(Qt.AlignHCenter)


class RadioExclusiveLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(QLineEdit, self).__init__(*args, **kwargs)
        self.setEnabled = False


class NewMedWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.setWindowTitle("Add medication")
        self.initUI()

    def initUI(self):
        # TODO: Separate sections to individual methods for readability
        # TODO: Split off elements that will be used for other windows
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

        # in-line dosage
        row_inline_dosage_container = QVBoxLayout()
        lbl_dosage = QLabel("Dosage:")
        row_inline_dosage_container.addWidget(lbl_dosage)
        # TODO: procedural rows from cfg.lst_freqs. for now, hard-coded
        # options
        self.dosage_options_grp = QButtonGroup()
        # ' option "Take [i], [n] times per day."
        # '' radio button
        opt1 = QHBoxLayout()
        opt1_radio = QRadioButton("Take")
        opt1_radio.setStatusTip("Take [i], [n] times per day.")
        self.dosage_options_grp.addButton(opt1_radio)
        opt1.addWidget(opt1_radio)
        # '' txt_i
        self.opt1_txt_i = QLineEdit()
        self.opt1_txt_i.setPlaceholderText("i")
        opt1.addWidget(self.opt1_txt_i)
        # '' ", " label
        lbl = QLabel(", ")
        opt1.addWidget(lbl)
        # '' txt_n
        self.opt1_txt_n = QLineEdit()
        self.opt1_txt_n.setPlaceholderText("n")
        opt1.addWidget(self.opt1_txt_n)
        lbl = QLabel(" times per day.")
        opt1.addWidget(lbl)
        # add to row
        row_inline_dosage_container.addLayout(opt1)

        # option "Take [i] as needed up to [n] times per day."
        opt2 = QHBoxLayout()
        opt2_radio = QRadioButton("Take")
        opt2_radio.setStatusTip("Take [i], [n] times per day.")
        self.dosage_options_grp.addButton(opt2_radio)
        opt2.addWidget(opt2_radio)
        # '' txt_i
        self.opt2_txt_i = QLineEdit()
        self.opt2_txt_i.setPlaceholderText("i")
        opt2.addWidget(self.opt2_txt_i)
        # '' ", " label
        lbl = QLabel(" as needed up to ")
        opt2.addWidget(lbl)
        # '' txt_n
        self.opt2_txt_n = QLineEdit()
        self.opt2_txt_n.setPlaceholderText("n")
        opt2.addWidget(self.opt2_txt_n)
        lbl = QLabel(" times per day.")
        opt2.addWidget(lbl)
        # add to row
        row_inline_dosage_container.addLayout(opt2)
        # option "Take according to regime."
        opt3 = QHBoxLayout()
        opt3_radio = QRadioButton("Take according to regime.")
        self.dosage_options_grp.addButton(opt3_radio)
        opt3.addWidget(opt3_radio)
        row_inline_dosage_container.addLayout(opt3)
        # option custom text row

        # add dosage inline to page wrapper
        wrapper.addLayout(row_inline_dosage_container)

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

    def switch_dosage(self):
        # store value as object var
        self.dosage_selected = self.dosage_radio_grp.checkedButton().text()
        # enable/disable i, n txtinput

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
