#█▄▀ ▄▀█ █▀█ █ ▀█▀ █░█ ▄▀█
#█░█ █▀█ █▀▄ █ ░█░ █▀█ █▀█
#muhammetozmen
# -*- coding: utf-8 -*-

from PIL import Image ##Çeşitli imaj etkileşimi için Pillow kütüphanesi kullandım
import sqlite3 as sql #SQL olarak SQLite tercih ettim.
import random #Karakter rastgeleleştirmesi için kullandım.
import os #Klasör yaratma gibi işletim sistemsel işlevler
import shutil #Klasör silme gibi işletim sistemsel işlevler

#Kırpılan resmin konumu paths.db'ye SQL verisi olarak kaydeder
def import_db(letter,letter_path):
    global cursor, conn
    cursor.execute("INSERT INTO image_paths (letter, path) VALUES (?, ?)", (letter, letter_path))
    conn.commit()

#Bu fonksiyon ile SQL ve kırpılmış harfler boşaltılır
def clean_letters():
    #SQL table boşaltma
    global cursor
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='image_paths'")
    result= cursor.fetchone()
    if result:
        cursor.execute("DROP TABLE image_paths")
        print("Mevcut tablo siliniyor, yeni tablo yaratılacak.")
    else:
        print("Mevcut tablo yok, yeni tablo yaratılacak.")

    #Klasörü silip içinde boş klasör yaratma, böylece önceden kalma kırpılmış harfleri vs siler
    shutil.rmtree('./img/letters')
    os.mkdir('./img/letters')
    os.mkdir('./img/letters/alphabet')
    os.mkdir('./img/letters/symbols')
    os.mkdir('./img/letters/numbers')


#Bu fonksiyon ile img/workbench içinde bulunan işlenmek üzere doldurulmuş 'letter_table.png' üstündeki harfler çağrılma sırasına göre kırpılıyor  ve img/letters/alphabet klasörüne kaydediliyor
#coords: sol üst, sağ alt kordinatları
def crop_letter(i,letter,coords):
    path_letter_table= str(gui_val[6]) #BURAYI DAHA SONRA WORKBENCH DİYE DÜZELT
    image_obj = Image.open(path_letter_table)
    cropped_image = image_obj.crop(coords)
    if letter in alphabet_numbers: #Rakamlar için klasör kategorizasyonu
        cropped_image.save(f'./img/letters/numbers/{i}.png')
        letter_path= f'./img/letters/numbers/{i}.png'
        import_db(letter,letter_path)
    elif letter in alphabet_symbols: #Semboller için klasör kategorizasyonu
        cropped_image.save(f'./img/letters/symbols/{i}.png')
        letter_path= f'./img/letters/symbols/{i}.png'
        import_db(letter,letter_path)
    else: #Harfler için için klasör kategorizasyonu
        cropped_image.save(f'./img/letters/alphabet/{i}.png')
        letter_path= f'./img/letters/alphabet/{i}.png'
        import_db(letter,letter_path)

def foreground_randomizer(foreground): #Harflerin rastgeleleştirilmesi işlemi
    global gui_val
    rand_rotation= random.uniform(-int(gui_val[2]),int(gui_val[2]))
    foreground= foreground.rotate(rand_rotation) #Harflerin kullanıcı girdisine göre sağ/sol'a döndürülmesi
    width, height= foreground.size
    rand_size=random.uniform(1.0-(int(gui_val[3])/100),1.0+(int(gui_val[3])/100))
    new_width= int(width*rand_size)
    new_height= int(height*rand_size)
    foreground= foreground.resize((new_width,new_height), Image.ANTIALIAS) #Harflerin kullanıcı girdisine yatay ve dikey sıkıştırılması/genişletilmesi
    return foreground
    
def paste_letter(curr_path,x_background,y_background): #Kırpılan harflerin kağıda yapıştırılması işlemi
    global gui_val
    foreground= Image.open(curr_path).convert("RGBA")
    foreground= foreground.crop((5,5,40,40))
    alpha = foreground.split()[-1]
    alpha = alpha.point(lambda x: 255 if x > 0 else 0)
    foreground.putalpha(alpha)
    foreground= foreground_randomizer(foreground)
    resized_foreground= foreground.resize((int(gui_val[1]),int(gui_val[1])))
    background.paste(resized_foreground,(int(x_background),int(y_background)),resized_foreground)

def start_sql(): #SQL Başlatma
    global conn, cursor
    conn = sql.connect('paths.db')
    cursor= conn.cursor()
    clean_letters()
    cursor.execute("CREATE TABLE 'image_paths' (letter,path)") #Bu tabloyu harfleri ve konumlarını saklamak ve erişmek için kullanacağız

