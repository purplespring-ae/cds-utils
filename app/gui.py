# EXTERNAL MODULES
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
# INTERNAL MODULES
import config as cfg

# ---------------------------------------------------------

# WIDGET OVERRIDES


class ShortIntInput(QLineEdit):
    def __init__(self, default_text=None, *args, **kwargs):
        super(QLineEdit, self).__init__(*args, **kwargs)
        self.setFixedWidth(25)
        self.setPlaceholderText(default_text)
        self.setAlignment(Qt.AlignHCenter)


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
        self.build_UI()

    def build_UI(self):
        def r_header():
            elem = QHBoxLayout()
            lbl_title = QLabel("Medication In")
            elem.addWidget(lbl_title)
            return elem

        def t_med_editor():
            elem = QVBoxLayout()
            lbl_title = QLabel("Edit Medication")
            elem.addWidget(lbl_title)
            return elem

        def t_med_table():
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

        def r_tools_0():
            elem = QHBoxLayout()
            elem.addLayout(t_med_editor())
            elem.addLayout(t_med_table())
            return elem

        # instantiate overall layout
        wrapper = QVBoxLayout()
        self.setLayout(wrapper)

        # add r elements to wrapper
        wrapper.addLayout(r_header())
        wrapper.addLayout(r_tools_0())


# APP


def main():
    app = QApplication(sys.argv)
    window = MedsInTool()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
