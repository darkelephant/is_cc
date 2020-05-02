import os
from flask import Flask, request, redirect, url_for
# from flask import send_from_directory


basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = {
    'txt', 'pdf', 'png', 'jpg', 'jpeg',
    'gif', 'doc', 'docx', 'xlsx'
}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(os.path.join(basedir, file.filename))
            link_to_file = os.path.join(basedir, file.filename)
            print(link_to_file)
            return redirect(url_for('upload_file'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)
