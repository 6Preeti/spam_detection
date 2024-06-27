from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

nb = pickle.load(open("Naive_model.pkl","rb"))

@app.route('/', methods=["GET","POST"])
def main_function():
    if request.method == "POST":
        text = request.form['email']
        emails = [text]
        output = nb.predict(emails)
        print(output)
        return render_template("show.html", prediction = output)
    
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)