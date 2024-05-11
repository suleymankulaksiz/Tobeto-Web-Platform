<strong>TEST SENARYOSU 4 ANASAYFAYA İŞLEMLERİ</strong> <br>
*orijinal test caseler excel ile yazılmıştır.

![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/b9f34b29-2dd3-4a66-be96-2e59ac76293d)


<b>Test Case 1 :</b> Anasayfaya yönlendirilme bildirimi
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/dc581bc6-f159-4d10-b45d-dd54fc7de87a)

<b>Description :</b> Kullanıcının platforma giriş işleminin ardından doğru sayfaya yönlendirildiğine dair uyarı mesajının gösterilmesi test edilecektir.<br>
<b>Ön koşul :</b> Test ortamı çalısır ve hazır durumda olmalıdır. 

<b>Adımlar:</b>

<b>1-</b> Siteye gidilir. <br>
Test Data:https://tobeto.com/giris<br>
<b>2-</b>"E-Posta" kutucuğuna tıklanır ve e-posta girilir.<br>
İnput:tobeto@hotmail.com<br>
<b>3-</b>"Sifre" kutucuguna tiklanır ve sifre girilir<br>
İnput: 123456<br>
<b>4-</b>"Giriş yap" butonuna tıklanır.<br>

<b>Expected Result:</b> Ana sayfaya yönlendirildiği ve ekranda "Giriş Başarılı" uyarısı pop-up uyarı mesajı ekranda görüntülenmelidir. Görsel içeriği ekteki gibi olmalıdır.<br>
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/8fb7d301-af2c-4d60-aec5-790fcefdb068)


<b>Test Case 2 :</b> Üst menü panelinin kontrolü 
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/7f6bb511-df12-4cb6-9187-0bd120592436)

<b>Description :</b>Üst menü panelinin içinde bulunan başlıkların tıklanabilir buton olduğu test edilecektir.
<b>Ön koşul :</b> Sayfanın hazır ve çalışır durumda olması https://tobeto.com/platform adresine gidilmelidir.


<b>Adımlar:</b>

<b>1-</b>  "Ana Sayfa" butonuna tıklanır. <br>
<b>Expected Result:</b> "Ana Sayfa" sayfası görüntülenmelidir.<br>
<b>2-</b>  "Profilim" butonuna tıklanır.<br>
<b>Expected Result:</b> https://tobeto.com/profilim sayfasına yönlendirilmelidir.<br>
<b>3-</b>  "Değerlendirmeler" butonuna tıklanır.<br>
<b>Expected Result:</b> https://tobeto.com/degerlendirmeler sayfasına yönlendirilmelidir.<br>
<b>4-</b> "Katalog" butonuna tıklanır.<br>
<b>Expected Result:</b>https://tobeto.com/platform-katalog sayfasına yönlendirilmelidir.<br>
<b>5-</b> "Takvim" butonuna tıklanır.<br>
<b>Expected Result:</b>https://tobeto.com/takvim sayfasına yönlendirilmelidir.<br>
<b>6-</b> "İstanbul Kodluyor" butonuna tıklanır.<br>
<b>Expected Result:</b>https://tobeto.com/istanbul-kodluyor sayfasına yönlendirilmelidir.<br>

<b>Test Case 3 :</b>Ana sayfada yer alan Hoş geldin ve İstanbul Kodluyor panelinin metinleri kontrolü
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/8af54863-24f6-4442-8e08-e26ffeaaf307)

<b>Description :</b>Ana sayfadaki gerekli metinlerin görüntülendiği kontrol edilecektir. <br>
<b>Pre-condition :</b> Sayfanın hazır ve çalışır durumda olması https://tobeto.com/platform adresine gidilmelidir.

<b>Adımlar:</b>

<b>1-</b>"TOBETO'ya hoş geldin" metninin görüntülendiği doğrulanır.  <br>
<b>2-</b>"İsim" metninin görüntülendiği doğrulanır.<br>
Test Data:Kayıt yapılan hesabın ismi olmalıdır.<br>
<b>3-</b>"Yeni nesil öğrenme deneyimi ile Tobeto kariyer yolculuğunda senin yanında!" metninin görüntülendiği doğrulanır.<br>
<b>4-</b>"İstanbul Kodluyor" logosunun  görüntülendiği doğrulanır.<br>
<b>5-</b>"Ücretsiz eğitimlerle, geleceğin mesleklerinde sen de yerini al." metninin  görüntülendiği doğrulanır.<br>
<b>6-</b>"Aradığın  “İş”  Burada!" metninin  görüntülendiği doğrulanır.<br>

