from metric_converter import CheckTrue
import os
from flask import Flask, render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
import read_file as RF


UPLOAD_FOLDER = 'documents'
ALLOWED_EXTENSIONS = {'doc', 'docx'}

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

            if request.form['submit_button'] == 'Dosya Detayları':
                return redirect(url_for('file_details', filename=filename))
            if request.form['submit_button'] == 'Dosya Üst ve Alt Başlıkları':
                return redirect(url_for('file_header_footer', filename=filename))
            if request.form['submit_button'] == 'Paragraf':
                return redirect(url_for('paragraph', filename=filename))
            if request.form['submit_button'] == 'Dosya Sayfa Yapısı':
                return redirect(url_for('file_page_structure', filename=filename))
            if request.form['submit_button'] == 'Paragraf Hizalama ve Girinti':
                return redirect(url_for('file_alignment_and_indent', filename=filename))
            else:
                # redirect(url_for('select_file', filename=filename))
                return "Error"
    return render_template('index.html')


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
    file_margin = RF.read_page_structure(filename=filepath)
    # page structure de kullan bunu checkMargin
    _checkMargin = CheckTrue.checkMargin
    file_alignment = RF.read_alignment(filename=filepath)
    #file_body = RF.file_body(filename=filepath)
    file_indent = RF.read_alignment_and_indent(filename=filepath)
    return render_template('file_operations.html', _checkMargin=_checkMargin, file_details=file_details, filename=filename, content_list=content_list, file_header=file_header, file_footer=file_footer, file_margin=file_margin, file_alignment=file_alignment, file_indent=file_indent)


@app.route('/uploads/<filename>')
def file_details(filename):
    filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
        _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
    file_details = RF.file_properties(filename=filepath)
    return render_template('pages/file_details_page.html',  file_details=file_details, filename=filename)


@app.route('/uploads/<filename>')
def file_header_footer(filename):
    filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
        _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
    file_header = RF.file_header(filename=filepath)
    file_footer = RF.file_footer(filename=filepath)
    return render_template('file_operations.html',  filename=filename,  file_header=file_header, file_footer=file_footer)


@app.route('/uploads/<filename>')
def paragraph(filename):
    filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
        _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
    content_list = RF.read_paragraph(filename=filepath)
    return render_template('file_operations.html', filename=filename, content_list=content_list, )


@app.route('/uploads/<filename>')
def file_page_structure(filename):
    filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
        _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
    file_margin = RF.read_page_structure(filename=filepath)
    _checkMargin = CheckTrue.checkMargin
    return render_template('file_operations.html', _checkMargin=_checkMargin, filename=filename, file_margin=file_margin)


@app.route('/uploads/<filename>')
def file_alignment_and_indent(filename):
    filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
        _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
    file_indent = RF.read_alignment_and_indent(filename=filepath)
    return render_template('file_operations.html', filename=filename,  file_indent=file_indent)


if __name__ == '__main__':
    app.run(debug=True)
