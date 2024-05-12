# TEST SENARYOSU 11 "PROFİL OLUŞTUR" SAYFASI
*orijinal test caseler excel ile yazılmıştır.


![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/02db9675-ad9b-4eb5-903b-1dc95fadc9fd)




<b>Test Case 21 :</b> "Yabancı Dillerim" sayfasında yabancı dil eklenmesi

<b>Description :</b>Kullanıcının "Yabancı Dillerim" sayfasından yabancı dil eklemesi test edilecektir. <br>
<b>Pre-condition :</b> Test ortamı çalısır ve hazır durumda olmalıdır. Sol menüden "Yabancı Dillerim" butonuna tıklanmış olmalıdır.

<b>Adımlar:</b>

<b>1-</b>"Dil Seçiniz*" açılır listesinden bir dil seçilir<br>
<i>Test Data:</i>"Almanca"<br>
<b>2-</b>"Seviye Seçiniz*" açılır listesinden seviye seçilir.<br>
<i>Test Data:</i>Temel Seviye(A1,A2)<br>
<b>3-</b>"Kaydet" butonuna tıklanır.<br>
<b>Expected Result:</b>"Yabancı dil bilgisi eklendi." metni pop-up olarak ekranda görüntülenmelidir ve dil eklenmelidir. <br>
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/560c7eb5-6523-4e4b-bbea-40dc57b3d5f9)

<b>4-</b>"Dil Seçiniz*" açılır listesinden bir dil seçilir<br>
<i>Test Data:</i>Arapça<br>
<b>5-</b>"Seviye Seçiniz*" açılır listesinden seviye seçilir.<br>
<i>Test Data:</i>Orta Seviye(B1,B2)<br>
<b>6-</b>"Kaydet" butonuna tıklanır.<br>
<b>7-</b>"Dil Seçiniz*" açılır listesinden bir dil seçilir<br>
<i>Test Data:</i>Çekçe<br>
<b>8-</b>"Seviye Seçiniz*" açılır listesinden seviye seçilir.<br>
<i>Test Data:</i>İleri Seviye(C1,C2)<br>
<b>9-</b>"Kaydet" butonuna tıklanır.<br>
<b>10-</b>"Dil Seçiniz*" açılır listesinden bir dil seçilir<br>
<i>Test Data:</i>Çince(Mandarin)<br>
<b>11-</b>"Seviye Seçiniz*" açılır listesinden seviye seçilir.<br>
<i>Test Data:</i>Anadil<br>
<b>12-</b>"Kaydet" butonuna tıklanır.<br>
<b>Expected Result:</b>Bir satırda en fazla 3 adet dil görüntülenmelidir. <br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/00d25720-0fe4-4c6e-aa84-670c921adb1f" width="500" height="150"><br>




<b>Test Case 22 :</b> "Yabancı Dillerim" sayfasındadoldurulması zorunlu alanlarının boş bırakılma durumu<br>

<b>Description :</b> "Yabancı Dillerim" sayfasında doldurulması zorunlu alanlarının boş bırakılma durumunda ekranda uyarı metninin görüntülenmesi test edilecektir.<br>
<b>Pre-condition :</b> Test ortamı çalısır ve hazır durumda olmalıdır.  Sol menüden "Yabancı Dillerim" butonuna tıklanmış olmalıdır.

<b>Adımlar:</b>

<b>1-</b>"Dil Seçiniz*" alanından bir seçim yapılmaz. <br>
<b>2-</b>"Seviye Seçiniz*" alanından bir seçim yapılmaz.<br>
<b>3-</b>"Kaydet" butonuna tıklanır.<br>
<b>Expected Result:</b>Kutuların altında "Doldurulması zorunlu alan" uyarı mesajları gösterilmelidir. <br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/81f4191e-6d54-49fb-929d-33c79607e333" width="500" height="150"><br>



<b>Test Case 23 :</b> "Yabancı Dillerim" sayfasında eklenen yabancı dilin silinmesi<br>

<b>Description :</b>Kullanıcının "Yabancı Dillerim" sayfasında eklenen yabancı dilin silinmesi test edilecektir. <br>
<b>Pre-condition :</b>Test ortamı çalısır ve hazır durumda olmalıdır. Sol menüden "Yabancı Dillerim" butonuna tıklanmış olmalıdır.

<b>Adımlar:</b>

<b>1-</b>"Dil Seçiniz*" açılır listesinden bir dil seçilir.<br>
<i>Test Data:</i> "Almanca"<br>
<b>2-</b>"Seviye Seçiniz*" açılır listesinden seviye seçilir ve kayder butonuna tıklanır.<br>
<i>Test Data:</i> "Temel Seviye(A1,A2)"<br>
<b>Expected Result:</b> Dil eklenmelidir.<br>
<b>3-</b>Eklenen dil üzerindeki çöp kutusu ikonuna tıklanır.<br>
<b>4-</b>Açılır pencerede "Evet" seçeneğine tıklanır.<br>
<img src="https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/51408abf-f399-4ca7-bc13-04d8f30cc9b9" width="300" height="150"><br>

<b>Expected Result:</b>Eklenen dil listeden kaldırılmalıdır.<br>
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/49e9a2d0-6847-4bb8-bdfe-57f0ea990e33)<br>

<b>Test Case 24 :</b> "Yabancı Dillerim" sayfasında eklenen yabancı dilin tekrar eklenmesi<br>


<b>Description :</b>
<b>Pre-condition :</b>

<b>Adımlar:</b>

<b>1-</b>"Dil Seçiniz*" açılır listesinden bir dil seçilir<br>
<i>Test Data:</i>"Almanca"<br>
<b>2-</b>"Seviye Seçiniz*" açılır listesinden seviye seçilir.<br>
<i>Test Data:</i>"Temel Seviye(A1,A2)"<br>
<b>3-</b>"Kaydet" butonuna tıklanır.<br>
<b>Expected Result:</b>Dil eklenmelidir.<br>
<b>4-</b>"Dil Seçiniz*" açılır listesinden bir dil seçilir<br>
<i>Test Data:</i>"Almanca"<br>
<b>5-</b>"Seviye Seçiniz*" açılır listesinden seviye seçilir.<br>
<i>Test Data:</i>"Temel Seviye(A1,A2)"<br>
<b>6-</b>"Kaydet" butonuna tıklanır.<br>
<b>Expected Result:</b>"Bu dil zaten mevcut" uyarısı pop-up olarak ekranda gösterilmelidir.<br>
![image](https://github.com/suleymankulaksiz/Pair3-Tobeto-Proje/assets/137040573/7f35ac95-00ed-4102-830e-66aa02721397)














