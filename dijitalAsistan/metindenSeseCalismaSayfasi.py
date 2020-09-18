# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:23:37 2020

@author: 132415621
"""

from gtts import gTTS

import os

metin = "Hello, how are you?"

# dil ingilizce
language = "en"

sesim = gTTS(text=metin, lang=language, slow=False) 

sesim.save("merhaba.mp3") 

os.system("mpg321 merhaba.mp3")

#%%

from gtts import gTTS

import os

metin = "Merhaba, nasılsınız? işler nasıl gidiyor?"

# dil ingilizce
language = "tr"

sesim = gTTS(text=metin, lang=language, slow=False) 

sesim.save("turkce.mp3")

os.system("mpg321 turkce.mp3")

#%%

from gtts import gTTS

import os

metin = "Murat ve Tayfun aynı yurtta kalıyorlar. Onlar, oda arkadaşları. Çok iyi anlaşıyorlar. Bayram tatilinde Murat Tayfun'a Haydi bu tatilde seninle be­raber dedemin köyüne gidelim. Hem onlar çok sevinirler hem de biz şeh­rin gürültüsünden uzak üç gün dinleniriz. dedi."

# http://www.turkceogretimi.com/hikayeler/bayram-tatili adresinden alinmistir.
metin1="BAYRAM TATİLİ Murat ve Tayfun aynı yurtta kalıyorlar. Onlar, oda arkadaşları. Çok iyi anlaşıyorlar. Bayram tatilinde Murat Tayfun'a -Haydi bu tatilde seninle be­raber dedemin köyüne gidelim. Hem onlar çok sevinirler hem de biz şeh­rin gürültüsünden uzak üç gün dinleniriz.- dedi. Tayfun biraz düşünüp kabul etti. Bayramdan bir gün önce trene binip izmir'e kadar gittiler. Köye tren yoktu. Köye gitmek için izmir'den bir otobüse bindiler. Hemen dede­nin evine gittiler, iki yaşlı insan, dede ve nine çok mutlu oldular. Onlara evin en güzel odasını verdiler. Nine mutfağa koşup onlar için güzel yemek­ler yaptı. Tayfun ve Murat o akşam yorgunluktan erken uyudular. Sabah güneş doğmadan Önce uyandılar. Temiz havada biraz yürüyüp kahvaltıya koştular. Murat'ın dedesinin iki ineği, koyunları ve tavukları vardı. Murat'a ve Tayfun'a kahvaltıda taze süt, taze yumurta ve köy peyniri ikram ettiler. Tayfun -Her şey şehirden ne kadar farklı! Şehirde hiçbir zaman böyle taze yumurta, böyle güzel peynir yok.- dedi. O zaman Murat'ın dedesi gururla -Tabi oğlum, burada her şeyi biz kendimiz yapıyoruz. Bunun için hem çok temiz hem de çok taze.- diye cevap verdi. Tayfun ve Murat köyde üç gün kalıp döndüler. Derslerine yeni bir güç­le başladılar. Tayfun, onlann konukseverliğini hiç unutmadı. Her bayram, o da Murat gibi köye mutlaka bir bayram kartı göndermeği ihmal etmedi."
# dil ingilizce
language = "tr"

sesim = gTTS(text=metin1, lang=language, slow=False) 

sesim.save("turkce_hikaye1.mp3")

os.system("mpg321 turkce_hikaye.mp3")


