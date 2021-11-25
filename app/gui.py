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
            self.lbl_strength.setAlignment(Qt.AlignRight)
            self.txt_strength = IntInput()
            self.txt_strength.setMinimumWidth(100)
            self.cbo_strength_unit = QComboBox()
            for unit in cfg.valid_strength_units:
                self.cbo_strength_unit.addItem(unit)
            self.cbo_strength_unit.setMaximumWidth(50)
            self.lbl_qty = QLabel("Qty In")
            self.lbl_qty.setAlignment(Qt.AlignRight)
            self.txt_qty = IntInput()
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

            def opt1():
                opt_str = "Take [i], [n] times per day."
                # '' radio button
                opt1 = QHBoxLayout()
                opt1_radio = QRadioButton("Take")
                opt1_radio.setStatusTip(opt_str)
                self.dosage_options_grp.addButton(opt1_radio)
                opt1.addWidget(opt1_radio)
                # '' txt_i
                self.opt1_txt_i = IntInput("i")
                self.opt1_txt_i.setPlaceholderText("i")
                self.opt1_txt_i.setObjectName("opt1_txt_i")
                opt1.addWidget(self.opt1_txt_i)
                # '' ", " label
                lbl = QLabel(", ")
                opt1.addWidget(lbl)
                # '' txt_n
                self.opt1_txt_n = IntInput("n")
                self.opt1_txt_n.setPlaceholderText("n")
                self.opt1_txt_n.setEnabled(False)
                self.opt1_txt_n.setObjectName("opt1_txt_n")
                opt1.addWidget(self.opt1_txt_n)
                lbl = QLabel(" times per day.")
                opt1.addWidget(lbl)
                # add textlines to list for easy mass disable/enable
                self.list_exclusive_txtlines.append(self.opt1_txt_n)
                self.list_exclusive_txtlines.append(self.opt1_txt_i)
                # set alignment
                for widget in opt1.children():
                    print(widget)
                    widget.setAlignment(Qt.AlignLeft)
                return opt1

            def opt2():
                opt_str = "Take [i] as needed, up to [n] times per day."
                opt2 = QHBoxLayout()
                opt2_radio = QRadioButton("Take")
                opt2_radio.setStatusTip(opt_str)
                self.dosage_options_grp.addButton(opt2_radio)
                opt2.addWidget(opt2_radio)
                # '' txt_i
                self.opt2_txt_i = IntInput("i")
                self.opt2_txt_i.setPlaceholderText("i")
                self.opt2_txt_i.setObjectName("opt2_txt_i")
                opt2.addWidget(self.opt2_txt_i)
                # '' ", " label
                lbl = QLabel(" as needed up to ")
                opt2.addWidget(lbl)
                # '' txt_n
                self.opt2_txt_n = IntInput("n")
                self.opt2_txt_n.setPlaceholderText("n")
                self.opt2_txt_n.setEnabled(False)
                self.opt2_txt_n.setObjectName("opt2_txt_n")
                opt2.addWidget(self.opt2_txt_n)
                lbl = QLabel(" times per day.")
                opt2.addWidget(lbl)
                # add textlines to list for easy mass disable/enable
                self.list_exclusive_txtlines.append(self.opt2_txt_n)
                self.list_exclusive_txtlines.append(self.opt2_txt_i)
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
                self.list_exclusive_txtlines.append(self.opt4_txt)
                return opt4

            # BUILD AND ADD ROWS
            row_inline_dosage_container.addLayout(opt1())
            row_inline_dosage_container.addLayout(opt2())
            row_inline_dosage_container.addLayout(opt3())
            row_inline_dosage_container.addLayout(opt4())

            # connect to handlers and prepare controls
            for txt in self.list_exclusive_txtlines:
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
            self.btn_validate.clicked.connect(self.btn_validate_clicked)
            row_statement.addWidget(self.dosage_statement)
            row_statement.addWidget(self.btn_validate)
            return row_statement

        def row_buttons():
            row_buttons = QHBoxLayout()
            self.btn_reset = QPushButton("Reset")
            self.btn_reset.clicked.connect(lambda: self.reset_clicked())
            self.btn_submit = QPushButton("Submit")
            self.btn_submit.setEnabled(False)  # disable until data validates
            self.btn_submit.clicked.connect(lambda: self.submit_clicked())
            row_buttons.addWidget(self.btn_reset)
            row_buttons.addWidget(self.btn_submit)
            return row_buttons

        # wrapper for entire form
        wrapper = QVBoxLayout()
        self.setLayout(wrapper)
        self.list_exclusive_txtlines = []

        wrapper.addLayout(row_medication())
        wrapper.addLayout(row_strength_qty())
        wrapper.addLayout(row_dosage())
        wrapper.addLayout(row_statement())
        wrapper.addLayout(row_buttons())

    # EVENT HANDLERS
    def option_dosage_changed(self):
        # disable submit button to force re-validation
        self.btn_submit.setEnabled(False)
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

                    self.active_n = self.opt1_txt_n
                    self.opt1_txt_i.setEnabled(True)
                    self.active_i = self.opt1_txt_i
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
                    self.active_n = self.opt2_txt_n
                    self.opt2_txt_i.setEnabled(True)
                    self.active_i = self.opt2_txt_i
                    self.opt1_txt_n.clear()
                    self.opt1_txt_i.clear()
                    self.opt4_txt.clear()
                    self.opt1_txt_n.setEnabled(False)
                    self.opt1_txt_i.setEnabled(False)
                    self.opt4_txt.setEnabled(False)
                elif radio_i == 3:
                    self.active_n = None
                    self.active_i = None
                    self.dosage_statement.setText(self.dosage_option)
                elif radio_i == 4:
                    self.active_n = None
                    self.active_i = None
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

    def btn_validate_clicked(self):
        valid_data = {  # default to fail
            "name": False,
            "strength": False,
            "qty": False,
            "n": False,
            "i": False
        }
        # validate medication name
        if self.txt_name.text():
            valid_data.update({"name": True})
        # validate strength
        if self.txt_strength.text():
            valid_data.update({"strength": True})
        # validate dosage
        opt_str = self.dosage_options_grp.checkedButton().statusTip(
        ) if self.dosage_options_grp.checkedButton() else ""
        if "[n]" in opt_str or "[i]" in opt_str:
            # active_n and active_i are set, get which ones
            for txt in self.list_exclusive_txtlines:
                if txt.isEnabled() and txt.text():
                    valid_data.update({txt.objectName()[-1:]: True})
                elif txt.isEnabled():
                    valid_data.update({txt.objectName()[-1:]: False})
        elif self.dosage_options_grp.checkedButton():
            # option 3 or 4. n text fields to validate
            valid_data.update({"n": True})
            valid_data.update({"i": True})
        else:
            # no dosage selected, fail validation
            return False

        # validate qty in
        if self.txt_qty.text():
            valid_data.update({"qty": True})

        # aggregate validation
        print(valid_data)
        if False not in valid_data.values():
            self.btn_submit.setEnabled(True)
        else:
            pass
            # TODO: indicate validation issues to user

    def reset_clicked(self):
        self.txt_name.clear()
        self.txt_strength.clear()
        self.txt_qty.clear()
        self.opt1_txt_i.clear()
        self.opt1_txt_n.clear()
        self.opt2_txt_i.clear()
        self.opt2_txt_n.clear()
        self.opt4_txt.clear()
        # TODO: Why does this not uncheck dosage radio button?
        dosage_checked = self.dosage_options_grp.checkedButton()
        dosage_checked.setChecked(False)

    def submit_clicked(self):
        self.btn_validate_clicked()  # force re-validation
        export_values = {
            "name": self.txt_name.text(),
            "strength": self.txt_strength.text() + self.cbo_strength_unit.currentText(),
            "qty_in": self.txt_qty.text(),
            "dosage": self.dosage_statement.text()
        }
        print(export_values)


def main():
    app = QApplication(sys.argv)
    window = NewMedWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
