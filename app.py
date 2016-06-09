from flask import Flask, request, url_for, render_template, redirect, jsonify
import pycld2 as cld2

app = Flask(__name__)


@app.route('/')
def show_home():
    '''
    Render Home page
    '''
    return render_template('home.html')


@app.route('/compute', methods=['POST'])
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
        output = {'reliablity': reliability, 'lang': lang, 'match': match}
        return render_template('find.html', **output)


@app.route('/api/<string:sentence>/', methods=['GET'])
def apiResult(sentence):
    '''Checks the language of sentence.

    Returns JSON response that looks like this
        {
        "lang": "SWAHILI",
        "match": "95.0000 %",
        "reliablity": true
        }
    '''
    cleanSentence = sentence.split('+')
    cleanSentence = ' '.join(cleanSentence)
    get1, get2, get3 = cld2.detect(sentence)
    reliability = (get1)
    lang = (get3[0][0])
    match = ('{0:.4f} %'.format(get3[0][2]))
    output = {'reliablity': reliability, 'lang': lang, 'match': match}
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
