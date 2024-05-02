# GeoQuiz
Study and get quizzed on world geography.
<br><br>
## Installation
1. [Install python](https://www.python.org/downloads/)
2. [Download GeoQuiz](https://github.com/EthanSDD/GeoQuiz/archive/refs/heads/main.zip) and extract the zip
3. On Windows run `Install.bat` then `GeoQuiz.py`, else resort to one of the manual methods below.

### Windows
```
py -m ensurepip --upgrade
python -m venv MyEnv
.\MyEnv\scripts\activate
pip install customtkinter
pip install pillow
python GeoQuiz.py
```
### Linux / MacOs / Unix
```
python -m ensurepip --upgrade
python -m venv MyEnv
source MyEnv/bin/activate
pip install customtkinter
pip install pillow
python GeoQuiz.py
```
For Debian / Ubuntu tkinter must be installed prior
```
sudo apt update
sudo apt install python-tk
```

## Acknowledgements
[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
[Pillow](https://github.com/python-pillow/Pillow)