def crop_loop(): #Harf, numara ve sembolleri kırpma için dönen döngü
    global alphabet_all, coords, i
    for letter in alphabet_all:
        if letter=='x':
            coords[0]=-47
            coords[2]=1
            coords[1]+=98
            coords[3]+=98
        else:
            i+=1
            coords[0]+=49
            coords[2]+=49
            crop_letter(i,letter,coords)

def create_text(): #Yazıyı oluşturma işlemi, belli kordinatları sürekli olarak paste_letter() fonksiyonuna yollayarak sürekli resmi yapıştırır.
    global x_background, y_background, user_text, background, cursor, curr_path, gui_val, new_width
    x_background=20 #20
    y_background= 20 #8
    background= Image.open('./img/clean_temps/a4.png')
    for curr_letter in gui_val[4]:
        space_randomizer= random.uniform(0.2,0.7) #Boşluk miktarını rastgeleleştirir
        if curr_letter==' ' or curr_letter not in alphabet_all:
            if x_background + new_width >=2460 or curr_letter=='#':
                y_background+= new_width
                x_background=20
            else:
                x_background+=int(new_width*space_randomizer)
        else:
            cursor.execute("SELECT * FROM image_paths WHERE letter=(?)",(curr_letter)) #DataBase üzerinden harfin dizinini bulur
            curr_path= cursor.fetchone()
            paste_letter(curr_path[1],x_background,y_background)
        if gui_val[0]=='PNG' or 'JPEG':
            background.save(str(gui_val[7])+'/text.'+str(gui_val[0]))
        else:
            background.save(str(gui_val[7])+'/text.PNG')
        #Satır atlama
        if x_background+(new_width*2)>= 2460 or curr_letter=='#':
            x_background+=new_width
            if curr_letter!=' ' and curr_letter!='#':
                paste_letter('./img/letters/symbols/49.png',x_background,y_background)
            y_background+=new_width
            x_background=20
        else:
            x_background+=new_width

def convert_to_pdf(): #Eğer kullanıcı PDF olarak seçmiş ise PDF'e dönüştürür. (Pillow kütüphanesinden dolayı runtime error verebiliyor ama düzgün bir şekilde çalışmakta)
    global gui_val
    image_path= str(gui_val[7])+'/text.PNG'
    image = Image.open(image_path)
    pdf_path_with_extension = str(gui_val[7])+'/text.PDF'
    image.save(pdf_path_with_extension, "PDF", resolution=100.0)
    print("PDF'ye dönüştürüldü...")
    

def gui_start_trigger(): #Yazdır butonuna tıklayınca tetiklenecek fonksiyon, başla emri
    #uimenu'da kaydedilen değişkenleri main'e aktarır
    global gui_val, background, new_width, conn
    with open("gui_values.txt", "r") as dosya:
        gui_val = [satir.rstrip() for satir in dosya.readlines()]
        #gui_val= (0-selected_type, 1-font_size, 2-rotating_size, 3-resizing_size, 4-main_text_submit, 5-data_folder_path, 6-inputdata_folder_path, 7-data_folder_path2)
    new_width= int(gui_val[1])
    print("Arayüzden veriler alındı...")
    start_sql()
    print("SQL açıldı...")
    crop_loop()
    print("Harf kırpma işlemi bitti...")
    create_text()
    print("Yazı oluşturuldu...")
    convert_to_pdf()
    print(f"{gui_val[0]} dosya türü olarak kaydedildi")
    print("Tüm işlem başarıyla tamamlandı...")
    from uimenu import close_ui
    close_ui()
    print("Program Bitti")


#DEĞİŞKENLER
i=0 #Dosya adı
coords= [-47,51,-1,97] #0-x1,1-y1,2-x2,3-y2 tablo üzerindeki başlangıç koordinatları
alphabet_all= 'ABCÇDEFGĞHIİJxKLMNOÖPRSŞTUÜxVYZ0123456789x/"\'.,?!()-+;:xabcçdefgğhıijxklmnoöprsştuüxvyz%=><*[]{}~' #Döngü üstü harf kontrolü, x'ler alt satır temsil ediyor
alphabet_symbols= '/"\'.,?!()-+;:%=><*[]{}~' #Liste içindeki semboller
alphabet_numbers= '0123456789' #Liste içindeki numaralar
alphabet_words= 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz' #Liste içindeki harfler
letter_path= None #Son kırpılan harfin path'ini tutar
new_width= float() #Yeni genişlik değerini tutar



if __name__ == "__main__":
    from uimenu import start_gui #Kullanıcı arayüzünü ekler
    start_gui()
