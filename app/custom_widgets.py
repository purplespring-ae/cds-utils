# EXTERNAL MODULES
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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
