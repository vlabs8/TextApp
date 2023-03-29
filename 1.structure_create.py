"""
Python script that creates a root folder named demo and generates the necessary file structure for the project within the demo folder

demo
├── instance
    └── texts.db
├── js
│   └── main.js
├── static
│   └── css
│       └── style.css
├── templates
│   ├── add_text.html
│   ├── base.html
│   ├── home.html
│   ├── index.html
│   ├── text_page.html
│   └── texts_list.html
└── app.py


"""


import os

root_folder = "demo"

# Create directories
dirs = [
    root_folder,
    f'{root_folder}/static',
    f'{root_folder}/static/css',
    f'{root_folder}/static/js',
    f'{root_folder}/templates',
]

for directory in dirs:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create empty files
files = [
    (f'{root_folder}/app.py', ''),
    (f'{root_folder}/static/css/style.css', ''),
    (f'{root_folder}/static/js/main.js', ''),
    (f'{root_folder}/templates/base.html', ''),
    (f'{root_folder}/templates/index.html', ''),
    (f'{root_folder}/templates/text_page.html', ''),
]

for file_path, content in files:
    with open(file_path, 'w') as file:
        file.write(content)

print("File structure created successfully in 'demo' folder.")
