import UDPPipe
import threader
from flask import Flask, request, render_template, session
import csv
import hashlib
app = Flask(__name__)
app.secret_key = hashlib.md5(b"hello").digest()

@app.route('/runsa', methods=['GET', 'POST'])
def buttonclick1():
    #x1 = 'data/toparse.txt'
    x1 = request.form.get("filepath")
    outputtext = UDPPipe.run(x1)
    session['ops'] = outputtext
    return render_template('results.html',outputtext=outputtext)

@app.route('/runsab', methods=['GET', 'POST'])
def sabatch():
    x1 = request.form.get("filepath")
    rv = threader.threadWalk(x1)
    print(rv)
    return render_template('results.html',outputtext=rv)

@app.route('/runla', methods=['GET', 'POST'])
def buttonclick2():
        x1 = request.form.get("filepath")
        outputtext = UDPPipe.run(x1)

        return render_template('results.html',outputtext=outputtext)
@app.route('/returntomain', methods=['GET', 'POST'])
def bc2():
    return render_template('main.html');

@app.route('/exp', methods=['GET', 'POST'])
def exp():
    outputtext = session['ops']
    csv_file = "results/exportedsa.csv"
    try:
        with open('exportedsa', 'w') as f:
            for key in outputtext.keys():
                f.write("%s,%s\n"%(key,outputtext[key]))
    except IOError:
        print("FAILED")
    return render_template('results.html', outputtext=outputtext)

@app.route("/")
def runnable():
    session['ops'] = 0
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=9874)
