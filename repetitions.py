#!/usr/bin/python3

from PyQt6.QtWidgets import QApplication

import fenetre


# Application Qt
app = QApplication([])
fenetre = fenetre.Fenetre()
fenetre.show()
app.exec()
