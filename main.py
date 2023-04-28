import psutil,datetime
import sys,threading,time
from ui_interface import *
from win10toast import ToastNotifier
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        net_io_counters = psutil.net_io_counters()
        self.start_bytes_sent = net_io_counters.bytes_sent
        self.start_bytes_recv = net_io_counters.bytes_recv
        self.sayac = False
        self.ilkez = True
        self.setting = QSettings('Uygulamam','uygulamaAyarlari')
        
        s=self.setting.value('internet')
        self.ui.doubleSpinBox.setValue(float(s))
        self.max2 = float(s)*1000
        #os.system("netsh interface show interface")
        #self.disable()
        self.prog = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerr)
        self.timer.start(1000)         
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        #loadJsonStyle(self, self.ui) 
        self.ui.doubleSpinBox.valueChanged.connect(self.spinn)
        self.ui.pushButton.clicked.connect(self.thread)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        
        self.ui.widget_2.mouseMoveEvent=self.MoveWindow
        self.ui.pushButton_3.clicked.connect(self.kapat)
        self.thread()
        self.show()
    def spinn(self,val):
        self.setting.setValue('internet',val)
        self.max2 = val*1000


    def MoveWindow(self,event):
        if self.isMaximized==False:
            pass
        self.move(self.pos()+event.globalPos()-self.clickPosition)
        self.clickPosition=event.globalPos()  


    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()

    def kapat(self):
        self.ui.pushButton.setChecked(False)
        self.timer.stop()
        app.exit()

    def thread(self):

        self.durum=self.ui.pushButton.isChecked()
        
        if self.durum != False:
            self.ui.pushButton.setText("Durdur")
            t=threading.Thread(target=self.scroll,args=("hh",))
            t.start()
        else:
            self.ui.pushButton.setText("Başlat")    
            self.durum=False
            #print(self.durum)
    def timerr(self):
        self.ui.progressBar.setValue(self.prog)

    def scroll(self,w):
        while self.durum:

            try:
                self.durum=self.ui.pushButton.isChecked()
                net_io_counters = psutil.net_io_counters()
                bytes_sent = net_io_counters.bytes_sent
                bytes_recv = net_io_counters.bytes_recv
                connections = psutil.net_connections(kind='inet')
                         
                total_bytes_sent = bytes_sent - self.start_bytes_sent
                total_bytes_recv = bytes_recv - self.start_bytes_recv
                total_data_used = total_bytes_sent + total_bytes_recv
                total_data_used_MB = total_data_used / 1000000
                self.ui.label.setText(f"Giden Veri (MB): {bytes_sent/1000000:.2f}")
                self.ui.label_2.setText(f"Gelen Veri (MB): {bytes_recv/1000000:.2f}")
                self.ui.label_3.setText(f"Toplam Harcanan Veri (MB): {total_data_used_MB:.2f}")
                
                s=self.setting.value('internet')                
                    #self.ui.progressBar.setValue(deger)
                if s!='0':
                    toplam = total_data_used_MB/float(s)*1000
                    #self.ui.progressBar.setValue(toplam)
                    #§print(float(s)*1000,toplam,total_data_used_MB)
                    self.prog  =  total_data_used_MB *100 / self.max2
                    if self.prog >100:
                        self.prog =100

                    if self.prog>=100:
                        toaster = ToastNotifier()
                        d= datetime.datetime.now().minute
                        if self.ilkez:
                            toaster.show_toast("internet kullanım uyarısı", f"belirlenen internet limiti aşıldı \ninternet: {total_data_used_MB:.2f}", duration=3)
                            self.ilkez =False

                        if self.sayac ==False and d %2==0:
                            toaster.show_toast("internet kullanım uyarısı", f"belirlenen internet limiti aşıldı \nintentet: {total_data_used_MB:.2f}", duration=3)
                            self.sayac=True

                        if d %2 != 0:
                            self.sayac=False
                        
            except Exception as hata:
                print("hata",hata)  
            time.sleep(0.1)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
