# Check True

Python Flask frameworkunu kullanarak word dosyasında istediğimiz işlemleri yapmak için oluşturduğum web arayüzüdür.

Kullandığım kütüphaneler:

| Kullandığım Python Kütüphaneleri                             | Version |
| ------------------------------------------------------------ | :-----: |
| [pip · PyPI](https://pypi.org/project/pip/)                  |  21.0   |
| [docx2python](https://docx2python.readthedocs.io/en/latest/index.html#installation) | 1.27.1  |
| [python-docx](https://python-docx.readthedocs.io/en/latest/user/install.html#install) | 0.8.10  |
| [Werkzeug · PyPI](https://pypi.org/project/Werkzeug/)        |  1.0.1  |
| [Flask · PyPI](https://pypi.org/project/Flask/)              |  1.1.2  |
| [Jinja2 · PyPI](https://pypi.org/project/Jinja2/)            | 2.11.2  |
| [Pandas · PyPI]( https://pypi.org/project/pandas/ )          | 1.1.5   |
| [Numpy · PyPI](https://pypi.org/project/numpy/)              |  1.19.3 |

| Kullandığım JavaScript Kütüphaneleri                             | Version |
| ------------------------------------------------------------ | :-----: |
| [docsify](https://docsify.js.org/#/)                        |  4.11.6 |

İlk olarak ana dosya dizininde aşağıdaki satırı komut satırınızda çalıştırın:

```shell
>python main.py
```

ardından `localhost:5000` adresini tarayıcınızda ziyaret edin. Sizleri `Resim 1` deki gibi bir ekran kaşılayacaktır.

Dökümantasyonu için **documentation**/ dosya konumunda  aşağıdaki kodu komut satırında çalıştırın ve `localhost:3000` adresini  tarayıcınızda ziyaret edin.

```sh
> docsify serve .
```



<img src="./documentation/images/image-20210130021047530.png">

> Resim 1 - Sistemin ana sayfasının bir görünümü.

Dosya Seç butonunu kullanarak docx/doc seçin ve analiz etmek istediğiniz özelliği seçin. Ardından seçtiğiniz/görmek istediğiniz dosya özelliğine göre aşağıdaki ekran ile karşılaşacaksınız.

## Dosya Detayları

<img src="./documentation/images/image-20210130015638143.png">

> Resim 2 - Dosya özelliklerinin görünümü

## Dosya Üst ve Alt Başlıkları

<img src="./documentation/images/image-20210130021831285.png">

> Resim 3 - Dosyada bulunan alt ve üst başlıkların kontrolu

## Paragraf

<img src="./documentation/images/image-20210130022306238.png">

> Resim 4 - Dosyada bulunan paragrafların listesi ve bulundukları sıra numarası

## Dosya Sayfa Yapısı

<img src="./documentation/images/image-20210130023452440.png">

> Resim 5 - Kenar boşlukları ve yönlendirmeye dair bilgilerin bulunduğu ekran

## Paragraf Hizalama ve Girinti

<img src="./documentation/images/image-20210130023756476.png">

> Resim 6 - Dosyada bulunan her bir paragrafın durumun gösterildiği ekran

## Tablolar

<img src="./documentation/images/image-20210202181945841.png">

> Resim 7 - Dosyada bulunan bütün tabloların gösterildiği ekran

## Kaynaklar

<img src="./documentation/images/image-20210202182042240.png">

> Resim 7 - Dosyada bulunan kaynakların gösterildiği ekran



**Proje hala geliştirilme aşamasındadır. Bu yüzden yanlışlar ve eksikler olabilir.**
