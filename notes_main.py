import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog,QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,QTextEdit,QListWidget,QLineEdit

notes = {"Добро пожаловать":{
    "текст":"Это самое лучшее приложение для заметок в мире!","теги":["добро","инструкция"]}
    }
'''with open("notes_data.json","w") as file:
    json.dump(notes, file, sort_keys=True)'''
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Умные замтки')
main_win.resize(600,400)

create = QPushButton('Создать заметку')
find = QPushButton('Искать заметку по тегу')
editteg = QPushButton('Добавить к заметке')
otkrepit = QPushButton('Открепить от заметки')
text = QTextEdit()
spisoktegov = QListWidget()
delzam = QPushButton('Удалить заметку')
vvtef = QLineEdit()
saveteg = QPushButton('Сохранить заметку')
label1 = QLabel('Список заметок')
label2 = QLabel('Список тегов')
spisokzam = QListWidget() 

vvtef.setPlaceholderText('Введите тег...')

hline = QHBoxLayout()
vline = QVBoxLayout()
hline.addLayout(vline)
vline.addWidget(text)
vline2 = QVBoxLayout()
hline.addLayout(vline2)
vline2.addWidget(label1)
vline2.addWidget(spisokzam)
hline2 = QHBoxLayout()
hline2.addWidget(create)
hline2.addWidget(delzam)
vline2.addLayout(hline2)
vline2.addWidget(saveteg)
vline2.addWidget(label2)
vline2.addWidget(spisoktegov)
vline2.addWidget(vvtef)
hline3 = QHBoxLayout()
hline3.addWidget(editteg)
hline3.addWidget(otkrepit)
vline2.addLayout(hline3)
vline2.addWidget(find)

main_win.setLayout(hline)

def show_note():
    name = spisokzam.selectedItems()[0].text()
    text.setText(notes[name]['текст'])
    spisoktegov.clear()
    spisoktegov.addItems(notes[name]['теги'])

spisokzam.itemClicked.connect(show_note)

def add_note():
    not_name, ok = QInputDialog.getText(main_win,'Добавить заметку','Название заметки')
    if ok and not_name != '':
        notes[not_name] = {'текст':'','теги':[]}
        spisokzam.addItem(not_name)
        spisoktegov.addItems(notes[not_name]['теги'])

def save_note():
    if spisokzam.selectedItems():
        key = spisokzam.selectedItems()[0].text()
        notes[key]['текст'] = text.toPlainText()
        with open ('notes_data.json','w',) as file:
            json.dump(notes,file,sort_keys = True)
def del_note():
    if spisokzam.selectedItems():
        key = spisokzam.selectedItems()[0].text()
        del notes[key]
        spisokzam.clear()
        spisoktegov.clear()
        text.clear()
        spisokzam.addItems(notes)
        with open ('notes_data.json','w',) as file:
            json.dump(notes,file,sort_keys = True)

def add_tag():
    if spisokzam.selectedItems():
        key = spisokzam.selectedItems()[0].text()
        tag = vvtef.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            spisoktegov.addItem(tag)
            vvtef.clear()
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        print("Заметка для добавлуния тега не выбрана.")

def del_tag():
    if spisokzam.selectedItems():
        key = spisokzam.selectedItems()[0].text()
        tag = spisoktegov.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        spisoktegov.clear()
        spisoktegov.addItems(notes[key]["теги"])
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True)

def search_tag():
    tag = vvtef.text()
    if find.text() == 'Искать заметку по тегу' and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note]=notes[note]
        find.setText('Сбросить поиск')
        spisokzam .clear()
        spisoktegov.clear()
        spisokzam.addItems(notes_filtered)
    elif find.text() == 'Сбросить поиск':
        vvtef.clear()
        spisokzam.clear()
        spisoktegov.clear()
        spisokzam.addItems(notes)
        find.setText('Искать заметку по тегу')
    else:
        pass


create.clicked.connect(add_note)
saveteg.clicked.connect(save_note)
delzam.clicked.connect(del_note)
editteg.clicked.connect(add_tag)
otkrepit.clicked.connect(del_tag)
find.clicked.connect(search_tag)

main_win.show()
with open ('notes_data.json','r') as file:
   notes = json.load(file)
spisokzam.addItems(notes)
app.exec_()