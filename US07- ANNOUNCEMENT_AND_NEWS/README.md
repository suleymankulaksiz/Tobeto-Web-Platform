<strong>TEST SENARYOSU 7 DUYURU VE HABERLERİMDE YER ALAN FİLTRELEME İŞLEMLERİ</strong> <br>
*orijinal test caseler excel ile yazılmıştır.

![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/a4d48055-ae60-4c18-b17a-0550b422c96e)



<b>Test Case 1 :</b> Duyuru ve haberlerin başlıklara göre aranması

<b>Description :</b> Listelenen eğitimlerinin başlıklarına göre arama yapılması test edilecektir.<br>
<b>Pre-condition :</b> Test ortamı çalısır ve hazır durumda olmalıdır. 

<b>Adımlar:</b>

<b>1-</b>En fazla 9 adet eğitim görüntülendiği doğrulanır. <br>
<b>2-</b>"Arama" kutucuğuna tıklanır.<br>
<b>3-</b>"Arama" kutucuğuna istenilen haber/duyuru başlığı girilir.<br>
Test Data:s-ınav<br>
<b>Expected Result:</b> Arama butonuna yazılan başlığa göre her bir karakter girildiğinde duyuru ve haberler anlık olarak güncellenmelidir.
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/482ec2e5-7c91-4720-bcb3-fe5f4fbe6bd9" width="600" height="150"><br>
<b>4-</b>"Arama" kutusuna girilen değer silinir.<br>
<b>5-</b>"Arama" kutucuğuna istenilen haber/duyuru başlığı girilir.<br>
Test Data: "q"<br>
<b>Expected Result:</b>"Bir duyuru bulunmamaktadır." uyarı mesajı ekranda görüntülenmelidir.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/7ec86886-e5a2-44a5-9fb5-a88d5803ec2a" width="700" height="100"><br>






<b>Test Case 2 :</b> Duyuru ve haberlerin türe göre filtrelenmesi

<b>Description :</b>Duyuru ve haberlerin türlerine göre filtrelenmesi test edilecektir.<br>
<b>Pre-condition :</b> Test ortamı çalısır ve hazır durumda olmalıdır. 

<b>Adımlar:</b>

<b>1-</b>"Tür" butonu tıklanır.   <br>
<b>2-</b>"Duyuru" seçilir.<br>
<b>Expected Result:</b> Duyurular listelenmelidir. Herhangi bir veri bulunmadığı takdirde "Bir duyuru bulunmamaktadır." uyarısının ekranda görüntülenmelidir.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/e8d7ed32-5b43-45c1-a22c-13f1c688a633" width="700" height="150"><br>

<b>3-</b>Tür başlığından "Duyuru" seçimi kaldırılır.<br>
<b>4-</b>"Tür" butonu tıklanır<br>
<b>5-</b>"Haber" seçilir.<br>
<b>Expected Result:</b>"Bir duyuru bulunmamaktadır." uyarısının ekranda görüntülenmelidir.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/56e13e99-ffc6-4a51-affd-5273515ba719" width="600" height="150"><br>







<b>Test Case 3 :</b>Duyuru ve haberlerin organizasyon isimlerine göre filtrelenmesi

<b>Description :</b>Listelenen duyuru ve haberlerin organizasyon ismine göre filtrelenmesi test edilecektir.<br>
<b>Pre-condition :</b> Sayfanın hazır ve çalışır durumda olmalıdır.

<b>Adımlar:</b>

<b>1-</b>Organizasyon bölümüne tıklanır. <br>
<b>2-</b>Organizasyon ismi seçilir.<br>
Test Data:İstanbul Kodluyor<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/50721daa-8d1d-4606-9f73-4955e9a6f0ae" width="600" height="100"><br>

<b>3-</b>Organizasyon bölümüne tıklanır.<br>
<b>4-</b>Organizasyon bölümünden "İstanbul Kodluyor" adının listeden kaldırıldığı kontrol edilir.<br>
<b>5-</b>Organizasyon kutucuğundaki X butonuna tıklanır.<br>
<b>6-</b>Organizasyon kutucuğuna harf girişi yapılır.<br>
Test Data: "L"<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/5061ace5-3c93-407a-845b-fcd5b910fb22" width="600" height="100"><br>


