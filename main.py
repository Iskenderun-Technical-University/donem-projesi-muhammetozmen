#█▄▀ ▄▀█ █▀█ █ ▀█▀ █░█ ▄▀█
#█░█ █▀█ █▀▄ █ ░█░ █▀█ █▀█
#muhammetozmen

from PIL import Image ##Çeşitli imaj etkileşimi için Pillow kütüphanesi kullandım
import sqlite3 as sql #SQL olarak SQLite tercih ettim.
import os #Klasör yaratma gibi işletim sistemsel işlevler
import shutil #Klasör silme gibi işletim sistemsel işlevler

#Kırpılan resmin konumu paths.db'ye SQL verisi olarak kaydeder
def import_db(letter,letter_path):
    cursor.execute("INSERT INTO image_paths (letter, path) VALUES (?, ?)", (letter, letter_path))
    conn.commit()

#Bu fonksiyon ile SQL ve kırpılmış harfler boşaltılır
def clean_letters():
    #SQL table boşaltma
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='image_paths'")
    result= cursor.fetchone()
    if result:
        cursor.execute("DROP TABLE image_paths")
        print("Mevcut tablo siliniyor, yeni tablo yaratılacak.")
    else:
        print("Mevcut tablo yok, yeni tablo yaratılacak.")

    #Klasörü silip içinde boş klasör yaratma
    shutil.rmtree('./img/letters')
    os.mkdir('./img/letters')
    os.mkdir('./img/letters/alphabet')
    os.mkdir('./img/letters/symbols')
    os.mkdir('./img/letters/numbers')


#Bu fonksiyon ile img/workbench içinde bulunan işlenmek üzere doldurulmuş 'letter_table.png' üstündeki harfler çağrılma sırasına göre kırpılıyor  ve img/letters/alphabet klasörüne kaydediliyor
#coords: sol üst, sağ alt kordinatları
def crop_letter(i,letter,coords):
    image_obj = Image.open(path_letter_table).convert("RGBA") #RGBA dönüştürme sebebimiz kırpılmış imajların etrafındaki oluşan kareyi silmek
    cropped_image = image_obj.crop(coords)
    if letter in alphabet_numbers: #Klasör kategorizasyonu
        cropped_image.save(f'./img/letters/numbers/{i}.png')
        letter_path= f'./img/letters/numbers/{i}.png'
        import_db(letter,letter_path)
    elif letter in alphabet_symbols:
        cropped_image.save(f'./img/letters/symbols/{i}.png')
        letter_path= f'./img/letters/symbols/{i}.png'
        import_db(letter,letter_path)
    else:
        cropped_image.save(f'./img/letters/alphabet/{i}.png')
        letter_path= f'./img/letters/alphabet/{i}.png'
        import_db(letter,letter_path)


i=0 #Dosya adı
coords= [-47,51,-1,97] #0-x1,1-y1,2-x2,3-y2
path_letter_table= './img/testdata/letter_table.png' #BURAYI DAHA SONRA WORKBENCH DİYE DÜZELT
alphabet_all= 'ABCÇDEFGĞHİIJxKLMNOÖPRSŞTUÜxVYZ0123456789x/"\'.,?!()-+;:xabcçdefgğhiıjxklmnoöprsştuüxvyz%=><*[]{}~' #Döngü üstü harf kontrolü, x'ler alt satır temsil ediyor
alphabet_symbols= '/"\'.,?!()-+;:%=><*[]{}~' #Liste içindeki semboller
alphabet_numbers= '0123456789' #Liste içindeki numaralar
letter_path= None #Son kırpılan harfin path'ini tutar

#Bir sql dosyası oluşturulur ve imleçç ile bir table yaratılır.
conn = sql.connect('paths.db')
cursor= conn.cursor()
clean_letters()
cursor.execute("CREATE TABLE 'image_paths' (letter,path)") #Bu tabloyu harfleri ve konumlarını saklamak ve erişmek için kullanacağız

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