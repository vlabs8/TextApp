from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///texts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_text", methods=["GET", "POST"])
def add_text():
    if request.method == "POST":
        name = request.form["name"]
        content = request.form["content"]
        new_text = Text(name=name, content=content)
        db.session.add(new_text)
        db.session.commit()
        return redirect(url_for("text_page", text_id=new_text.id))
    return render_template("add_text.html")

@app.route("/all_texts")
def all_texts():
    texts = Text.query.all()
    return render_template("texts_list.html", texts=texts)

@app.route("/text_page/<int:text_id>")
def text_page(text_id):
    text = Text.query.get_or_404(text_id)
    return render_template("text_page.html", text=text)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

