# Copyright (C) 2024  Darko Milosevic

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

    
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QTextEdit, QFileDialog, QComboBox, QMessageBox, QLineEdit)
from PyQt5.QtCore import Qt
from yuconv import YuConverter
import sys

class TransliterationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YuConv GUI Application")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.tabs = []
        self.create_tabs()

    def create_tabs(self):
        self.layout.addWidget(self.create_text_transliteration_tab())
        self.layout.addWidget(self.create_file_transliteration_tab())
        self.layout.addWidget(self.create_word_transliteration_tab())

    def create_text_transliteration_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.text_input = QTextEdit()
        layout.addWidget(QLabel("Input Text:"))
        layout.addWidget(self.text_input)

        self.text_mode = QComboBox()
        self.text_mode.addItems(["LatinToCyrillic", "CyrillicToLatin"])
        layout.addWidget(QLabel("Mode:"))
        layout.addWidget(self.text_mode)

        btn = QPushButton("Transliterate")
        btn.clicked.connect(self.transliterate_text)
        layout.addWidget(btn)

        tab.setLayout(layout)
        self.tabs.append(tab)
        return tab

    def transliterate_text(self):
        mode = self.text_mode.currentText()
        text = self.text_input.toPlainText()
        yu_converter = YuConverter()

        try:
            if mode == "LatinToCyrillic":
                result = yu_converter.transliterate_text(text, "lat-to-cyr")
            else:
                result = yu_converter.transliterate_text(text, "cyr-to-lat")
            self.text_input.setText(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def create_file_transliteration_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.input_file = QLineEdit()
        input_btn = QPushButton("Browse Input File")
        input_btn.clicked.connect(self.browse_input_file)
        
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_file)
        input_layout.addWidget(input_btn)
        layout.addLayout(input_layout)

        self.output_file = QLineEdit()
        output_btn = QPushButton("Browse Output File")
        output_btn.clicked.connect(self.browse_output_file)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_file)
        output_layout.addWidget(output_btn)
        layout.addLayout(output_layout)

        self.file_mode = QComboBox()
        self.file_mode.addItems(["LatinToCyrillic", "CyrillicToLatin"])
        layout.addWidget(QLabel("Mode:"))
        layout.addWidget(self.file_mode)

        btn = QPushButton("Transliterate")
        btn.clicked.connect(self.transliterate_file)
        layout.addWidget(btn)

        tab.setLayout(layout)
        self.tabs.append(tab)
        return tab

    def browse_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Input File")
        if file_path:
            self.input_file.setText(file_path)

    def browse_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Select Output File")
        if file_path:
            self.output_file.setText(file_path)

    def transliterate_file(self):
        mode = self.file_mode.currentText()
        input_path = self.input_file.text()
        output_path = self.output_file.text()
        yu_converter = YuConverter()

        try:
            if mode == "LatinToCyrillic":
                yu_converter.transliterate_text_file(input_path, output_path, "lat-to-cyr")
            else:
                yu_converter.transliterate_text_file(input_path, output_path, "cyr-to-lat")
            QMessageBox.information(self, "Success", "Transliteration complete.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def create_word_transliteration_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.word_input_file = QLineEdit()
        word_input_btn = QPushButton("Browse Word Input File")
        word_input_btn.clicked.connect(self.browse_word_input_file)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.word_input_file)
        input_layout.addWidget(word_input_btn)
        layout.addLayout(input_layout)

        self.word_output_file = QLineEdit()
        word_output_btn = QPushButton("Browse Word Output File")
        word_output_btn.clicked.connect(self.browse_word_output_file)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.word_output_file)
        output_layout.addWidget(word_output_btn)
        layout.addLayout(output_layout)

        self.word_mode = QComboBox()
        self.word_mode.addItems(["LatinToCyrillic", "CyrillicToLatin"])
        layout.addWidget(QLabel("Mode:"))
        layout.addWidget(self.word_mode)

        btn = QPushButton("Transliterate")
        btn.clicked.connect(self.transliterate_word)
        layout.addWidget(btn)

        tab.setLayout(layout)
        self.tabs.append(tab)
        return tab

    def browse_word_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Word Input File", filter="Word Files (*.docx)")
        if file_path:
            self.word_input_file.setText(file_path)

    def browse_word_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Select Word Output File", filter="Word Files (*.docx)")
        if file_path:
            self.word_output_file.setText(file_path)

    def transliterate_word(self):
        mode = self.word_mode.currentText()
        input_path = self.word_input_file.text()
        output_path = self.word_output_file.text()
        yu_converter = YuConverter()

        try:
            if mode == "LatinToCyrillic":
                yu_converter.transliterate_word_document(input_path, output_path, "lat-to-cyr")
            else:
                yu_converter.transliterate_word_document(input_path, output_path, "cyr-to-lat")
            QMessageBox.information(self, "Success", "Transliteration complete.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TransliterationApp()
    main_window.show()
    sys.exit(app.exec_())
