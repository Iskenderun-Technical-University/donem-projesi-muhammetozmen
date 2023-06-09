[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/uelKf0-p)
# Parwrite: El Yazısı Taklit Programı

![Logo](./img/readme_images/logo.png)

**Parwrite Nedir?**

> Parwrite, insanların el yazısı yazı stillerini dijital olarak kaydederek, yazı stilini koruyarak bilgisayar ortamında kullanılabilecek hale getiren bir teknolojidir. Bu teknoloji, özellikle el yazısı yazma tarzıyla öne çıkan veya kişisel bir imza niteliği taşıyan belgelerin, mektupların veya notların dijitalleştirilmesinde ve saklanmasında kullanışlıdır. Parwrite, kaydedilen el yazısı örnekleri üzerinden bir imaj tabanlı yazı biçemi (font) oluşturur ve bu fontu dijital ortama aktarır. Böylece, örneğin bir kişinin özel bir imzası, Parwrite sayesinde yazı, tabloyu dolduranın el yazısıyla aynı görünümü korur.

**Projenin Yapılma Sebebi Nedir?**

> Projenin faydalı olabileceği durumlar şunlardır.
> -   Özellikle okul ve üniversite öğrencileri için, ödevlerin el yazısı ile yazılması gerektiği durumlarda bu teknoloji sayesinde yazma işlemi hızlandırılabilir ve daha okunaklı hale getirilebilir. Ayrıca, Parwrite teknolojisi, ödevlerin veya belgelerin düzenlenmesi veya düzeltmeler yapılması gerektiğinde de kullanışlıdır. El yazısı ile yazılan bir belgeyi bilgisayara aktarmak için çoğu zaman yeniden yazmak veya elle tarayarak dijitalleştirmek gerekiyor. Ancak Parwrite teknolojisi ile bu işlem daha hızlı ve kolay hale getirilir. Bu sayede, belgelerin ve ödevlerin daha hızlı ve kolay bir şekilde hazırlanması ve düzenlenmesi mümkün olur.
> -   Parwrite teknolojisi, el yazısı yazmayı zorlaştıran bazı sağlık sorunlarına sahip olan kişiler için de oldukça yararlıdır. Örneğin, Parkinson hastalığı olan kişilerin el yazısı yazmaları zor olabilir. Bu durumda Parwrite teknolojisi, kişinin el yazısını dijitalleştirerek yazma işlemini kolaylaştırabilir.
> -   El yazısı, birçok kişiye göre, dijital yazılarla kıyaslandığında daha kişisel ve duygusal bir ifade aracıdır. Bu nedenle, el yazısı kullanarak yazılan mektuplar, şiirler veya öyküler, okuyucuda daha güçlü bir etki bırakabilir ve daha kişisel bir bağ kurulmasına olanak tanır. El yazısı, her bireyin kendine özgü bir yazı stili geliştirebileceği bir alandır ve bu nedenle el yazısı kullanarak yazılan metinler, yazarın kendine özgü kişiliğini ve stilini yansıtır. El yazısı kullanımı, yazılan metne bir estetik değer katar ve bu nedenle, el yazısı ile yazılmış bir mektup veya şiir, okuyucuda daha derin bir etki bırakabilir. Ayrıca, el yazısı kullanarak yazılmış metinler, yazılı kültürün tarihinde önemli bir yer tutar ve bu nedenle, el yazısı kullanımı, bir kültür mirası olarak da değerlidir. Sonuç olarak, el yazısı kullanarak yazılan metinler, sadece okuyucuya daha güçlü bir etki bırakmakla kalmaz, aynı zamanda yazma eylemini daha kişisel ve anlamlı hale getirir.
> - Tüm bunların yanında Parwrite projesi, el yazısı yazma işlemini dijitalleştirerek, belgelerin daha hızlı ve kolay bir şekilde yazılmasına olanak tanıdığından. Ayrıca, yazının doğrudan dijital ortamda kaydedilmesi, kağıt tüketimini azaltarak çevre dostu bir seçenek sunar.

**Projenin Çalışma Mantığı**
> Kullanıcı, 7x13'lük bir tabloya numara, sembol ve alfabenin tüm harflerini büyük ve küçük olacak şekilde el yazısı ile yazar.
>
> ![Letter Table](./img/readme_images/letter_table.png)
>
>> *El yazısı için arkadaşım Tolga'ya teşekkür ederim ;)*
>
> Daha sonra, Parwrite yazılımı, kaydedilen harflerle bir veri kümesi oluşturur ve bu veri kümesi, yazının dijital ortamda saklanabilmesi için kullanılır. Kullanıcı, istediği bir yazıyı el yazısı ile yazar ve Parwrite yazılımı, önceden kaydedilmiş harfleri kullanarak, yazıyı dijital ortamda kırpar ve kullanıcının isteği üzerine çeşitli rastgeleleştirmeler ve font büyüklüğü değişiklikleri yaparak kağıda döker.
>
> ![From App](./img/readme_images/fromapp.jpg)
>> *Yapım aşamasından bir görüntüdür, proje bitişte farklı gözükebilir*
>
> Son olarak kullanıcının tercihine göre PNG, JPEG veya PDF olarak kaydeder.
> 
> ![Result](./img/readme_images/example.png)
>> *Bu örnekte rastgelelik yüksektir, rastgelelik çeşitlilik doğurur ama okunabilirlikle ters orantılıdır.*


**Projedeki Veritabanı Hakkında**
> Parwrite projesinde, kullanıcının el yazısı ile yazdığı harfleri dijital ortamda saklamak için SQLite veritabanı kullanılacak. SQLite, küçük boyutu, hızlı performansı ve yerel bir veritabanı yönetim sistemi olarak kullanılabilmesi gibi özellikleri sayesinde, Parwrite projesi için uygun bir seçimdir. SQLite veritabanı içinde, her harf için bir tablo oluşturulacak. Tabloların sütunları, harf ve harfin bulunduğu dizini tutacak. Kullanıcının girdiği harf, bu tablolardan biri ile eşleştirilecek ve harfin bulunduğu dizin, Parwrite yazılımı tarafından okunarak kullanılabilecek. Bu veritabanı yapısı, Parwrite projesinde veri yönetimini kolaylaştıracak ve daha hızlı bir arama ve erişim işlemi sağlayacak. Örneğin, kullanıcı "A" harfini yazdığında, Parwrite yazılımı, SQLite veritabanındaki "A" tablosuna erişerek, bu harfin bulunduğu dizini kolayca bulabilecek. Parwrite projesinde kullanılan SQLite veritabanı yapısı, aynı zamanda gelecekteki geliştirmeler için de uygun bir temel oluşturur. Veritabanına yeni harfler veya semboller eklemek, mevcut harfleri düzenlemek veya silmek gibi işlemler, SQLite veritabanı yönetim araçları kullanılarak kolayca gerçekleştirilebilir.
>
> Sonuç olarak, Parwrite projesinde kullanılacak SQLite veritabanı, veri yönetimini kolaylaştıran ve hızlı bir arama ve erişim işlemi sağlayan bir veritabanı yönetim sistemi olarak kullanılacak.

---
### Kullandığım Kaynaklara Atıflar:

#### Font: 
[Baby Doll](https://www.dafont.com/babydoll.font)

[Morning Breeze](https://www.fontspace.com/morning-breeze-font-f64724)

#### İmaj:
[Kalem](https://static.thenounproject.com/png/118822-200.png)
