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

def verify_duplicity_email():

    # Verificação de duplicidade de cadastro
    cursor = banco.cursor()
    query = f'SELECT * FROM usuarios'
    cursor.execute(query)
    all_data = cursor.fetchall() # Todos os registros em matriz
    email = register.lineEdit_5.text() # E-mail digitado
    print(f'E-mail digitado: {email}')

    # Isolamento dos e-mail do banco de dados da matriz
    x = 0
    email = register.lineEdit_5.text()
    for x in range (0,len(all_data)):
        email_to_confirm = all_data[x][4] # E-mails registrados listados em coluna
        print(f"E-mails registrados: {email_to_confirm}")

        if email_to_confirm == email:
            print(f"E-mail repetido: {email}")
            return False
        else:
            print("Nenhuma repetição")
            return True

        x += 1


def do_register():

    # Cadastrar novo user
    
    name = register.lineEdit.text()
    login_name = register.lineEdit_2.text()
    password = register.lineEdit_3.text()
    password_to_confirm = register.lineEdit_4.text()
    email = register.lineEdit_5.text()

    if password == password_to_confirm:
        # Senhas se confirmam

        try:
            if ({name} == ' ' or {login_name} == ' ' or {password} == ' ' or {password_to_confirm} == ' ' or {email == ' '}):

                register.label_2.setText('Favor preencher todos os campos.')
            else:

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


def execute_register():
    name = main.lineEdit.text()
    cpf_cnpj = main.lineEdit_2.text()
    apel = main.lineEdit_3.text()
    email = main.lineEdit_4.text()
    tel = main.lineEdit_11.text()
    ender = main.lineEdit_5.text()
    number = main.lineEdit_6.text()
    neigh = main.lineEdit_7.text()
    complement = main.lineEdit_8.text()
    city = main.lineEdit_9.text()
    uf = main.lineEdit_10.text()
    cep = main.lineEdit_12.text()

    if ((name == '') or (cpf_cnpj == '') or (email == '') or (tel == '') or (ender == '') or (number == '') or (neigh == '') or (city == '') or (uf == '') or (cep == '')):
        main.label_2.setText('Há dados faltantes.')
    else:

        cursor = banco.cursor()
        query = f"INSERT INTO fornecedores (nome, CPFouCNPJ, apelido, cep, endereco, numero, bairro, complemento, cidade, uf, telefone, email) VALUES ('{name}', '{cpf_cnpj}', '{apel}', '{cep}', '{ender}', '{number}', '{neigh}', '{complement}', '{city}', '{uf}', '{tel}', '{email}')"
        print(query)
        cursor.execute(query)
        banco.commit()
        main.label_2.setText('Cadastro realizado!')

        # Limpeza
        name = main.lineEdit.setText('')
        cpf_cnpj = main.lineEdit_2.setText('')
        apel = main.lineEdit_3.setText('')
        email = main.lineEdit_4.setText('')
        tel = main.lineEdit_11.setText('')
        ender = main.lineEdit_5.setText('')
        number = main.lineEdit_6.setText('')
        neigh = main.lineEdit_7.setText('')
        complement = main.lineEdit_8.setText('')
        city = main.lineEdit_9.setText('')
        uf = main.lineEdit_10.setText('')
        cep = main.lineEdit_12.setText('')

def show_register_list():

    main.close()
    register_list.show()
    cursor = banco.cursor()
    query = "SELECT * FROM fornecedores"
    cursor.execute(query)
    data = cursor.fetchall()
    
    # Montagem da tabela no formulário
    register_list.tableWidget.setRowCount(len(data))
    register_list.tableWidget.setColumnCount(13)

    # Inserção da dados na tabela
    for i in range (0,len(data)): # Número de linhas
        for j in range (0,13): # Número de colunas
            register_list.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(data[i][j])))


def show_update():

    update.show()
    # Número da linha desejada para edição dos dados
    number_line = register_list.tableWidget.currentRow()

    # Reescrever na tela as informações do ID para modificações
    cursor = banco.cursor()
    query = 'SELECT id FROM fornecedores'
    cursor.execute(query)
    all_data = cursor.fetchall()
    id = all_data[number_line][0]
    
    # Obtenção das informações do referido ID
    cursor = banco.cursor()
    query = f'SELECT * FROM fornecedores WHERE id = {id}'
    cursor.execute(query)
    all_data_by_id = cursor.fetchall()
    print(all_data_by_id)

    # Obtenção dos valores referente às variáveis
    name = all_data_by_id[0][1]
    cpf_cnpj = all_data_by_id[0][2]
    apel = all_data_by_id[0][3]
    cep = all_data_by_id[0][4]
    ender = all_data_by_id[0][5]
    number = all_data_by_id[0][6]
    neigh = all_data_by_id[0][7]
    complement = all_data_by_id[0][8]
    city = all_data_by_id[0][9]
    uf = all_data_by_id[0][10]
    tel = all_data_by_id[0][11]
    email = all_data_by_id[0][12]

    # Preenchimento dos campos para edição
    update.lineEdit.setText(name)
    update.lineEdit_2.setText(str(cpf_cnpj))
    update.lineEdit_3.setText(apel)
    update.lineEdit_4.setText(str(email))
    update.lineEdit_5.setText(ender)
    update.lineEdit_6.setText(str(number))
    update.lineEdit_7.setText(neigh)
    update.lineEdit_8.setText(str(complement))
    update.lineEdit_9.setText(city)
    update.lineEdit_10.setText(uf)
    update.lineEdit_11.setText(str(tel))
    update.lineEdit_12.setText(str(cep))

