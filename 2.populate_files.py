# A Python script that generates the necessary content for the app.py file within the demo folder

app_py_content = '''from flask import Flask, render_template, request, redirect, url_for
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

'''

with open('demo/app.py', 'w') as app_py_file:
    app_py_file.write(app_py_content)

print("Content generated for 'demo/app.py'.")



with open('demo/app.py', 'w') as app_py_file:
    app_py_file.write(app_py_content)

######
# A Python script that generates the necessary content for the style.css file within the demo folder

style_css_content = '''body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

form {
    margin-bottom: 2rem;
}

input[type="text"] {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
}

input[type="submit"] {
    display: inline-block;
    background-color: #007bff;
    color: white;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border: none;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #0056b3;
}
'''

with open('demo/static/css/style.css', 'w') as style_css_file:
    style_css_file.write(style_css_content)

######

# A Python script that generates the necessary content for the main.js file within the demo folder:

main_js_content = '''document.addEventListener('DOMContentLoaded', function() {
    // Add any JavaScript code here
});
'''

with open('demo/static/js/main.js', 'w') as main_js_file:
    main_js_file.write(main_js_content)

######
base_html_content = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <script src="{{ url_for('static', filename='js/main.js') }}" defer></script>
    <title>{{ title }}</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="{{ url_for('home') }}">TextApp</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="{{ url_for('home') }}">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{ url_for('add_text') }}">Add Text</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{ url_for('all_texts') }}">All Texts</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <main class="container mt-4">
      {% block content %}{% endblock %}
    </main>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>
  </body>
</html>

'''

with open('demo/templates/base.html', 'w') as base_html_file:
    base_html_file.write(base_html_content)


home_html_content = '''
{% extends "base.html" %}

{% block content %}
  <h1>TextApp: A Simple Text Management Application</h1>
  <p>Welcome to TextApp, a web-based application built using Flask, a lightweight Python web framework. This app allows users to manage texts by adding new texts, viewing existing texts, and navigating through a collection of texts within the web application.</p>

  <h2>Functionalities</h2>
  <ul>
    <li><strong>Home page (Project Description):</strong> The home page displays a brief description of the project, explaining its purpose and basic functionalities.</li>
    <li><strong>Add Text:</strong> This feature allows users to add new texts to the application. Users can input a name and the content of the text, then submit the information. The text data is then stored in a database for future reference.</li>
    <li><strong>All Texts:</strong> This page lists all the texts that have been added to the app. Each text in the list is displayed as a link, which leads to the individual text page.</li>
    <li><strong>Text Page:</strong> When a user clicks on a text link in the "All Texts" page, they are directed to a dedicated page for that specific text. The text page displays the name and the content of the text.</li>
  </ul>

  <p>The app uses Flask for handling HTTP requests and rendering HTML templates, while SQLite is used as the database for storing the texts. The front-end is designed using the Bootstrap CSS framework, which provides a clean and responsive user interface.</p>
{% endblock %}

'''

with open('demo/templates/home.html', 'w') as home_html_file:
    home_html_file.write(home_html_content)


add_text_html_content = '''
{% extends "base.html" %}

{% block content %}
  <h2>Add Text Functionality</h2>
  <form action="{{ url_for('add_text') }}" method="post">
    <div class="mb-3">
      <label for="name" class="form-label">Name</label>
      <input type="text" class="form-control" id="name" name="name" required>
    </div>
    <div class="mb-3">
      <label for="content" class="form-label">Content</label>
      <textarea class="form-control" id="content" name="content" rows="3" required></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
{% endblock %}
'''

with open('demo/templates/add_text.html', 'w') as add_text_html_file:
    add_text_html_file.write(add_text_html_content)


texts_list_html_content = '''
{% extends "base.html" %}

{% block content %}
    <h2>All the Texts Added List</h2>
    <ul class="list-group">
        {% for text in texts %}
            <li class="list-group-item">
                <a href="{{ url_for('text_page', text_id=text.id) }}">{{ text.name }}</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
'''

with open('demo/templates/texts_list.html', 'w') as texts_list_html_file:
    texts_list_html_file.write(texts_list_html_content)

text_page_html_content = '''{% extends "base.html" %}

{% block content %}
    <h2>{{ text.name }}</h2>
    <p>{{ text.content }}</p>
    <a href="{{ url_for('all_texts') }}">Back to All Texts</a>
{% endblock %}


'''
with open('demo/templates/text_page.html', 'w') as text_page_html_file:
    text_page_html_file.write(text_page_html_content)
