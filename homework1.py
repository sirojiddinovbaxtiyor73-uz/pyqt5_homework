from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit

class calculator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.v_main_lay=QVBoxLayout()
        
        self.dis=QLineEdit()
        self.dis.setFixedHeight(50)
        self.dis.setStyleSheet("font-size: 20px")
        self.v_main_lay.addWidget(self.dis)
        
        self.btn_1=QPushButton("1")
        self.btn_2=QPushButton("2")
        self.btn_3=QPushButton("3")
        self.btn_4=QPushButton("4")
        self.btn_5=QPushButton("5")
        self.btn_6=QPushButton("6")
        self.btn_7=QPushButton("7")
        self.btn_8=QPushButton("8")
        self.btn_9=QPushButton("9")
        self.btn_0=QPushButton("0")
        self.btn_c=QPushButton("c")
        self.btn_p=QPushButton("+")
        self.btn_m=QPushButton("-")
        self.btn_k=QPushButton("*")
        self.btn_b=QPushButton("/")
        
        self.h_main_lay1=QHBoxLayout()
        self.h_main_lay1.addWidget(self.btn_1)
        self.h_main_lay1.addWidget(self.btn_2)
        self.h_main_lay1.addWidget(self.btn_3)
        self.h_main_lay1.addWidget(self.btn_4)
        self.h_main_lay1.addWidget(self.btn_5)
        
        self.h_main_lay2=QHBoxLayout()

        self.h_main_lay2.addWidget(self.btn_6)
        self.h_main_lay2.addWidget(self.btn_7)
        self.h_main_lay2.addWidget(self.btn_8)
        self.h_main_lay2.addWidget(self.btn_9)
        self.h_main_lay2.addWidget(self.btn_0)
        
        self.h_main_lay3=QHBoxLayout()

        self.h_main_lay3.addWidget(self.btn_c)
        self.h_main_lay3.addWidget(self.btn_p)
        self.h_main_lay3.addWidget(self.btn_m)
        self.h_main_lay3.addWidget(self.btn_k)
        self.h_main_lay3.addWidget(self.btn_b)

        self.v_main_lay.addLayout(self.h_main_lay1)
        self.v_main_lay.addLayout(self.h_main_lay2)
        self.v_main_lay.addLayout(self.h_main_lay3)
        
        self.btn_equal = QPushButton("=")
        self.btn_equal.setFixedHeight(45)
        self.btn_equal.setStyleSheet("font-size: 18px; background-color: lightgreen")
        self.btn_equal.clicked.connect(self.calculate)
        
        self.v_main_lay.addWidget(self.btn_equal)
        self.setLayout(self.v_main_lay)
        
        button=[
            self.btn_1,self.btn_2,self.btn_3,self.btn_4,self.btn_5,
            self.btn_6,self.btn_7,self.btn_8,self.btn_9,self.btn_0,
            self.btn_p,self.btn_m,self.btn_k,self.btn_b,self.btn_c
        ]
      
        for i in button:
            i.setFixedHeight(40)
            i.setStyleSheet("font-size: 15px;")
            i.clicked.connect(self.bosmoq)
            
    def bosmoq(self):
        sender_btn = self.sender()
        
        if sender_btn == self.btn_c:
            self.dis.clear()
        else:
            self.dis.setText(self.dis.text() + sender_btn.text())
    def calculate(self):
        try:
            natija = eval(self.dis.text())
            self.dis.setText(str(natija))
        except:
            self.dis.setText("Xato")
            
app=QApplication([])
win=calculator()
win.show()
app.exec_()