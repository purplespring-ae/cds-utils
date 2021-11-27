# EXTERNAL MODULES
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
# INTERNAL MODULES
import config as cfg

# ---------------------------------------------------------

# WIDGET OVERRIDES


class TextInput(QLineEdit):
    def __init__(self, min_width=None, max_width=None, default_text=None, *args, **kwargs):
        super(QLineEdit, self).__init__(*args, **kwargs)
        if min_width:
            self.setMinimumWidth(min_width)
        if max_width:
            self.setMaximumWidth(max_width)
        self.setPlaceholderText(default_text)


class DosageValueInput(QLineEdit):
    def __init__(self, placeholder, name, *args, **kwargs):
        super(QLineEdit, self).__init__(*args, **kwargs)
        self.setPlaceholderText(placeholder)
        self.setObjectName(name)
        self.setAlignment(Qt.AlignHCenter)


class ComboBox(QComboBox):
    def __init__(self, options=[], *args, **kwargs):
        super(ComboBox, self).__init__(*args, **kwargs)
        for opt in options:
            self.addItem(opt)


class HeadedTable(QTableWidget):
    def __init__(self, columns=[], *args, **kwargs):
        super(QTableWidget, self).__init__(*args, **kwargs)
        for column in columns:
            c = TableColumnHeader(column)
            self.setHorizontalHeaderItem(columns.index(column), c)


class TableColumnHeader(QTableWidgetItem):
    def __init__(self, title, *args, **kwargs):
        super(QTableWidgetItem, self).__init__(*args, **kwargs)
        self.setText(title)


# MAIN WIDGET