<b>Expected Result:</b>Organizasyon listesinden yapılan seçime göre liste güncellenmelidir.






<b>Test Case 4 :</b> Duyuru ve haberlerin tarihe göre sıralanması

<b>Description :</b>Duyuru ve haberlerin tarihe göre sıralanması test edilecektir.<br>
<b>Pre-condition :</b>Sayfanın hazır ve çalışır durumda olmalıdır.

<b>Adımlar:</b>

<b>1-</b>Sıralama kutucuğuna tıklanır.<br>
<b>2-</b>Sıralama kutucuğundan "Tarihe Göre (Y-E)" seçilir.<br>
<b>Expected Result:</b>Duyuru ve haberler tarihlerine göre yeniden eskiye (Y-E) olacak şekilde sıralanarak listelenmelidir.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/9fcfa507-60b6-4ae1-aa29-c66b60f6a796" width="700" height="150"><br>

<b>3-</b>Sıralama kutucuğundan "Tarihe Göre (E-Y)" seçilir.<br>
<b>Expected Result:</b>Duyuru ve haberler tarihlerine göre eskiden yeniye (E-Y) olacak şekilde sıralanarak listelenmelidir.
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/86f4670f-5119-4518-92fb-5a052aaa013d" width="700" height="150"><br>








<b>Test Case 5 :</b>"Okunmuş Olanları Gizle" ve "Hepsini Göster" butonların işlevinin kontrolü

<b>Description :</b>"Okunmuş olanları gizle" butonuna tıklandığında listede okunmuş olan haber ve duyuruların gizlendiği, "Hepsini Göster" butonuna tıklandığında bütün duyuru ve haberlerin listelendiği test edilecektir. <br>
<b>Pre-condition :</b> Sayfanın hazır ve çalışır durumda olmalıdır.

<b>Adımlar:</b>

<b>1-</b>Gri renkli bir duyuru/haber seçilir<br>
<b>2-</b>"Devamını Oku" kısmına tıklanır.<br>
<b>3-</b>Açılan sayfadan kapat butonuna tıklanır.<br>
<b>Expected Result:</b>Duyuru/haber renginin beyaz olarak değişmelidir.<br>
<b>4-</b>"Okunmuş Olanları Gizle" butonuna tıklanır.<br>
<b>Expected Result:</b>Listenen duyurularda okunmus olanlar gizlenmelidir.






<b>Test Case 6 :</b>Filtreleme araçlarının eş zamanlı çalışmasının kontrolü 

<b>Description :</b>"Arama", "Tür", "Organizasyon" ve "Sıralama" filtreleme araçlarının eş zamanlı çalışması test edilecektir.<br>
<b>Pre-condition :</b>Sayfanın hazır ve çalışır durumda olmalıdır.

<b>Adımlar:</b>

<b>1-</b>"Arama" kutucuğuna tıklanır.<br>
<b>2-</b>"Arama" kutucuğuna istenilen haber/duyuru başlığı girilir.<br>
Test Data: "sınav"<br>
<b>Expected Result:</b>Girilen başlığa yönelik liste güncellenmelidir.<br>
<b>3-</b>"Tür" butonu tıklanır.<br>
<b>4-</b>"Duyuru" seçilir.<br>
<b>Expected Result:</b>Tür butonundan "Duyuru" ve "Haber" seçimine göre liste güncellenmelidir.<br>
<b>5-</b>Organizasyon bölümüne tıklanır.<br>
<b>6-</b>Organizasyon ismi seçilir.<br>
Test Data:"İstanbul Kodluyor"<br>
<b>Expected Result:</b>Organizasyon listesinden yapılan seçime göre liste güncellenmelidir.<br>
<b>7-</b>Sıralama kutucuğuna tıklanır.<br>
<b>8-</b>Sıralama kutucuğundan "Tarihe Göre (E-Y)" seçilir.<br>
<b>Expected Result:</b>Duyuru ve haberler tarihlerine göre eskiden yeniye  (E-Y)  olacak şekilde sıralanarak listelenmelidir.
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/62f0ddab-c543-4d24-9946-48b55d9ee491" width="700" height="150"><br>








