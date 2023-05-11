# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
import shutil
import os

current_dir = os.getcwd() #Programın çalıştığı dosyayı belirler.

class Ui_page_main(object):
    def setupUi(self, page_main):
        page_main.setObjectName("page_main")
        page_main.resize(800, 600)
        page_main.setMinimumSize(QtCore.QSize(800, 600))
        page_main.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/parwrite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        page_main.setWindowIcon(icon)
        page_main.setWindowOpacity(1.0)
        page_main.setStyleSheet("background-image: url('./ui/appicons/paper_wallpaper.png');")
        self.logo_label = QtWidgets.QLabel(page_main)
        self.logo_label.setGeometry(QtCore.QRect(30, 20, 161, 161))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        self.logo_label.setFont(font)
        self.logo_label.setStyleSheet("image: url('./ui/appicons/parwrite.png');")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.logotext_label = QtWidgets.QLabel(page_main)
        self.logotext_label.setGeometry(QtCore.QRect(200, 30, 551, 101))
        font = QtGui.QFont()
        font.setFamily("Baby Doll")
        font.setPointSize(90)
        font.setBold(True)
        font.setItalic(False)
        self.logotext_label.setFont(font)
        self.logotext_label.setStyleSheet("font: 700 90pt \"Baby Doll\";\n"
        "border-style:outset;\n"
        "color: rgb(165, 29, 45);")
        self.logotext_label.setObjectName("logotext_label")
        self.tabWidget = QtWidgets.QTabWidget(page_main)
        self.tabWidget.setGeometry(QtCore.QRect(20, 200, 761, 381))
        self.tabWidget.setStyleSheet("background-color: rgb(192, 191, 188);\n"
        "font: 11pt \"Baby Doll\";\n"
        "color: rgb(36, 31, 49);")
        self.tabWidget.setObjectName("tabWidget")
        self.input_table = QtWidgets.QWidget()
        self.input_table.setFocusPolicy(QtCore.Qt.TabFocus)
        self.input_table.setObjectName("input_table")
        self.textinputdesc_label = QtWidgets.QLabel(self.input_table)
        self.textinputdesc_label.setGeometry(QtCore.QRect(20, 10, 301, 18))
        self.textinputdesc_label.setStyleSheet("color: rgb(165, 29, 45);\n"
        "font: 700 13pt \"Morning Breeze\";")
        self.textinputdesc_label.setObjectName("textinputdesc_label")
        self.tobeconv_text = QtWidgets.QPlainTextEdit(self.input_table)
        self.tobeconv_text.setGeometry(QtCore.QRect(20, 60, 721, 241))
        self.tobeconv_text.setStyleSheet("color: rgb(0, 0, 0);\n"
        "font: 300 13pt \"Morning Breeze\";")
        self.tobeconv_text.setObjectName("tobeconv_text")
        self.textinputdesc_label_2 = QtWidgets.QLabel(self.input_table)
        self.textinputdesc_label_2.setGeometry(QtCore.QRect(20, 30, 711, 18))
        self.textinputdesc_label_2.setStyleSheet("color: rgb(36, 31, 49);\n"
        "font: 13pt \"Morning Breeze\";")
        self.textinputdesc_label_2.setObjectName("textinputdesc_label_2")
        
        #ENTER TEXT BUTTON
        self.entertext_button = QtWidgets.QPushButton(self.input_table)
        self.entertext_button.setGeometry(QtCore.QRect(630, 310, 111, 31))
        self.entertext_button.setStyleSheet("")
        self.entertext_button.setObjectName("entertext_button")
        self.entertext_button.clicked.connect(self.entertext_button_clicked) #Tıklama tetik

        self.tabWidget.addTab(self.input_table, "")
        self.output_table = QtWidgets.QWidget()
        self.output_table.setObjectName("output_table")
        self.data_sample_group = QtWidgets.QGroupBox(self.output_table)
        self.data_sample_group.setGeometry(QtCore.QRect(10, 10, 351, 311))
        self.data_sample_group.setStyleSheet("font: 700 11pt \"Morning Breeze\";")
        self.data_sample_group.setObjectName("data_sample_group")
        self.textinputdesc_label_3 = QtWidgets.QLabel(self.data_sample_group)
        self.textinputdesc_label_3.setGeometry(QtCore.QRect(10, 50, 301, 18))
        self.textinputdesc_label_3.setStyleSheet("color: rgb(165, 29, 45);\n"
        "font: 700 11pt \"Morning Breeze\";")
        self.textinputdesc_label_3.setObjectName("textinputdesc_label_3")
        self.data_path = QtWidgets.QLineEdit(self.data_sample_group)
        self.data_path.setGeometry(QtCore.QRect(10, 70, 211, 26))
        self.data_path.setObjectName("data_path")

        #DATA PATH ARAMA (KLASÖR)
        self.data_path_browse = QtWidgets.QPushButton(self.data_sample_group)
        self.data_path_browse.setGeometry(QtCore.QRect(230, 70, 81, 26))
        self.data_path_browse.setObjectName("data_path_browse")
        self.data_path_browse.clicked.connect(self.data_path_browse_button_clicked) #Tıklama tetik

        #DATA PATH'A DOSYA OLUŞTUR
        self.premade_data_path = QtWidgets.QCheckBox(self.data_sample_group)
        self.premade_data_path.setGeometry(QtCore.QRect(10, 100, 311, 24))
        self.premade_data_path.setObjectName("premade_data_path")

        #DATA PATH ARAMA (DOLDURULMUŞ DOSYA)
        self.inputdata_path_browse = QtWidgets.QPushButton(self.data_sample_group)
        self.inputdata_path_browse.setGeometry(QtCore.QRect(230, 170, 81, 26))
        self.inputdata_path_browse.setObjectName("inputdata_path_browse")
        self.inputdata_path_browse.clicked.connect(self.inputdata_path_browse_button_clicked) #Tıklama tetik

        self.textinputdesc_label_4 = QtWidgets.QLabel(self.data_sample_group)
        self.textinputdesc_label_4.setGeometry(QtCore.QRect(10, 150, 301, 18))
        self.textinputdesc_label_4.setStyleSheet("color: rgb(165, 29, 45);\n"
        "font: 700 11pt \"Morning Breeze\";")
        self.textinputdesc_label_4.setObjectName("textinputdesc_label_4")
        self.inputdata_path = QtWidgets.QLineEdit(self.data_sample_group)
        self.inputdata_path.setGeometry(QtCore.QRect(10, 170, 211, 26))
        self.inputdata_path.setObjectName("inputdata_path")
        self.comboBox = QtWidgets.QComboBox(self.data_sample_group)
        self.comboBox.setGeometry(QtCore.QRect(230, 280, 81, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textinputdesc_label_5 = QtWidgets.QLabel(self.data_sample_group)
        self.textinputdesc_label_5.setGeometry(QtCore.QRect(10, 230, 301, 18))
        self.textinputdesc_label_5.setStyleSheet("color: rgb(165, 29, 45);\n"
        "font: 700 11pt \"Morning Breeze\";")
        self.textinputdesc_label_5.setObjectName("textinputdesc_label_5")

        #DATA PATH ARAMA 2 (KAYIT NOKTASI)
        self.data_path_browse_2 = QtWidgets.QPushButton(self.data_sample_group)
        self.data_path_browse_2.setGeometry(QtCore.QRect(230, 250, 81, 26))
        self.data_path_browse_2.setObjectName("data_path_browse_2")
        self.data_path_browse_2.clicked.connect(self.data_path_browse_button_2_clicked) #Tıklama tetik


        self.textinputdesc_label_6 = QtWidgets.QLabel(self.data_sample_group)
        self.textinputdesc_label_6.setGeometry(QtCore.QRect(10, 280, 201, 21))
        self.textinputdesc_label_6.setStyleSheet("color: rgb(36, 31, 49);\n"
        "font: 700 11pt \"Morning Breeze\";")
        self.textinputdesc_label_6.setObjectName("textinputdesc_label_6")
        self.data_path_2 = QtWidgets.QLineEdit(self.data_sample_group)
        self.data_path_2.setGeometry(QtCore.QRect(10, 250, 211, 26))
        self.data_path_2.setObjectName("data_path_2")
        self.data_save_group = QtWidgets.QGroupBox(self.output_table)
        self.data_save_group.setGeometry(QtCore.QRect(390, 10, 351, 311))
        self.data_save_group.setStyleSheet("font: 700 11pt \"Morning Breeze\";")
        self.data_save_group.setObjectName("data_save_group")
        self.textinputdesc_label_7 = QtWidgets.QLabel(self.data_save_group)
        self.textinputdesc_label_7.setGeometry(QtCore.QRect(20, 50, 201, 21))
        self.textinputdesc_label_7.setStyleSheet("color: rgb(36, 31, 49);\n"
        "font: 700 11pt \"Morning Breeze\";")
        self.textinputdesc_label_7.setObjectName("textinputdesc_label_7")

        #FONT BÜYÜKLÜĞÜ
        self.font_val = QtWidgets.QSpinBox(self.data_save_group)
        self.font_val.setGeometry(QtCore.QRect(180, 40, 41, 41))
        self.font_val.setMinimum(10)
        self.font_val.setMaximum(100)
        self.font_val.setProperty("value", 35)
        self.font_val.setObjectName("font_val")

        self.textinputdesc_label_8 = QtWidgets.QLabel(self.data_save_group)
        self.textinputdesc_label_8.setGeometry(QtCore.QRect(20, 110, 201, 21))
        self.textinputdesc_label_8.setStyleSheet("color: rgb(36, 31, 49);\n"
        "font: 700 11pt \"Morning Breeze\";")
        self.textinputdesc_label_8.setObjectName("textinputdesc_label_8")

        #DÖNME BÜYÜKLÜĞÜ
        self.rotate_val = QtWidgets.QSpinBox(self.data_save_group)
        self.rotate_val.setGeometry(QtCore.QRect(180, 100, 41, 41))
        self.rotate_val.setMinimum(0)
        self.rotate_val.setMaximum(90)
        self.rotate_val.setProperty("value", 10)
        self.rotate_val.setObjectName("rotate_val")


        self.textinputdesc_label_9 = QtWidgets.QLabel(self.data_save_group)
        self.textinputdesc_label_9.setGeometry(QtCore.QRect(20, 170, 171, 21))
        self.textinputdesc_label_9.setStyleSheet("color: rgb(36, 31, 49);\n"
        "font: 700 11pt \"Morning Breeze\";")
        self.textinputdesc_label_9.setObjectName("textinputdesc_label_9")

        #BÜYÜLTME/KÜÇÜLTME BÜYÜKLÜĞÜ
        self.resize_val = QtWidgets.QSpinBox(self.data_save_group)
        self.resize_val.setGeometry(QtCore.QRect(180, 160, 41, 41))
        self.resize_val.setMinimum(0)
        self.resize_val.setMaximum(90)
        self.resize_val.setProperty("value", 10)
        self.resize_val.setObjectName("resize_val")

        self.defaultval_label = QtWidgets.QLabel(self.data_save_group)
        self.defaultval_label.setGeometry(QtCore.QRect(230, 50, 91, 21))
        self.defaultval_label.setStyleSheet("color: rgb(154, 153, 150);\n"
        "font: italic 13pt \"Morning Breeze\";")
        self.defaultval_label.setObjectName("defaultval_label")
        self.defaultval_label_2 = QtWidgets.QLabel(self.data_save_group)
        self.defaultval_label_2.setGeometry(QtCore.QRect(230, 110, 91, 21))
        self.defaultval_label_2.setStyleSheet("color: rgb(154, 153, 150);\n"
        "font: italic 13pt \"Morning Breeze\";")
        self.defaultval_label_2.setObjectName("defaultval_label_2")
        self.defaultval_label_3 = QtWidgets.QLabel(self.data_save_group)
        self.defaultval_label_3.setGeometry(QtCore.QRect(230, 170, 91, 21))
        self.defaultval_label_3.setStyleSheet("color: rgb(154, 153, 150);\n"
        "font: italic 13pt \"Morning Breeze\";")
        self.defaultval_label_3.setObjectName("defaultval_label_3")
        self.textinputdesc_label_10 = QtWidgets.QLabel(self.data_save_group)
        self.textinputdesc_label_10.setGeometry(QtCore.QRect(20, 240, 141, 51))
        self.textinputdesc_label_10.setStyleSheet("color: rgb(165, 29, 45);\n"
        "font: 700 16pt \"Morning Breeze\";")
        self.textinputdesc_label_10.setObjectName("textinputdesc_label_10")

        #YAZDIR BUTONU
        self.pushButton = QtWidgets.QPushButton(self.data_save_group)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 91, 51))
        self.pushButton.setStyleSheet("font: 700 17pt \"Morning Breeze\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.print_clicked) #Tıklama tetik


        self.tabWidget.addTab(self.output_table, "")
        self.about_group = QtWidgets.QWidget()
        self.about_group.setObjectName("about_group")
        self.groupBox = QtWidgets.QGroupBox(self.about_group)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 321))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 331, 281))
        self.label.setStyleSheet("font: 300 14pt \"Morning Breeze\";")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.about_group)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 10, 361, 321))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 331, 281))
        self.label_2.setStyleSheet("font: 300 14pt \"Morning Breeze\";")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.about_group, "")
        self.defaultval_label_4 = QtWidgets.QLabel(page_main)
        self.defaultval_label_4.setGeometry(QtCore.QRect(610, 140, 141, 21))
        self.defaultval_label_4.setStyleSheet("color: rgb(154, 153, 150);\n"
        "font: italic 13pt \"Morning Breeze\";")
        self.defaultval_label_4.setObjectName("defaultval_label_4")
        self.defaultval_label_5 = QtWidgets.QLabel(page_main)
        self.defaultval_label_5.setGeometry(QtCore.QRect(670, 160, 81, 21))
        self.defaultval_label_5.setStyleSheet("font: italic 13pt \"Morning Breeze\";\n"
        "color: rgb(192, 191, 188);")
        self.defaultval_label_5.setObjectName("defaultval_label_5")

        self.retranslateUi(page_main)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(page_main)

