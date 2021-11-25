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
        # TODO: Split off elements that will be used for other windows
        def row_medication():
            row_med_name = QFormLayout()
            self.lbl_name = QLabel("Medication name")
            self.txt_name = QLineEdit()
            row_med_name.addRow(self.lbl_name, self.txt_name)
            return row_med_name

        def row_strength_qty():
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
            return row_strength

        def row_dosage():
            row_inline_dosage_container = QVBoxLayout()
            lbl_dosage = QLabel("Dosage:")
            row_inline_dosage_container.addWidget(lbl_dosage)
            # TODO: procedural rows from cfg.lst_freqs. for now, hard-coded
            # options
            self.dosage_options_grp = QButtonGroup()
            list_exclusive_txtlines = []

            def opt1():
                opt_str = "Take [i], [n] times per day."
                # '' radio button
                opt1 = QHBoxLayout()
                opt1_radio = QRadioButton("Take")
                opt1_radio.setStatusTip(opt_str)
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
                self.opt1_txt_n.setEnabled(False)
                opt1.addWidget(self.opt1_txt_n)
                lbl = QLabel(" times per day.")
                opt1.addWidget(lbl)
                # add textlines to list for easy mass disable/enable
                list_exclusive_txtlines.append(self.opt1_txt_n)
                list_exclusive_txtlines.append(self.opt1_txt_i)
                return opt1

            def opt2():
                opt_str = "Take [i] as needed, up to [n] times per day."
                opt2 = QHBoxLayout()
                opt2_radio = QRadioButton("Take")
                opt2_radio.setStatusTip(opt_str)
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
                self.opt2_txt_n.setEnabled(False)
                opt2.addWidget(self.opt2_txt_n)
                lbl = QLabel(" times per day.")
                opt2.addWidget(lbl)
                # add textlines to list for easy mass disable/enable
                list_exclusive_txtlines.append(self.opt2_txt_n)
                list_exclusive_txtlines.append(self.opt2_txt_i)
                return opt2

            def opt3():
                opt_str = "Take according to regime."
                opt3 = QHBoxLayout()
                opt3_radio = QRadioButton(opt_str)
                opt3_radio.setStatusTip(opt_str)
                self.dosage_options_grp.addButton(opt3_radio)
                opt3.addWidget(opt3_radio)
                return opt3

            def opt4():
                # option custom text row
                opt4 = QHBoxLayout()
                opt4_radio = QRadioButton("Custom")
                opt4_radio.setStatusTip("Custom: ")
                self.dosage_options_grp.addButton(opt4_radio)
                opt4.addWidget(opt4_radio)
                self.opt4_txt = QLineEdit()
                self.opt4_txt.setPlaceholderText(
                    "Caution - use the preset options where possible.")
                self.opt4_txt.setEnabled(False)
                opt4.addWidget(self.opt4_txt)
                list_exclusive_txtlines.append(self.opt4_txt)
                return opt4

            # BUILD AND ADD ROWS
            row_inline_dosage_container.addLayout(opt1())
            row_inline_dosage_container.addLayout(opt2())
            row_inline_dosage_container.addLayout(opt3())
            row_inline_dosage_container.addLayout(opt4())

            # connect to handlers and prepare controls
            for txt in list_exclusive_txtlines:
                txt.setEnabled(False)
                txt.textChanged.connect(lambda: self.option_dosage_changed())

            for radio in self.dosage_options_grp.buttons():
                radio.released.connect(lambda: self.option_dosage_changed())

            self.opt4_txt.textChanged.connect(
                lambda: self.txt_custom_changed())
            return row_inline_dosage_container

        def row_statement():
            row_statement = QHBoxLayout()
            self.dosage_statement = QLabel("...")
            self.dosage_statement.setMinimumWidth(300)
            self.dosage_statement.setAlignment(Qt.AlignHCenter)
            self.btn_validate = QPushButton("Check")
            self.btn_validate.setMaximumWidth(150)
            self.btn_validate.clicked.connect(self.btn_clicked_validate)
            row_statement.addWidget(self.dosage_statement)
            row_statement.addWidget(self.btn_validate)
            return row_statement

        def row_buttons():
            row_buttons = QHBoxLayout()
            self.btn_reset = QPushButton("Reset")
            self.btn_submit = QPushButton("Submit")
            self.btn_submit.setEnabled(False)  # disable until data validates
            row_buttons.addWidget(self.btn_reset)
            row_buttons.addWidget(self.btn_submit)
            return row_buttons

        # wrapper for entire form
        wrapper = QVBoxLayout()
        self.setLayout(wrapper)

        wrapper.addLayout(row_medication())
        wrapper.addLayout(row_strength_qty())
        wrapper.addLayout(row_dosage())
        wrapper.addLayout(row_statement())
        wrapper.addLayout(row_buttons())

    # EVENT HANDLERS
    def option_dosage_changed(self):
        for radio in self.dosage_options_grp.buttons():
            if radio.isChecked():
                self.dosage_option = radio.statusTip()
                radio_i = self.dosage_options_grp.buttons().index(radio) + 1
                if radio_i == 1:
                    str_n = self.opt1_txt_n.text() if len(
                        self.opt1_txt_n.text()) != 0 else "[BLANK: n]"
                    str_i = self.opt1_txt_i.text() if len(
                        self.opt1_txt_i.text()) != 0 else "[BLANK: i]"
                    statement_str = self.dosage_option.replace(
                        "[n]", str_n)
                    statement_str = statement_str.replace(
                        "[i]", str_i)
                    # display statement
                    self.dosage_statement.setText(statement_str)
                    # clear & disable unselected txt input
                    # TODO: create class & method for toggleable txt inputs to avoid replicating code between options
                    self.opt1_txt_n.setEnabled(True)
                    self.opt1_txt_i.setEnabled(True)
                    self.opt2_txt_n.clear()
                    self.opt2_txt_i.clear()
                    self.opt4_txt.clear()
                    self.opt2_txt_n.setEnabled(False)
                    self.opt2_txt_i.setEnabled(False)
                    self.opt4_txt.setEnabled(False)
                elif radio_i == 2:
                    str_n = self.opt2_txt_n.text() if len(
                        self.opt2_txt_n.text()) != 0 else "[BLANK: n]"
                    str_i = self.opt2_txt_i.text() if len(
                        self.opt2_txt_i.text()) != 0 else "[BLANK: i]"
                    statement_str = self.dosage_option.replace(
                        "[n]", str_n)
                    statement_str = statement_str.replace(
                        "[i]", str_i)
                    # display statement
                    self.dosage_statement.setText(statement_str)
                    # clear & disable unselected txt input
                    self.opt2_txt_n.setEnabled(True)
                    self.opt2_txt_i.setEnabled(True)
                    self.opt1_txt_n.clear()
                    self.opt1_txt_i.clear()
                    self.opt4_txt.clear()
                    self.opt1_txt_n.setEnabled(False)
                    self.opt1_txt_i.setEnabled(False)
                    self.opt4_txt.setEnabled(False)
                elif radio_i == 3:
                    self.dosage_statement.setText(self.dosage_option)
                elif radio_i == 4:
                    self.opt4_txt.setEnabled(True)
                    statement_str = self.opt4_txt.text() if len(
                        self.opt4_txt.text()) != 0 else "[BLANK: custom dosage/frequency]"
                    self.dosage_statement.setText(
                        self.dosage_option + statement_str)
                    self.txt_custom_changed()
                else:
                    raise ValueError()

    def txt_custom_changed(self):
        statement_str = self.opt4_txt.text() if len(
            self.opt4_txt.text()) != 0 else "[BLANK: custom dosage/frequency]"
        self.dosage_statement.setText(self.dosage_option + statement_str)

    def refresh_statement(self):
        self.option_dosage_changed()

    def btn_clicked_validate(self):
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
