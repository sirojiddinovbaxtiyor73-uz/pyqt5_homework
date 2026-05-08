from PyQt5.QtWidgets import *
import json


class library(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('font-size: 25px')

        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.book = QLineEdit()
        self.book.setPlaceholderText("book name...")

        self.author = QLineEdit()
        self.author.setPlaceholderText("author name...")

        self.btn_find = QPushButton("find")
        self.btn_find.clicked.connect(self.find)

        self.btn_exit = QPushButton("exit")
        self.btn_exit.clicked.connect(exit)

        self.btn_add = QPushButton("add")
        self.btn_add.clicked.connect(self.add)

        self.lst = QListWidget()

        self.h_btn_lay.addWidget(self.btn_find)
        self.h_btn_lay.addWidget(self.btn_add)
        self.h_btn_lay.addWidget(self.btn_exit)

        self.v_main_lay.addWidget(self.book)
        self.v_main_lay.addWidget(self.author)
        self.v_main_lay.addLayout(self.h_btn_lay)
        self.v_main_lay.addWidget(self.lst)

        self.setLayout(self.v_main_lay)

    def find(self):

        self.lst.clear()

        book = self.book.text()
        author = self.author.text()

        if book and author:

            f = open("test.json", "r")

            books = json.load(f)

            f.close()

            found = False

            for i in books:

                if i["name"].lower() == book.lower() and i["author"].lower() == author.lower():

                    self.lst.addItem(f'{i["name"]}   |   {i["author"]}')

                    found = True

                    self.book.clear()
                    self.author.clear()

                    break

            if not found:
                QMessageBox.warning(self, "error", "bu kitob yo'q")

        else:
            QMessageBox.warning(self, "error", "barcha kataklarni to'ldiring!")

    def add(self):

        book_n = self.book.text()
        author_n = self.author.text()

        if book_n and author_n:

            f = open("test.json", "r+")

            books = json.load(f)

            bor = False

            for i in books:

                if i["name"].lower() == book_n.lower():

                    bor = True
                    break

            if bor:

                QMessageBox.warning(self, "error", "bu kitob mavjud")

            else:

                dct = {
                    "name": book_n,
                    "author": author_n
                }

                books.append(dct)

                f.seek(0)

                json.dump(books, f, indent=4)

                f.truncate()

                QMessageBox.information(self, "success", "kitob qo'shildi")

                self.book.clear()
                self.author.clear()

            f.close()

        else:
            QMessageBox.warning(self, "error", "barcha kataklarni to'ldiring!")


app = QApplication([])

win = library()

win.show()

app.exec_()