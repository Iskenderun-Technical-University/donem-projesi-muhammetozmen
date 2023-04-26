#█▄▀ ▄▀█ █▀█ █ ▀█▀ █░█ ▄▀█
#█░█ █▀█ █▀▄ █ ░█░ █▀█ █▀█
#muhammetozmen

#Çeşitli imaj etkileşimi için Pillow kütüphanesi kullandım ve SQL olarak SQLite tercih ettim.
from PIL import Image
import sqlite3

#Bu fonksiyon ile img/workbench içinde bulunan işlenmek üzere doldurulmuş 'letter_table.png' üstündeki harfler çağrılma sırasına göre kırpılıyor  ve img/letters/alphabet klasörüne kaydediliyor
#coords: sol üst, sağ alt kordinatları
def crop_letter(i,coords):
    image_obj = Image.open(path_letter_table).convert("RGBA") #RGBA dönüştürme sebebimiz kırpılmış imajların etrafındaki oluşan kareyi silmek
    cropped_image = image_obj.crop(coords)
    cropped_image.save(f'./img/letters/alphabet/{i}.png')
i=0 #Dosya adı
coords= [-47,51,-1,97] #0-x1,1-y1,2-x2,3-y2
path_letter_table= './img/testdata/letter_table.png' #BURAYI DAHA SONRA WORKBENCH DİYE DÜZELT
alphabet= 'ABCÇDEFGĞHİIJxKLMNOÖPRSŞTUÜxVYZ0123456789x/"\'.,?!()-+;:xabcçdefgğhiıjxklmnoöprsştuüxvyz%=><*[]{}~' #Döngü üstü harf kontrolü, x'ler alt satır temsil ediyor

for letter in alphabet:
    if letter=='x':
        coords[0]=-47
        coords[2]=1
        coords[1]+=98
        coords[3]+=98
    else:
        i+=1
        coords[0]+=49
        coords[2]+=49
        crop_letter(i,coords)