from flask import request, render_template, redirect, session, Flask
import datetime
from finance import append_data, show_data, delete_row, reset

app = Flask(__name__)

@app.route('/')
def home():
    data, total, saved, spent = show_data()

    return render_template('index.html', data=data, total=total, saved=saved, spent=spent)

@app.route('/post', methods=["GET", "POST"])
def add_cost():
    if request.method=="GET":
        return render_template('post.html')
    if request.method=="POST":
        type=request.form.get("type")
        cost=request.form.get('cost')
        description = request.form.get('desc')
        append_data(type, cost, description)
        return redirect('/')

@app.route('/view')
def viewall():
    data, total, saved, spent = show_data()
    return render_template('view.html', data=data, total=total, saved=saved, spent=spent)

@app.route("/delete/<row>")
def delete(row):
    delete_row(row)
    return redirect("/view")

@app.route('/reset')
def reset_book():
    reset()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)