<b>Expected Result:</b>İlgili metinler ekranda görüntülenmelidir. Ekteki gibi olmalıdır.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/c2be6af5-0476-4619-a25d-349b9a488d90" width="500" height="450"><br>

<b>Test Case 4 :</b> İstanbul Kodluyor panel içeriğinin kontrolü
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/7727ee40-8aff-41cf-a178-b941329fd2b6)

<b>Description :</b>İstanbul Kodluyor panel içeriği kontrol edilecektir.
<b>Pre-condition :</b>Sayfanın hazır ve çalışır durumda olması https://tobeto.com/platform adresine gidilmelidir.


<b>Adımlar:</b>

<b>1-</b>Varsayılan olarak "Başvurularım" açılır menünün görüntülendiği doğrulanır<br>
<b>Expected Result:</b>Profil sahibinin başvuru yaptığı program ve kabul durumu görüntülenmelidir. <br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/66b4d690-8f35-4ec8-a8dd-765bc8d6ffb9" width="500" height="200"><br>
<b>2-</b>"Eğitimlerim"butonu tıklanır ve ilgili açılır menünün görüntülendiği doğrulanır<br>
<b>Expected Result:</b>Ekteki gibi görüntülenmelidir.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/c1e245ac-1953-40b6-8398-750fd255b4a2" width="500" height="200"><br>
<b>3-</b>"Duyuru ve Haberlerim"butonu tıklanır ve ilgili açılır menünün görüntülendiği doğrulanır<br>
<b>Expected Result:</b>Ekteki gibi görüntülenmelidir.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/d2210aa6-dfc5-4d34-8f85-ffee10b46b34" width="500" height="200"><br>
<b>4-</b>"Anketlerim"butonu tıklanır ve ilgili açılır menünün görüntülendiği doğrulanır<br>
<b>Expected Result:</b>Ekteki gibi görüntülenmelidir.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/1f13c16c-3977-4dd1-b229-7ca533bb57ce" width="500" height="200"><br>
<b>5-</b>Okunmamış bildirim varsa bu sayının ekranda görüntülendiği doğrulanır.<br>
<b>Expected Result:</b>Ekteki gibi görüntülenmelidir.<br>
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/85bca7a5-d15b-4e6e-a529-2995e4d053a0)


<b>Test Case 5 :</b>Anasayfada yer alan "Eğitimlerim" bölümünün kontrolü
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/7faff93b-c9ed-41d5-b362-f55613daee04)

<b>Description :</b>Eğitimlerim bölümünde "Daha Fazla Göster" ve "Eğitime Git" butonlarının işlevi ve ilgili sayfaya yönlendirilmesi test edilecektir. <br>
<b>Pre-condition :</b> Sayfanın hazır ve çalışır durumda olmasıhttps://tobeto.com/platform adresine gidilmelidir.

<b>Adımlar:</b>

<b>1-</b>"Eğitimlerim"butonu tıklanır<br>
<b>Expected Result:</b>Açılır menü görüntülenmelidir.<br>
<b>2-</b>En fazla 4 eğitim içeriği görüntülendiği doğrulanır.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/ac0cf207-036b-42bd-8635-eb814ebfea8c" width="400" height="200"><br>
<b>3-</b>Dörtten fazla eğitim varsa "Daha Fazla Göster" butonuna tıklanır.<br>
<b>Expected Result:</b>https://tobeto.com/egitimlerim sayfasına yönlendirilmelidir.<br>
<b>4-</b>"Eğitime Git" butonuna tıklanır.<br>
<b>Expected Result:</b>İlgili eğitimin detaylarının görüntülendiği sayfaya yönlendirilmelidir.<br>

<b>Test Case 6 :</b>Anasayfada yer alan "Duyuru ve Haberlerim" bölümünün kontrolü

