from PyQt5 import uic, QtWidgets
import mysql.connector
import sqlite3

# Conexão com o Banco de Dados

banco = mysql.connector.connect(

    host='127.0.0.1',
    user='root',
    password='',
    database='fornecedores'

)

def do_login():

    # Login no sistema
    login.lineEdit.setText('')
    user = login.lineEdit.text()
    password = login.lineEdit_2.text()

def do_register():

    # Cadastrar novo user
    
    name = register.lineEdit.text()
    login_name = register.lineEdit_2.text()
    password = register.lineEdit_3.text()
    password_to_confirm = register.lineEdit_4.text()
    email = register.lineEdit_5.text()

    if password == password_to_confirm:
        # Senhas se confirmam

        # Verificação de duplicidade de cadastro
        cursor = banco.cursor()
        query = f'SELECT * FROM usuarios'
        cursor.execute(query)
        all_data = cursor.fetchall()

        cont = 0
        for email_to_confirm in range (0,len(all_data)):
            email_to_confirm = all_data[cont][4]
            print(email_to_confirm)
            cont += 1
            if email_to_confirm == email:
                print(f'E-mail repetido: {email_to_confirm}')
            else:
                print('Não há e-mails duplicados.')
             

        try:
            cursor = banco.cursor()
            query = f"INSERT INTO usuarios (nome, login, senha, email) VALUES ('{name}', '{login_name}', '{password}', '{email}')"
            cursor.execute(query)
            banco.commit()
            register.label_2.setText('Registro efetuado com sucesso!')

            # Limpa os dados
            name = register.lineEdit.setText('')
            login_name = register.lineEdit_2.setText('')
            password = register.lineEdit_3.setText('')
            password_to_confirm = register.lineEdit_4.setText('')
            email = register.lineEdit_5.setText('')

        except sqlite3.Error as erro:
            print('Erro no cadastro de novos usuários: ',erro)
            register.label_2.setText('Ops... algo de errado aconteceu.')

    else:
        register.label_2.setText('As senhas são diferentes.')


# Controle de telas
def show_do_register():
    login.close()
    register.show()

def back_to_login():
    register.close()
    login.show()



app = QtWidgets.QApplication([])
# Importação das telas
login = uic.loadUi('login.ui')
register = uic.loadUi('register.ui')

# Chamadas
login.pushButton_2.clicked.connect(show_do_register) # Chama a tela de registro
#______________________________________
register.pushButton_2.clicked.connect(back_to_login)
register.pushButton.clicked.connect(do_register)


# Start do Sistema
login.show()
app.exec()
