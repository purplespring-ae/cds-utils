from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(510, 640)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 110, 422, 361))
        self.options_container = QVBoxLayout(self.verticalLayoutWidget)
        self.options_container.setObjectName(u"options_container")
        self.options_container.setContentsMargins(0, 0, 0, 0)
        self.ctr_option_1 = QHBoxLayout()
        self.ctr_option_1.setObjectName(u"ctr_option_1")
        self.radio1 = QRadioButton(self.verticalLayoutWidget)
        self.radio1.setObjectName(u"radio1")

        self.ctr_option_1.addWidget(self.radio1)

        self.opt1_i = QLineEdit(self.verticalLayoutWidget)
        self.opt1_i.setObjectName(u"opt1_i")
        self.opt1_i.setAlignment(Qt.AlignCenter)

        self.ctr_option_1.addWidget(self.opt1_i)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.ctr_option_1.addWidget(self.label)

        self.opt1_n = QLineEdit(self.verticalLayoutWidget)
        self.opt1_n.setObjectName(u"opt1_n")
        self.opt1_n.setAlignment(Qt.AlignCenter)

        self.ctr_option_1.addWidget(self.opt1_n)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.ctr_option_1.addWidget(self.label_2)

        self.options_container.addLayout(self.ctr_option_1)

        self.ctr_option_2 = QHBoxLayout()
        self.ctr_option_2.setObjectName(u"ctr_option_2")
        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.ctr_option_2.addWidget(self.radioButton_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.ctr_option_2.addWidget(self.label_3)

        self.opt1_i_2 = QLineEdit(self.verticalLayoutWidget)
        self.opt1_i_2.setObjectName(u"opt1_i_2")
        self.opt1_i_2.setAlignment(Qt.AlignCenter)

        self.ctr_option_2.addWidget(self.opt1_i_2)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.ctr_option_2.addWidget(self.label_4)

        self.opt1_n_2 = QLineEdit(self.verticalLayoutWidget)
        self.opt1_n_2.setObjectName(u"opt1_n_2")
        self.opt1_n_2.setAlignment(Qt.AlignCenter)

        self.ctr_option_2.addWidget(self.opt1_n_2)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.ctr_option_2.addWidget(self.label_5)

        self.options_container.addLayout(self.ctr_option_2)

        self.ctr_option_3 = QHBoxLayout()
        self.ctr_option_3.setObjectName(u"ctr_option_3")
        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.ctr_option_3.addWidget(self.radioButton_3)

        self.options_container.addLayout(self.ctr_option_3)

        self.ctr_option_4 = QHBoxLayout()
        self.ctr_option_4.setObjectName(u"ctr_option_4")
        self.radioButton = QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.ctr_option_4.addWidget(self.radioButton)

        self.txt_customdosage = QLineEdit(self.verticalLayoutWidget)
        self.txt_customdosage.setObjectName(u"txt_customdosage")

        self.ctr_option_4.addWidget(self.txt_customdosage)

        self.options_container.addLayout(self.ctr_option_4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radio1.setText(QCoreApplication.translate("Form", u"Take", None))
        self.label.setText(QCoreApplication.translate("Form", u"units,", None))
        self.label_2.setText(QCoreApplication.translate(
            "Form", u"times per day", None))
        self.radioButton_2.setText(
            QCoreApplication.translate("Form", u"Take", None))
        self.label_3.setText(
            QCoreApplication.translate("Form", u"up to", None))
        self.label_4.setText(QCoreApplication.translate(
            "Form", u"as needed, up to ", None))
        self.label_5.setText(QCoreApplication.translate(
            "Form", u"times per day", None))
        self.radioButton_3.setText(QCoreApplication.translate(
            "Form", u"Take according to regime", None))
        self.radioButton.setText(
            QCoreApplication.translate("Form", u"Custom:", None))
    # retranslateUi


def main():
    app = QApplication(sys.argv)
    window = Ui_Form()
    # window.show()
    app.exec_()


if __name__ == "__main__":
    main()