<b>Description :</b>"Duyuru ve Haberlerim" bölümünde "Daha Fazla Göster" ve "Devamını Oku" butonlarının işlevi ve ilgili sayfaya yönlendirilmesi test edilecektir. <br>
<b>Pre-condition :</b>Sayfanın hazır ve çalışır durumda olması https://tobeto.com/platform adresine gidilmelidir.

<b>Adımlar:</b>

<b>1-</b>"Duyuru ve Haberlerim"butonu tıklanır<br>
<b>Expected Result:</b>Açılır menü görüntülenmelidir.<br>
<b>2-</b>En fazla 3 adet duyuru/haber içeriğin görüntülendiği doğrulanır.<br>
<b>Expected Result:</b>Ekte yer alan görsel gibi görüntülenmelidir.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/c61fb267-a60a-49f3-8f4f-cd41e21ecfe8" width="400" height="200"><br>
<b>3-</b>Üçten fazla duyuru/haber varsa "Daha Fazla Göster" butonuna tıklanır.<br>
<b>Expected Result:</b> https://tobeto.com/duyurular sayfasına yönlendirilmelidir.<br>
<b>4-</b>"Devamını Oku" butonuna tıklanır.<br>
<b>Expected Result:</b>İlgili Duyuru/Haber detaylarının görüntülendiği sayfaya yönlendirilmelidir.

<b>Test Case 7 :</b>Anasayfada yer alan "Sınavlarım" bölümünün kontrolü
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/63acdabb-5116-496b-93be-a566526ffcca)


<b>Description :</b>"Sınavlarım" bölümündeki sınav detaylarına erişebilme ve rapor görüntüleme penceresi kontrol edilecektir.
<b>Pre-condition :</b>Sayfanın hazır ve çalışır durumda olması https://tobeto.com/platform adresine gidilmelidir.


<b>Adımlar:</b>

<b>1-</b>Sınavlarım bölümünün görüntülendiğini doğrulanır.<br>
<b>Expected Result:</b>Sınav adı,sınıfı,adı,sınav süresi bilgilerinin görüntülenmelidir.<br>
<b>2-</b>Sınav kutucuğuna tıklanır.<br>
<b>Expected Result:</b>Sınava ait detayların görüntülendiği bir açılır pencere ekranda görüntülenmelidir.<br>
<b>3-</b>Açılır pencerede sınav gerçekleştiyse "Raporu Görüntüle" butonuna tıklanır.<br>
<b>Expected Result:</b>"Doğru","Yanlış","Boş","Puan" bilgilerinin bulunduğu bir açılır pencere ekranda görüntülenmelidir.


<b>Test Case 8 :</b>Anasayfanın en altında yer alan "Profilini Oluştur","Kendini Değerlendir" ve "Öğrenmeye Başla" bölümlerinin ve "Başla" butonunun kontrolü
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/7058ad41-2bac-494d-8196-c620ff984f25)



<b>Description :</b>Anasayfanın en altında yer alan "Profilini Oluştur","Kendini Değerlendir" ve "Öğrenmeye Başla" bölümlerinin ve "Başla" butonunun kontrolü test edilecektir.<br>
<b>Pre-condition :</b>Sayfanın hazır ve çalışır durumda olması https://tobeto.com/platform adresine gidilmelidir.


<b>Adımlar:</b>

<b>1-</b>Anasayfanın en altında "Profilini oluştur","Kendini değerlendir","Öğrenmeye başla" bölümlerinin görüntülendiği doğrulanır.<br>
<b>Expected Result:</b> Ekteki gibi olmalıdır.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/97f6de6f-13d0-4aa3-8a9a-de8a472801ae" width="500" height="150"><br>
<b>2-</b>"Profilini Oluştur" butonuna tıklanır. <br>
<b>Expected Result:</b>https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim sayfasına yönlendirilmelidir.<br>
<b>3-</b>Ana sayfa butonuna tıklanır.<br>
<b>4-</b>"Kendini Değerlendir" butonuna tıklanır.<br>
<b>Expected Result:</b> https://tobeto.com/degerlendirmeler sayfasına yönlendirilmelidir.<br>
<b>5-</b>Ana sayfa butonuna tıklanır.<br>
<b>6-</b>"Öğrenmeye Başla" butonuna tıklanır.<br>
<b>Expected Result:</b>https://tobeto.com/egitimlerim sayfasına yönlendirilmelidir.






