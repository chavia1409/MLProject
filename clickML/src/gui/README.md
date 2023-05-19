## Getting Started
Wenn du virtualenv nicht installiert hast:

    python -m pip install --upgrade pip setuptools virtualenv

Je nach installation von python musst du anstatt 'python' 'python3' benutzen

1. Create the virtual environment named kivy_venv in your current directory:

        python -m virtualenv kivy_venv

2. Activate the virtual environment.

    Win CMD

        kivy_venv\Scripts\activate

    Win bash terminal

        source kivy_venv/Scripts/activate

    linux or macOS

        source kivy_venv/bin/activate
3. Install Kivy

        python -m pip install "kivy[base]"

4. Install some additional packages

        pip install varname
        python -m pip install git+https://github.com/HeaTTheatR/KivyMD.git
5. Start App

        python ./clickmlapp.py
