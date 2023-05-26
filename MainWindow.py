import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QWidget, QLabel, QApplication, QBoxLayout, QHBoxLayout, QVBoxLayout, QPushButton, QListWidget, QSplitter, QFrame,
    QTextEdit, QButtonGroup, QStyle, QStackedWidget, QListWidgetItem, QToolButton, QStyledItemDelegate, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPen, QColor, QPalette
        
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FIH-ML-tool')
        
        main_layout = QHBoxLayout(self)
        
        step_widget = QWidget()
        step_layout = QVBoxLayout(step_widget)
        btn_name = ['Step1', 'Step2', 'Step3']
        self.step_btn = []
        for i in range(len(btn_name)):
            btn = QPushButton(btn_name[i])
            btn.clicked.connect(lambda state, x=i: self.widget_stack.setCurrentIndex(x))
            step_layout.addWidget(btn)
        
        self.widget_stack = QStackedWidget()
        self.widget_stack.addWidget(QTextEdit('Step1'))
        self.widget_stack.addWidget(QTextEdit('Step2'))
        self.widget_stack.addWidget(QTextEdit('Step3'))
        
        splitter = QSplitter()
        splitter.setOrientation(Qt.Horizontal)
        splitter.addWidget(step_widget)
        splitter.addWidget(self.widget_stack)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 6)
        main_layout.addWidget(splitter)

if __name__ == '__main__':
    app = QApplication([])
    widget = MainWindow()
    widget.showMaximized()
    app.exec_()