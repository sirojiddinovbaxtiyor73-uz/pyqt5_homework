import json

from PyQt5.QtWidgets import *

class mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,300)
        self.setStyleSheet("font-size:25px")
        self.v_main_lay=QVBoxLayout()
        
        self.edit_text=QLineEdit()
        self.edit_text.setPlaceholderText("Task nomi...")
        
        self.edit_status=QLineEdit()
        self.edit_status.setPlaceholderText("Status(Done/Pending)...")
        
        self.edit_qidiruv=QLineEdit()
        self.edit_qidiruv.setPlaceholderText("Qidiruv...")
        
        self.btn_qoshish=QPushButton("Qo'shish")
        self.btn_qoshish.clicked.connect(self.qoshish)
        self.btn_qidirish=QPushButton("Qidirish")
        self.btn_qidirish.clicked.connect(self.qidirish)
        self.btn_umumiy=QPushButton("Umumiy son")
        self.btn_umumiy.clicked.connect(self.umumiy)
        
        
        self.lbl=QLabel("Jami tasklar: 0")
        
        self.v_main_lay.addWidget(self.edit_text)
        self.v_main_lay.addWidget(self.edit_status)
        self.v_main_lay.addWidget(self.edit_qidiruv)
        self.v_main_lay.addWidget(self.btn_qoshish)
        self.v_main_lay.addWidget(self.btn_qidirish)
        self.v_main_lay.addWidget(self.btn_umumiy)
        self.v_main_lay.addWidget(self.lbl)
        
        self.setLayout(self.v_main_lay)
        
        
    def qoshish(self):
        task = self.edit_text.text()
        status = self.edit_status.text()
    
        try:
                f=open("lugat.json",'r+') 
                new = json.load(f)
        except :
            new = []
        if task and status:
            if status.lower() == 'done' or status.lower() == 'pending':
                bor = False
                for i in new:
                    if task == i["task"]:
                        bor = True
                        break
                    
                if not bor:
                    dct = {
                        "task": task,
                        "status": status
                    }
                    new.append(dct)
                    f.seek(0)
                    json.dump(new, f, indent=4)
                    QMessageBox.information(self, "ok", "Task qo'shildi")
                
                    count = len(new)
                    self.lbl.setText(f"jami tasklar: {count}")
                else:
                    QMessageBox.warning(self, "xato", "Bu task mavjud")
            else:
                QMessageBox.warning(self, "xato", "Status noto'g'ri!")
    
        self.edit_text.clear()
        self.edit_status.clear()
        
        
    def qidirish(self):
        qidiruv=self.edit_qidiruv.text()
        
        if qidiruv:
            f=open("lugat.json")
            search=json.load(f)
            topildi=False
            for i in search:
                if qidiruv.lower() in i['task'].lower():
                    QMessageBox.information(self,"topildi",f"task: {i['task']}\nstatus: {i['status']}")
                    topildi=True
                    break
                    
            if not topildi:
                QMessageBox.information(self,"natija","Topilmadi")
            self.edit_qidiruv.clear()        
        else:
            QMessageBox.warning(self,"Habar","Qidiruvga so'z yozing")
            
            
    def umumiy(self):
        f=open("lugat.json")
        data=json.load(f)
        umumiy_s=len(data)
        QMessageBox.information(self,"umumiy",f"Jami tasklar soni: {umumiy_s}")
  
app=QApplication([])
win=mywindow()
win.show()
app.exec_()
        
        