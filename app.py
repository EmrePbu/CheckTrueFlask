from metric_converter import CheckTrue
import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, send_from_directory
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, FileField, validators
from passlib.hash import sha256_crypt
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
import read_file as RF


UPLOAD_FOLDER = 'documents'
ALLOWED_EXTENSIONS = {'doc', 'docx', 'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# main page route
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # bu return işlemi kullanıcıya dosya indirmesi için redirect yapmayı sağlıyor
            return redirect(url_for('select_file', filename=filename))
    return render_template('index.html')


"""
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


# istenilen dosyanın kullanıcıya sunulması işlemini yapıyor
# yani kullanıcının bilgisayarına dosya indirmek için
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})
"""


# doc page
@app.route('/doc')
def documentation():
    return render_template('documentation.html')


# register page
@app.route('/register')
def register():
    return render_template('register.html')


# selected file
@app.route('/uploads/<filename>')
def select_file(filename):
    filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
        _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
    content_list = RF.read_paragraph(filename=filepath)
    file_details = RF.file_properties(filename=filepath)
    file_header = RF.file_header(filename=filepath)
    file_footer = RF.file_footer(filename=filepath)
    file_margin = RF.read_margin(filename=filepath)
    _checkMargin = CheckTrue.checkMargin
    # RF.file_footer(filename=filepath)
    file_body = RF.file_body(filename=filepath)

    return render_template('file_operations.html', _checkMargin=_checkMargin, file_details=file_details, filename=filename, content_list=content_list, file_header=file_header, file_footer=file_footer, file_body=file_body, file_margin=file_margin)


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
