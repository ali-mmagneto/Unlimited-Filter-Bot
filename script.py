class Script(object):

    START_MSG = """<b>Hey {},

Ben bir filter botuyum ve filterlarla ilgili bir sınırım yok ekle ekleyebildiğin kadar :)

<i>/help</i> detaylar için kullan.</b>
"""


    HELP_MSG = """
<i>Beni grubunuza yönetici olarak ekle ve filtrelemeye başla :)</i>


<b>Basic Commands;</b>

/start - Hayatta olup olmadığımı kontrol et!
/help - Yardım komutu
/about - Benim hakkımda bişiler!


<b>Filtre Komutları;</b>

<code>/filter Filtreismi</code>  -  Ad için filtre ekleme

<code>/del Filtreismi</code>  -  Filter Silme

<code>/delall</code>  -  Filtrelerin tamamını silme (Yalnızca Grup Sahibi!) 

<code>/viewfilters</code>  -  Sohbetteki tüm filtreleri listeleme


<b>Connection Commands;</b>

<code>/connect grupid</code>  -  Grubunuzu PM'ime bağlayın. Ayrıca kolayca kullanabilirsiniz,
<code>/connect</code> in groups.

<code>/connections</code>  -  Bağlantılarınızı yönetme.


<b>© @mmagneto</b>
"""


    ABOUT_MSG = """⭕️<b>Benim Adım : Filtre Botu</b>

⭕️<b>Oluşturan:</b> @mmagneto   

⭕️<b>Dil :</b> <code>Python3</code>

⭕️<b>Kütüphane :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

"""
