# EXTERNAL MODULES
from typing import Text
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
# INTERNAL MODULES
import config as cfg
from custom_widgets import *

# ---------------------------------------------------------

# MAIN WIDGETS


class MainMenu(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.build_UI()
        self.init_connects()

    def build_UI(self):
        # TODO: build out MainMenu GUI
        # TODO: Main screen input for client details (Name, DOB, DOA, Room)
        def build_r_client():
            elem = QVBoxLayout()
            # - name
            row = QHBoxLayout()
            lbl = QLabel("Name")
            self.txt_client_fname = TextInput(100, 200, "First name")
            self.txt_client_sname = TextInput(100, 200, "Surname")
            row.addWidget(lbl)
            row.addWidget(self.txt_client_fname)
            row.addWidget(self.txt_client_sname)
            elem.addLayout(row)
            # - DOB
            row = QHBoxLayout()
            lbl = QLabel("Date of Birth")
            self.txt_dob_d = TextInput(50, 100, "DD")
            self.txt_dob_m = TextInput(50, 100, "MM")
            self.txt_dob_y = TextInput(50, 100, "YY")
            row.addWidget(lbl)
            row.addWidget(self.txt_dob_d)
            row.addWidget(self.txt_dob_m)
            row.addWidget(self.txt_dob_y)
            elem.addLayout(row)
            # - DOA
            row = QHBoxLayout()
            lbl = QLabel("Date of Admission")
            self.txt_doa_d = TextInput(50, 100, "DD")
            self.txt_doa_m = TextInput(50, 100, "MM")
            self.txt_doa_y = TextInput(50, 100, "YY")
            row.addWidget(lbl)
            row.addWidget(self.txt_doa_d)
            row.addWidget(self.txt_doa_m)
            row.addWidget(self.txt_doa_y)
            elem.addLayout(row)

        def build_r_staff():
            elem = QFormLayout()
            lbl = QLabel("Staff initials:")
            self.txt_staff = TextInput(50, 100)
            elem.addRow(lbl, self.txt_staff)
            return elem

        def build_r_buttons():
            elem = QVBoxLayout()
            self.btn_checklist = QPushButton("Admission Checklist", self)
            self.btn_confidentiality = QPushButton(
                "Confidentiality Waiver", self)
            self.btn_property = QPushButton("Property Waiver", self)
            self.btn_meds_in = QPushButton("Meds In", self)
            self.btn_meds_out = QPushButton("Meds Out", self)
            buttons = [self.btn_checklist, self.btn_confidentiality,
                       self.btn_property, self.btn_meds_in, self.btn_meds_out]
            elem.addWidget([btn for btn in buttons])
            self.main_menu_buttons = QButtonGroup(self)
            self.main_menu_buttons.addButton([btn for btn in buttons])

        # instantiate overall layout
        wrapper = QVBoxLayout()
        self.setLayout(wrapper)

        # add r elements to wrapper
        wrapper.addLayout(build_r_client())
        wrapper.addLayout(build_r_staff())
        wrapper.addLayout(build_r_buttons())

    def init_connects(self):
        # TODO: add MainMenu functionality
        pass


class MedsInTool(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.setWindowTitle("Medication In")
        self.build_UI()
        self.init_connects()

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


class MedsOutTool(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.build_UI()
        self.init_connects()

    def build_UI(self):
        # TODO: build out MedsOutTool GUI
        pass

    def init_connects(self):
        # TODO: add MedsOutTool functionality
        pass


class ChecklistTool(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.build_UI()
        self.init_connects()

    def build_UI(self):
        # TODO: Build out ChecklistTool GUI
        pass

    def init_connects(self):
        # TODO: Add ChecklistTool functionality
        pass


class ConfidentialityWaiverTool(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.build_UI()
        self.init_connects()

    def build_UI(self):
        # TODO: build out ConfidentialityWaiverTool GUI
        pass

    def init_connects(self):
        # TODO: add ConfidentialityWaiverTool functionality
        pass


class PropertyWaiverTool(QWidget):
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.build_UI()
        self.init_connects()

    def build_UI(self):
        # TODO: build out PropertyWaiverTool GUI
        pass

    def init_connects(self):
        # TODO: add PropertyWaiverTool functionality
        pass

# APP


def main():
    app = QApplication(sys.argv)
    window = MedsInTool()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