class MedsInTool(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.setWindowTitle("Medication In")
        self.build_UI()

    def build_UI(self):
        def build_r_header():
            elem = QHBoxLayout()
            # lbl_title = QLabel("Medication In")
            # elem.addWidget(lbl_title)
            return elem

        def build_t_med_editor():
            def r_med_name():
                elem = QFormLayout()
                lbl_name = QLabel("Medication name")
                self.txt_name = QLineEdit()
                elem.addRow(lbl_name, self.txt_name)
                return elem

            def r_str_qty():
                elem = QHBoxLayout()
                # -- strength input
                lbl_strength = QLabel("Strength")
                self.txt_strength = TextInput(100)
                # -- strength select unit
                self.cbo_strength_unit = ComboBox(cfg.valid_strength_units)
                self.cbo_strength_unit.setMaximumWidth(50)
                # -- qty
                lbl_qty = QLabel("Qty In")
                self.txt_qty = TextInput(None, 40)
                # --- add to layout & return
                elem.addWidget(lbl_strength)
                elem.addWidget(self.txt_strength)
                elem.addWidget(self.cbo_strength_unit)
                elem.addWidget(lbl_qty)
                elem.addWidget(self.txt_qty)
                return elem

            def r_input_dosage():
                def opt1():
                    # -- init option
                    opt = QHBoxLayout()
                    opt_str = "Take [i], [n] times per day."
                    # -- widgets
                    radio = QRadioButton("Take")
                    radio.setStatusTip(opt_str)
                    self.txt_i1 = DosageValueInput("i", "i1")
                    self.txt_i1.setEnabled(False)
                    lbl1 = QLabel(", ")
                    self.txt_n1 = DosageValueInput("n", "n1")
                    self.txt_n1.setEnabled(False)
                    lbl2 = QLabel(" times per day.")
                    # -- add to wlists
                    radios.append(radio)
                    self.dosage_inputs.extend([self.txt_i1, self.txt_n1])
                    # -- add to layout& return
                    opt.addWidget(radio)
                    opt.addWidget(self.txt_i1)
                    opt.addWidget(lbl1)
                    opt.addWidget(self.txt_n1)
                    opt.addWidget(lbl2)
                    return opt

                def opt2():
                    # -- init option
                    opt = QHBoxLayout()
                    opt_str = "Take [i], up to [n] times per day."
                    # -- widgets
                    radio = QRadioButton("Take")
                    radio.setStatusTip(opt_str)
                    self.txt_i2 = DosageValueInput("i", "i2")
                    self.txt_i2.setEnabled(False)
                    lbl1 = QLabel(" as needed up to ")
                    self.txt_n2 = DosageValueInput("n", "n2")
                    self.txt_n2.setEnabled(False)
                    lbl2 = QLabel(" times per day.")
                    # -- add to wlists
                    radios.append(radio)
                    self.dosage_inputs.extend([self.txt_i2, self.txt_n2])
                    # -- add to layout & return
                    opt.addWidget(radio)
                    opt.addWidget(self.txt_i2)
                    opt.addWidget(lbl1)
                    opt.addWidget(self.txt_n2)
                    opt.addWidget(lbl2)
                    return opt

                def opt3():
                    # -- init option
                    opt = QHBoxLayout()
                    opt_str = "Take according to regime."
                    # -- widgets
                    radio = QRadioButton(opt_str)
                    radio.setStatusTip(opt_str)
                    # -- add to layout, wlists & return
                    radios.append(radio)
                    opt.addWidget(radio)
                    return opt

                def opt4():
                    # -- init option
                    opt = QHBoxLayout()
                    # -- widgets
                    radio = QRadioButton("Custom")
                    radio.setStatusTip("Custom: ")
                    self.txt_custom_dosage = TextInput(
                        100, None, "Caution - use presets where possible.")
                    self.txt_custom_dosage.setEnabled(False)
                    # -- add to wlists
                    radios.append(radio)
                    self.dosage_inputs.append(self.txt_custom_dosage)
                    # -- add to layout & return
                    opt.addWidget(radio)
                    opt.addWidget(self.txt_custom_dosage)
                    return opt

                elem = QVBoxLayout()
                lbl_dosage = QLabel("Dosage:")
                radios = []
                self.dosage_inputs = []
                # --- add to element & return
                elem.addWidget(lbl_dosage)
                elem.addLayout(opt1())
                elem.addLayout(opt2())
                elem.addLayout(opt3())
                elem.addLayout(opt4())
                # --- radio buttons
                self.dosage_options = QButtonGroup()
                for radio in radios:
                    self.dosage_options.addButton(radio)
                # --- i, n textboxes
                #
                # --- return
                return elem

            def r_display_dosage():
                # --- layout
                elem = QHBoxLayout()
                # --- widgets
                self.dosage_statement = QLabel("...")
                self.dosage_statement.setMinimumWidth(300)
                self.dosage_statement.setAlignment(Qt.AlignHCenter)
                self.btn_validate = QPushButton("Check")
                self.btn_validate.setMaximumWidth(100)
                # -- add to layout & return
                elem.addWidget(self.dosage_statement)
                elem.addWidget(self.btn_validate)
                return elem

            def r_btns():
                elem = QHBoxLayout()
                self.btn_reset = QPushButton("Reset")
                self.btn_submit = QPushButton("Submit")
                elem.addWidget(self.btn_reset)
                elem.addWidget(self.btn_submit)
                return elem
            # --- layout
            elem = QVBoxLayout()
            # --- title
            lbl_title = QLabel("Edit Medication")
            elem.addWidget(lbl_title)
            elem.addLayout(r_med_name())
            elem.addLayout(r_str_qty())
            elem.addLayout(r_input_dosage())
            elem.addLayout(r_display_dosage())
            elem.addLayout(r_btns())
            return elem

        def build_t_med_table():
            elem = QVBoxLayout()
            # --- title row
            lbl_title = QLabel("Ready to check in")
            elem.addWidget(lbl_title)
            # --- table & buttons row
            row = QHBoxLayout()
            # -- table
            cols = ["Medication", "Strength", "Dosage", "Qty In"]
            self.meds_table = HeadedTable(cols)
            # -- buttons
            btn_panel = QVBoxLayout()
            panel_buttons = []
            self.btn_plus = QPushButton("+")
            self.btn_minus = QPushButton("-")
            self.btn_edit = QPushButton("Edit")
            self.btn_rm = QPushButton("Delete")
            panel_buttons.extend(
                [self.btn_plus, self.btn_minus, self.btn_edit, self.btn_rm])
            for btn in panel_buttons:
                btn_panel.addWidget(btn)
            # --- add to layout & return
            row.addWidget(self.meds_table)
            row.addLayout(btn_panel)
            return row

        def build_r_tools_0():
            elem = QHBoxLayout()
            elem.addLayout(build_t_med_editor())
            elem.addLayout(build_t_med_table())
            return elem

        # instantiate overall layout
        wrapper = QVBoxLayout()
        self.setLayout(wrapper)

        # add r elements to wrapper
        wrapper.addLayout(build_r_header())
        wrapper.addLayout(build_r_tools_0())


# APP


def main():
    app = QApplication(sys.argv)
    window = MedsInTool()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