def save():

    # Obtenção do ID
    cursor = banco.cursor()
    query = 'SELECT id FROM fornecedores'
    cursor.execute(query)
    all_data = cursor.fetchall()
    number_line = register_list.tableWidget.currentRow()
    id = all_data[number_line][0]

    # Adaptações nas caixas de texto
    name = update.lineEdit.text()
    cpf_cnpj = update.lineEdit_2.text()
    apel = update.lineEdit_3.text()
    email = update.lineEdit_4.text()
    ender = update.lineEdit_5.text()
    number = update.lineEdit_6.text()
    neigh = update.lineEdit_7.text()
    complement = update.lineEdit_8.text()
    city = update.lineEdit_9.text()
    uf = update.lineEdit_10.text()
    tel = update.lineEdit_11.text()
    cep = update.lineEdit_12.text()

    cursor = banco.cursor()
    query = f"UPDATE fornecedores SET nome = '{name}', CPFouCNPJ = '{cpf_cnpj}', apelido = '{apel}', cep = '{cep}', endereco = '{ender}', numero = '{number}', bairro = '{neigh}', complemento = '{complement}', cidade = '{city}', uf = '{uf}', telefone = '{tel}', email = '{email}' WHERE id = '{id}'"
    print(query)
    cursor.execute(query)
    banco.commit()

def delete():

    # Obtenção do ID
    cursor = banco.cursor()
    query = 'SELECT id FROM fornecedores'
    cursor.execute(query)
    all_data = cursor.fetchall()
    number_line = register_list.tableWidget.currentRow()
    register_list.tableWidget.removeRow(number_line)
    id = (all_data[number_line][0])

    cursor = banco.cursor()
    query = f"DELETE FROM fornecedores WHERE id = '{str(id)}'"
    cursor.execute(query)
    banco.commit()
    quest_delete.close()
    register_list.show()



# Controle de telas
def show_do_register():
    login.close()
    register.show()

def back_to_login():
    register.close()
    login.show()

def do_register_after_verify():
    if verify_duplicity_email():
        do_register()
    else:
        register.label_2.setText('E-mail já cadastrado.')

def show_main_form():
    login.close()
    main.show()


def logout():
    main.close()
    login.show()

def back_to_main():
    register_list.close()
    update.close()
    main.show()

def show_update_form():
    register_list.close()
    show_update()

def back_to_register_list():
    update.close()
    quest_delete.close()
    register_list.show()

def save_changes():
    save()
    back_to_register_list()

def quest_to_delete():
    quest_delete.show()



app = QtWidgets.QApplication([])
# Importação das telas
login = uic.loadUi('login.ui')
register = uic.loadUi('register.ui')
main = uic.loadUi('main.ui')
register_list = uic.loadUi('register_list.ui')
update = uic.loadUi('update.ui')
quest_delete = uic.loadUi('quest_delete.ui')

# Chamadas
login.pushButton.clicked.connect(show_main_form)
login.pushButton_2.clicked.connect(show_do_register) # Chama a tela de registro
#______________________________________
register.pushButton_2.clicked.connect(back_to_login)
register.pushButton.clicked.connect(do_register_after_verify)
#______________________________________
main.pushButton_2.clicked.connect(execute_register)
main.pushButton_3.clicked.connect(logout)
main.pushButton_4.clicked.connect(show_register_list)
#______________________________________
register_list.pushButton_2.clicked.connect(back_to_main)
register_list.pushButton_3.clicked.connect(show_update_form)
register_list.pushButton_4.clicked.connect(quest_to_delete)
#_______________________________________
update.pushButton_3.clicked.connect(back_to_main)
update.pushButton_2.clicked.connect(save_changes)
#________________________________________
quest_delete.pushButton_4.clicked.connect(delete)
quest_delete.pushButton_3.clicked.connect(back_to_register_list)





# Start do Sistema
login.show()
app.exec()
