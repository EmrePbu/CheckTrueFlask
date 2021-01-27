from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, send_from_directory
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import os
from werkzeug.utils import secure_filename
from werkzeug.middleware.shared_data import SharedDataMiddleware


app = Flask(__name__)


# main page route
@app.route('/')
def index():
    return render_template('index.html')


# doc page
@app.route('/doc')
def documentation():
    return render_template('documentation.html')


# register page
@app.route('/register')
def register():
    return render_template('register.html')


"""
# selecting file
@app.route('/file/<string:filename>')
def selectFile(filename):
    return 'Selected file name: '+filename
"""

if __name__ == '__main__':
    app.run(debug=True)


""""import methods as myMethods

# bu kısım çalışmıyor
#        word dosyasının kesinlikle ./documents klasöründe olması gerekiyor
#        fileName = "5150rnek_Tez_O_Orhan_YL_Parametresiz"


# Word dosyasında var olan bütün resimleri belirtilen dosya konumuna json dosyası olarak alır.
# ./buffer/word/media/ dosya yolunu kontrol edebilirsiniz.
myMethods.GetAllImages()

# Word dosyasından kullanılan bütün yazı fontlarını belitrilen dosya konumuna json dosyası olarak alır.
# ./buffer/word/fontTable.xml.json/ dosya yolunu kontrol edebilirsiniz.
myMethods.GetAllFonts()

# Word dosyasının içeriğinin bulunduğu kısım body kısmıdır bunuda belirtilen dosya konumuna json dosyası olarak alır.
# ./buffer/word/document.xml.json/ dosya yolunu kontrol edebilirsiniz.
myMethods.GetBody()

# Word dosyasının sayfa sayısını verir.
pages = myMethods.GetPageNumber()
print("Toplam sayfa sayısı: ", pages)

# Word dosyasındaki bütün sayfaların kenar boşluklarını kontrol eder.
# Hangi sayfaların Kenar boşluğu uygun değilse onu yazar. uygun ise True yazar.
myMethods.GetPagesMargin()
"""
