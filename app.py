from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)  #  App 

# App home page decorator by (/) 
@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    percentage = (score / 100) * 100  # Calculate the percentage
    
    if score >= 50:
        res = "PASS" 
    else:
        res="FAIL"
    return render_template('success.html', result=res, percentage=percentage)

## check the result
@app.route('/results/<int:score>')
def results(score):
    
    if score >= 50:
        result = "PASS" 
    else:
        result="FAIL"
    return render_template('result.html', result=result, score=score)


## The result checker html 
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        python = float(request.form['python'])
        machinelearning = float(request.form['machinelearning'])
        stats = float(request.form['stats'])
        datascience = float(request.form['datascience'])
        total_score = (python + machinelearning + stats + datascience) / 4
        return redirect(url_for('results', score=total_score))
    else:
        return redirect(url_for('welcome'))
    



if __name__ == '__main__':
    app.run(debug=True)



