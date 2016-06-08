from flask import Flask, request, url_for, render_template, redirect
import pycld2 as cld2

app = Flask(__name__)


@app.route('/')
def show_home():
    '''
    Render Home page
    '''
    return render_template('home.html')


@app.route('/compute', methods=['POST', 'GET'])
def result():
    '''
    Get language,reliabilty percentage and match
    '''
    if request.method == 'POST':
        if not request.form['word']:
            return redirect(url_for('show_home'))
        data = str(request.form['word'])
        get1, get2, get3 = cld2.detect(data)
        reliability = (get1)
        lang = (get3[0][0])
        match = ('{0:.4f} %'.format(get3[0][2]))
        return render_template('find.html', reliability=reliability, lang=lang, match=match)


if __name__ == '__main__':
    app.run(debug=True)
