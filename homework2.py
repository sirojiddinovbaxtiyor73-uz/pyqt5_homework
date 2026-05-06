from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel, QCheckBox, QHBoxLayout,QLineEdit,QRadioButton,QComboBox
import json
class homework(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("font-size: 25px")
        self.v_main_lay=QVBoxLayout()
        self.h_main_lay=QHBoxLayout()
        
        self.edit_name = QLineEdit()
        self.edit_name.setPlaceholderText("Name...")  
        
        self.edit_second=QLineEdit()
        self.edit_second.setPlaceholderText("second...") 
        
        self.edit_age=QLineEdit()
        self.edit_age.setPlaceholderText("age...") 
        
        self.v_main_lay.addWidget(self.edit_name)
        self.v_main_lay.addWidget(self.edit_second)
        self.v_main_lay.addWidget(self.edit_age)
        
        self.jins=QLabel("JINS...")
        self.j1=QRadioButton("Male")
        self.j2=QRadioButton("Famale")
        self.h_main_lay.addWidget(self.jins)
        self.h_main_lay.addWidget(self.j1)
        self.h_main_lay.addWidget(self.j2)
        
        self.v_main_lay.addLayout(self.h_main_lay)
        
        self.shaxar=QHBoxLayout()
        self.tuman=QHBoxLayout()
        
        self.shaxar_label = QLabel("Shaxar:")
        self.shaxar_combo = QComboBox()
        
        self.shaxar_combo.addItems(["toshkent", "navoiy", "jizzah", "buxoro", "samarqand"])
        self.shaxar_combo.activated[str].connect(self.citys)
        
        self.tuman_label = QLabel()
        self.tuman_combo = QComboBox()
        
        self.data = {
            "toshkent": ["Chilonzor", "Yunusobod", "Mirzo Ulug'bek"],
            "navoiy": ["Navoiy sh.", "Zarafshon", "Karmana"],
            "jizzah": ["Jizzax sh.", "Sharof Rashidov", "G'allaorol"],
            "buxoro": ["Buxoro sh.", "G'ijduvon", "Kogon"],
            "samarqand": ["Samarqand sh.", "Urgut", "Toyloq"]
        }
        
        self.update_tumans(self.shaxar_combo.currentText())
        
        self.shaxar.addWidget(self.shaxar_label)
        self.shaxar.addWidget(self.shaxar_combo)
        self.tuman.addWidget(self.tuman_label)
        self.tuman.addWidget(self.tuman_combo)
        
        self.v_main_lay.addLayout(self.shaxar)
        self.v_main_lay.addLayout(self.tuman)
        
        self.tugma=QHBoxLayout()
        
        self.submit=QPushButton("Submit")
        self.submit.clicked.connect(self.submit_f)
        self.exit=QPushButton("Exit")
        self.exit.clicked.connect(exit)

        
        self.tugma.addWidget(self.submit)
        self.tugma.addWidget(self.exit)
        
        self.v_main_lay.addLayout(self.tugma)
        
        
        self.setLayout(self.v_main_lay)
        
    def citys(self, text):
        self.update_tumans(text)

    def update_tumans(self, shahar):
        self.tuman_combo.clear() 
        if shahar in self.data:
            self.tuman_combo.addItems(self.data[shahar])
    def submit_f(self):
        data = {}
        name = self.edit_name.text()
        second = self.edit_second.text()
        age = self.edit_age.text()

        if self.j1.isChecked():
            jins = "male"
        else:
            jins = "female"

        shaxar = self.shaxar_combo.currentText()
        tuman = self.tuman_combo.currentText()
        
        if name and second and age and jins and shaxar and tuman:

            data["name"] = name
            data["second"] = second
            data["age"] = age
            data["jins"] = jins
            data["shaxar"] = shaxar
            data["tuman"] = tuman
            
            f = open("test.json", "r")
            loaded = json.load(f)
            loaded.append(data)
            f.close()
            f = open("test.json", "w")
            json.dump(loaded, f, indent=4)
            self.msgc = QMessageBox()
            self.msgc.setText("Muvaffaqiyatli!")
            self.msgc.setIcon(QMessageBox.Information)
            self.edit_name.clear()
            self.edit_second.clear()
            self.edit_age.clear()
            self.tuman_combo.clear()
            self.msgc.exec_()
            f.close()

        else:
            self.msg = QMessageBox()
            self.msg.setText("Barchasini toldirishingiz kerak")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()
      
                

        
app = QApplication([])
win = homework()
win.show()
app.exec_()    
        