#BUTONLARA ATANAN GÖREVLER BURADAN SONRA BAŞLIYOR
    def entertext_button_clicked(self):
        global main_text_submit
        main_text_submit= ''
        satirlar= ui.tobeconv_text.toPlainText().splitlines()
        for satir in satirlar:
            main_text_submit+=satir+'#'
        print("Yazı kaydedildi")

    def data_path_browse_button_clicked(self):
        global data_folder_path
        dialog = QtWidgets.QFileDialog()
        data_folder_path = dialog.getExistingDirectory(None, "Select Folder")
        self.data_path.setText(data_folder_path)
        if self.premade_data_path.isChecked() and data_folder_path!='':
            shutil.copy(current_dir+'/img/testdata/letter_table.png', data_folder_path) #Doldurulmuş kağıt oluşturur
        elif data_folder_path!='':
            shutil.copy(current_dir+'/img/clean_temps/letter_table.png',data_folder_path) #Boş kağıt oluşturur
            
    def inputdata_path_browse_button_clicked(self):
        global inputdata_folder_path
        dialog = QtWidgets.QFileDialog()
        dialog.setDirectory('/path/to/starting/directory')
        inputdata_folder_path, _ = dialog.getOpenFileName(None, "Select File", "", "Resim Dosyası (*.png)")
        self.inputdata_path.setText(inputdata_folder_path)

    def data_path_browse_button_2_clicked(self):
        global data_folder_path2
        dialog = QtWidgets.QFileDialog()
        data_folder_path2 = dialog.getExistingDirectory(None, "Select Folder")
        self.data_path_2.setText(data_folder_path2)

    def print_clicked(self): #YAZDIRMA ANA BUTON
        global selected_type, font_size, rotating_size, resizing_size
        selected_type = self.comboBox.currentText() #Kayededilecek tip
        font_size = self.font_val.value() #Font büyüklüğü
        rotating_size = self.rotate_val.value() #Dönme oranı
        resizing_size= self.resize_val.value() #Büyüme-küçülme oranı
        global all_gui_values
        all_gui_values= (selected_type, font_size, rotating_size, resizing_size, main_text_submit, data_folder_path,inputdata_folder_path, data_folder_path2)
        save_txt()
        from main import gui_start_trigger
        gui_start_trigger()

    def retranslateUi(self, page_main): #Translate kısmı
        _translate = QtCore.QCoreApplication.translate
        page_main.setWindowTitle(_translate("page_main", "Parwrite"))
        self.logotext_label.setText(_translate("page_main", "PARWRITE"))
        self.textinputdesc_label.setText(_translate("page_main", "Dönüştürülecek Yazı:"))
        self.tobeconv_text.setPlainText(_translate("page_main", "Buraya ödevinizi, mektubunuzu ya da şiirinizi girin!"))
        self.textinputdesc_label_2.setText(_translate("page_main", "Buraya el yazısına dönüştürülecek yazıyı yazın. Satır sonlarını pas geçin, onu program halleder!"))
        self.entertext_button.setText(_translate("page_main", "Yazıyı Kaydet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.input_table), _translate("page_main", "Girilecek Yazı"))
        self.data_sample_group.setTitle(_translate("page_main", "  Kayıt Bilgileri"))
        self.textinputdesc_label_3.setText(_translate("page_main", "Harf tablosu oluştur:"))
        self.data_path.setText(_translate("page_main", "./img/workbench"))
        self.data_path_browse.setText(_translate("page_main", "Dizin Seç"))
        self.premade_data_path.setText(_translate("page_main", "Doldurulmuş Tablo Oluştur (Deneme Amaçlı)"))
        self.inputdata_path_browse.setText(_translate("page_main", "Dosya Seç"))
        self.textinputdesc_label_4.setText(_translate("page_main", "Doldurulmuş harf tablosu seç:"))
        self.inputdata_path.setText(_translate("page_main", "./img/workbench"))

        #SAVE TYPE
        self.comboBox.setItemText(0, _translate("page_main", "PNG"))
        self.comboBox.setItemText(1, _translate("page_main", "PDF"))
        self.comboBox.setItemText(2, _translate("page_main", "JPEG"))
        selected_type = self.comboBox.currentText()

        self.textinputdesc_label_5.setText(_translate("page_main", "Dosyanın kayıt noktası:"))
        self.data_path_browse_2.setText(_translate("page_main", "Dizin Seç"))
        self.textinputdesc_label_6.setText(_translate("page_main", "Dosya\'nın kaydedilme biçimi:"))
        self.data_path_2.setText(_translate("page_main", "./img/workbench"))
        self.data_save_group.setTitle(_translate("page_main", "  Yazma Biçimleri"))
        self.textinputdesc_label_7.setText(_translate("page_main", "Font Büyüklüğü:"))
        self.textinputdesc_label_8.setText(_translate("page_main", "Dönüş Rastgeleliği:"))
        self.textinputdesc_label_9.setText(_translate("page_main", "Sıkıştırma Rastgeleliği:"))
        self.defaultval_label.setText(_translate("page_main", "Varsayılan: 35"))
        self.defaultval_label_2.setText(_translate("page_main", "Varsayılan: 10"))
        self.defaultval_label_3.setText(_translate("page_main", "Varsayılan: 10"))
        self.textinputdesc_label_10.setText(_translate("page_main", "Yazıyı oluştur:"))
        self.pushButton.setText(_translate("page_main", "Yazdır"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.output_table), _translate("page_main", "Yazdırma Ayarları"))
        self.groupBox.setTitle(_translate("page_main", "  Program Hakkında"))
        self.label.setText(_translate("page_main", "Parwrite, kullanıcının elle girdiği tablo verilerini kırparak bütün bu harfleri tekrar girilen yazıyı el yazısına dönüştürmek için kullanılabilecek bir programdır. Program, İskenderun Teknik Üniversitesi öğrencisi Muhammet Özmen tarafından Nesne Tabanlı Görsel Programlama Dersi için yapılmıştır."))
        self.groupBox_2.setTitle(_translate("page_main", "  Programcı Hakkında"))
        self.label_2.setText(_translate("page_main", "Muhammet Özmen İSTE Bil. Müh. 2. sınıf öğrencisidir. Şu anda özellikle Python programlama diliyle uğraşmaktadır."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_group), _translate("page_main", "Hakkında"))
        self.defaultval_label_4.setText(_translate("page_main", "by Muhammet Özmen"))
        self.defaultval_label_5.setText(_translate("page_main", "AKA Karitha"))


def close_ui():
    import sys
    sys.exit()

def save_txt():
        global all_gui_values
        filename = "gui_values.txt"
        with open(filename, "w") as file:
            file.write("")
        with open(filename, "a") as file:
            for line in all_gui_values:
                string = str(line)+"\n"
                file.write(string)

#DEFAULT DEĞERLER
all_gui_values= tuple()
selected_type= 'PNG'
font_size= 35
rotating_size= 10
resizing_size= 10
main_text_submit= 'Metin boş bırakıldı'
data_folder_path= current_dir+'/img/tesdata'
inputdata_folder_path= current_dir + '/img/testdata/letter_table.png'
data_folder_path2= current_dir + '/img/workbench'

def start_gui():
    global app, page_main, ui
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page_main = QtWidgets.QWidget()
    ui = Ui_page_main()
    ui.setupUi(page_main)
    page_main.show()
    sys.exit(app.exec_())



#main'e yollanacaklar değişkenler
# main_text_submit GİRİLEN YAZI
# data_folder_path YENİ TABLO OLUŞTURMA YERİ
# input_data_folder_path DOLU TABLO YERİ
# data_folder_path2 DOSYANIN OLUŞTURULACAĞI YER