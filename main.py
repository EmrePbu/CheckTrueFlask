from metric_converter import CheckTrue
import os
from flask import Flask, render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from read_file import WithDocx, WithDocx2Python
UPLOAD_FOLDER = 'documents'
UPLOAD_IMAGE_FOLDER = 'images'
ALLOWED_EXTENSIONS = {'doc', 'docx'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


class Main:
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
            if file and Main.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # dosya kaydetme işi
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # bu return işlemi kullanıcıya dosya indirmesi için redirect yapmayı sağlıyor

                if request.form['submit_button'] == 'Dosya Detayları':
                    return redirect(url_for('file_details', filename=filename))

                elif request.form['submit_button'] == 'Dosya Üst ve Alt Başlıkları':
                    return redirect(url_for('file_header_footer', filename=filename))

                elif request.form['submit_button'] == 'Paragraf':
                    return redirect(url_for('paragraph', filename=filename))

                elif request.form['submit_button'] == 'Dosya Sayfa Yapısı':
                    return redirect(url_for('file_page_structure', filename=filename))

                elif request.form['submit_button'] == 'Paragraf Hizalama ve Girinti':
                    return redirect(url_for('file_alignment_and_indent', filename=filename))

                elif request.form['submit_button'] == 'Bütün Özellikleri Tek Seferde Kontrol Et':
                    return redirect(url_for('select_all', filename=filename))

                elif request.form['submit_button'] == 'Tablolar':
                    return redirect(url_for('file_table', filename=filename))

                elif request.form['submit_button'] == 'Kaynaklar':
                    return redirect(url_for('file_resources', filename=filename))

                else:
                    # redirect(url_for('select_file', filename=filename))
                    # TODO: error page yap
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
    def select_all(filename):
        filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
            _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
        content_list = WithDocx.read_paragraph(filename=filepath)
        file_details = WithDocx2Python.file_properties(filename=filepath)
        file_header = WithDocx2Python.file_header(filename=filepath)
        file_footer = WithDocx2Python.file_footer(filename=filepath)
        file_margin = WithDocx.read_page_structure(filename=filepath)
        # page structure de kullan bunu checkMargin
        _checkMargin = CheckTrue.checkMargin
        file_alignment = WithDocx.read_alignment(filename=filepath)
        #file_body = WithDocx2Python.file_body(filename=filepath)
        file_indent = WithDocx.read_alignment_and_indent(filename=filepath)
        file_table = WithDocx.read_table(filename=filepath)
        return render_template('file_operations.html', _checkMargin=_checkMargin, file_details=file_details, filename=filename, content_list=content_list, file_header=file_header, file_footer=file_footer, file_margin=file_margin, file_alignment=file_alignment, file_indent=file_indent, file_table=file_table)

    @app.route('/uploads/file_details/<filename>')
    def file_details(filename):
        filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
            _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
        file_details = WithDocx2Python.file_properties(filename=filepath)
        return render_template('pages/file_details_page.html',  file_details=file_details, filename=filename)

    @app.route('/uploads/file_header_footer/<filename>')
    def file_header_footer(filename):
        filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
            _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
        file_header = WithDocx2Python.file_header(filename=filepath)
        file_footer = WithDocx2Python.file_footer(filename=filepath)
        return render_template('pages/file_header_footer_page.html',  filename=filename,  file_header=file_header, file_footer=file_footer)

    @app.route('/uploads/paragraph/<filename>')
    def paragraph(filename):
        filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
            _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
        content_list = WithDocx.read_paragraph(filename=filepath)
        return render_template('pages/paragraph_page.html', filename=filename, content_list=content_list)

    @app.route('/uploads/file_page_structure/<filename>')
    def file_page_structure(filename):
        filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
            _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
        file_margin = WithDocx.read_page_structure(filename=filepath)
        _checkMargin = CheckTrue.checkMargin
        return render_template('pages/file_page_structure_page.html', _checkMargin=_checkMargin, filename=filename, file_margin=file_margin)

    @app.route('/uploads/file_alignment_and_indent/<filename>')
    def file_alignment_and_indent(filename):
        filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
            _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
        file_indent = WithDocx.read_alignment_and_indent(filename=filepath)
        file_alignment = WithDocx.read_alignment(filename=filepath)
        return render_template('pages/file_alignment_and_indent_page.html', filename=filename,  file_indent=file_indent, file_alignment=file_alignment)

    @app.route('/uploads/file_table/<filename>')
    def file_table(filename):
        filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
            _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
        file_table = WithDocx.read_table(filename=filepath)
        return render_template('pages/file_tables_page.html', filename=filename, file_table=file_table)

    @app.route('/uploads/file_resources/<filename>')
    def file_resources(filename):
        filepath = '{_UPLOAD_FOLDER}/{_filename}'.format(
            _UPLOAD_FOLDER=UPLOAD_FOLDER, _filename=filename)
        file_resources = WithDocx.read_resources(filename=filepath)

        return render_template('pages/file_resources_page.html', filename=filename, file_resources=file_resources)


if __name__ == '__main__':
    app.run(debug=True)
