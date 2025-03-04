import sys
from datetime import datetime

# Imports bibliotecas
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QMessageBox, QTreeWidgetItem)
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QBrush, QColor
import mysql.connector

# Imports de interfaces gráficas
from Ui_Login import Ui_Login
from Ui_Menu_Vendas import Ui_MenuVendas
from Ui_Adicionar_Itens import Ui_Adicionar
from UI_AdicionarClientes import Ui_AddClientes
from Ui_AddSpecsItens import Ui_addspecs
from Ui_Verificarclientesp1 import Ui_Verify1
from Ui_Verificarclientesp2 import Ui_Verify2
from UI_MP_Engenharia import Ui_MP_Engenharia
from UI_Verificar_MP import Ui_Verificar_MP
from UI_ADD_MP_Engenharia import Ui_ADD_MP
from UI_Remover_MP import UI_REMOVE_MP
from UI_PCP_OS import Ui_PCP_OS
from UI_PCP_Estoque import Ui_PCP_Estoque
from UI_Compras_Inicio import UI_Compras_Inicio
from UI_AdicionarFornecedor import Ui_AdicionarFornecedor
from UI_VerificarFornecedor import UI_VerificarFornecedor
from UI_Compras_OS import UI_Compras_OS
from UI_Compras_Estoque import UI_Compras_Estoque
from UI_Compras_Preencher import UI_Compras_Preencher
from UI_Vendas_OS_Check import UI_Vendas_OS
from UI_Vendas_Check import Ui_Vendas_Check
from UI_Engenharia_Check import UI_Engenharia_Check
from UI_Engenharia_OS import UI_Engenharia_OS
from UI_Compras_Check import UI_Compras_Check
from UI_Compras_OS_Check import UI_Compras_OS_Check
from UI_PCP_OS_CHECK import UI_PCP_OS_CHECK
from UI_PCP_Check import UI_PCP_Check
from UI_Vendas_PCP_Check import Ui_Vendas_PCP_Check
from UI_PCP_Engenharia import UI_PCP_Engenharia
from UI_PCP_Compras import UI_PCP_Compras
from UI_Vendas_PCP_Check import Ui_Vendas_PCP_Check

# Conexão com o banco de dados
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    port = "3306",
    database="controle_fluxo"
)
cursor = mydb.cursor()



#Classe para a janela de login
class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self) -> None:
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Login')
        
       

        # Conectar o botão de login ao método de verificação de credenciais
        self.Btn_Logar.clicked.connect(self.verificar_credenciais)

    # Método para verificar as credenciais do login
    def verificar_credenciais(self):
        match self.Edit_User.text().lower():
            case 'vendas':
                if self.Edit_Pass.text().lower() == 'vendas':
                    # Se login for válido, abre a tela de Menu de Vendas
                    self.w = Menu_Vendas(self)
                    self.w.show()
                    self.close()
                else:
                    # Mensagem de senha incorreta
                    self.Label_Aviso.setText('<div align="center"><font color="red"><b>Senha incorreta!</b></font></div>')
                    QTimer.singleShot(1000, self.restore_label_text)  # Restaura o texto após 1 segundo
            
            case 'engenharia':
                if self.Edit_Pass.text().lower() == 'engenharia':
                    self.w = ADD_ItensMP_Engenharia(self)
                    self.w.show()
                    self.close()
                else:
                    # Mensagem de erro para nome de usuário ou senha incorretos
                    self.Label_Aviso.setText('<div align="center"><font color="red"><b>Verifique o nome de usuário ou a senha!</b></font></div>')
                    QTimer.singleShot(1000, self.restore_label_text)
            case 'pcp':
                if self.Edit_Pass.text().lower() == 'pcp':
                    self.w = PCP_os()
                    self.w.show()
                    self.close()
                else:
                    # Mensagem de erro para nome de usuário ou senha incorretos
                    self.Label_Aviso.setText('<div align="center"><font color="red"><b>Verifique o nome de usuário ou a senha!</b></font></div>')
                    QTimer.singleShot(1000, self.restore_label_text)
            case 'compras':
                if self.Edit_Pass.text().lower() == 'compras':
                    self.w = compras_inicio(self)
                    self.w.show()
                    self.close()
                else:
                    # Mensagem de erro para nome de usuário ou senha incorretos
                    self.Label_Aviso.setText('<div align="center"><font color="red"><b>Verifique o nome de usuário ou a senha!</b></font></div>')
                    QTimer.singleShot(1000, self.restore_label_text)
            case _:
                # Mensagem de usuário incorreto
                self.Label_Aviso.setText('<div align="center"><font color="red"><b>Verifique o nome de usuário ou a senha!</b></font></div>')
                QTimer.singleShot(1000, self.restore_label_text)

    # Método para restaurar o texto da label de aviso após um curto período
    def restore_label_text(self):
        self.Label_Aviso.setText('')  # Ou defina o texto original que deseja exibir
# Classe para a janela do Menu de Vendas
class Menu_Vendas(QMainWindow, Ui_MenuVendas):
    def __init__(self, login_window: LoginWindow):
        super(Menu_Vendas, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Vendas')
        self.login_window = login_window
       

        # Conectar os botões aos métodos correspondentes
        self.Btn_AddItens.clicked.connect(self.open_adicionar_itens)
        self.Btn_Voltar.clicked.connect(self.voltar_para_login)
        self.Btn_AddClientes.clicked.connect(self.open_adicionar_clientes)
        self.Btn_Verify.clicked.connect(self.open_verificar_clientes)  # Novo botão adicionado
        self.Btn_Check.clicked.connect(self.verificar_pedido)
        
        
    # Método para abrir a tela de Adicionar Itens
    def open_adicionar_itens(self):
        self.w = Adicionar_Itens(self)
        self.w.show()
        self.close()

    def verificar_pedido(self):
        self.w = Verificar_Vendas_os(self)
        self.w.show()
        self.close()


    # Método para abrir a tela de Adicionar Clientes
    def open_adicionar_clientes(self):
        self.w = Adicionar_Clientes(self)
        self.w.show()
        self.close()

    # Método para abrir a tela de Verificar Clientes
    def open_verificar_clientes(self):
        self.w = Verificar_Clientes(self)
        self.w.show()
        self.close()

    # Método para voltar à tela de login
    def voltar_para_login(self):
        self.login_window.show()
        self.close()
# Classe para a janela de Verificar a OS das vendas    
class Verificar_Vendas_os(QMainWindow, UI_Vendas_OS):
    def __init__(self, menu_vendas: Menu_Vendas):
        super(Verificar_Vendas_os, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Vendas')
        self.menu_vendas = menu_vendas

        self.Btn_Voltar.clicked.connect(self.voltar_para_menu_vendas)
        self.Btn_Avancar.clicked.connect(self.passar_os)  # Chama o método para passar a os

    def voltar_para_menu_vendas(self):
        self.menu_vendas.show()
        self.close()

    def passar_os(self):
        os_value = self.Edit_OS.text()  
        self.w = Verificar_Vendas_Check(os_value, self)  # Passa o valor de os para a próxima janela
        self.w.show()
        self.close()
# Classe para a janela de Verificar as Vendas        
class Verificar_Vendas_Check(QMainWindow, Ui_Vendas_Check):
    def __init__(self,os, verificar_os: Verificar_Vendas_os):
        super(Verificar_Vendas_Check, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Vendas')
        self.verificar_os = verificar_os
    
        self.Btn_Voltar_os.clicked.connect(self.voltar_para_os)
        
        consulta_cliente = '''
                SELECT os, numero_pedido, vendedor, cnpj_cliente, codigo_item, `desc`, quantidade, unidade, data_prevista, horario_att
                FROM vendas_pedidos 
                WHERE os LIKE %s
                '''
        
        cursor.execute(consulta_cliente, (os,))
        cliente = cursor.fetchall()
        

        for mp in cliente:
    # Cria um QTreeWidgetItem para cada linha de dados
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(mp[0]))  # Coluna 1: ID
            item.setText(1, str(mp[1]))
            item.setText(2, str(mp[2]))
            item.setText(3, str(mp[3]))
            item.setText(4, str(mp[4]))
            item.setText(5, str(mp[5]))
            item.setText(6, str(mp[6]))
            item.setText(7, str(mp[7]))
            item.setText(8, str(mp[8]))
            item.setText(9, str(mp[9]))

            
            for col in range(10): 
                item.setTextAlignment(col, Qt.AlignCenter)

            
            brush = QBrush(QColor(255, 255, 255))  
            for col in range(10):
                item.setForeground(col, brush)

    def voltar_para_os(self):
        self.verificar_os.show()
        self.close()
# Classe para a janela de Adicionar Itens
class Adicionar_Itens(QMainWindow, Ui_Adicionar):
    def __init__(self, menu_vendas: Menu_Vendas):
        super(Adicionar_Itens, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Vendas')
        self.menu_vendas = menu_vendas
       

        # Conectar os botões aos métodos correspondentes
        self.Btn_Voltar.clicked.connect(self.voltar_para_menu_vendas)
        self.Btn_Avancar.clicked.connect(self.adicionar_pedido_bd)

    def adicionar_pedido_bd(self):
        os = self.Edit_OS.text()
        Numero_Pedido = self.Edit_NumeroPedido.text()
        vendedor = self.Edit_Vendedor.text()
        cnpj = self.Edit_CNPJ.text()

        # Fecha a janela atual 
        self.close()

        # Criar e exibir múltiplas instâncias da janela Adicionar_Itens_Especs
        self.janelas = []
        janela_espec = Adicionar_Itens_Especs(os, Numero_Pedido, vendedor, cnpj, self)
        self.janelas.append(janela_espec)
        janela_espec.show()

    def exibir_aviso(self, mensagem):
        self.Label_Aviso.setText(f'<div align="center"><font color="red"><b>{mensagem}</b></font></div>')
        QTimer.singleShot(1000, self.restore_label_text)

    def restore_label_text(self):
        self.Label_Aviso.setText('')  # Ou defina o texto original que deseja exibir

    def voltar_para_menu_vendas(self):
        self.menu_vendas.show()
        self.close()
# Classe para a janela de Adicionar Itens Específicos
class Adicionar_Itens_Especs(QMainWindow, Ui_addspecs):
    def __init__(self, os, Numero_Pedido, vendedor, cnpj, parent_window):
        super(Adicionar_Itens_Especs, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Vendas')
        self.os = os
        self.Numero_Pedido = Numero_Pedido
        self.vendedor = vendedor
        self.cnpj = cnpj
        self.parent_window = parent_window  # Referência à janela pai
       

        # Conectar os botões aos métodos correspondentes
        self.Btn_Adicionar.clicked.connect(self.adicionar_itens_bd)
        self.Btn_Voltar.clicked.connect(self.voltar_para_adicionar_itens)

    def adicionar_itens_bd(self):
        data_atual = datetime.now().strftime("%d/%m/%Y")
        codigo_item = self.Edit_codigo.text()
        descricao = self.Edit_desc.text()
        quantidade = self.validar_quantidade(self.Edit_quantidade.text())
        unidade = self.Edit_unidade.text()
        data_prevista = self.Edit_dataprevista.text()

        if quantidade is None:
            self.exibir_aviso('<div align="center"><font color="red"><b>Quantidade Inválida!</b></font></div>')
            return

        try:
            
            inserir_vendas_pedidos = '''
            INSERT INTO vendas_pedidos 
            (os, codigo_item, quantidade, unidade, data_prevista, vendedor, `desc`, numero_pedido, cnpj_cliente,horario_att) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            dados = (self.os, codigo_item, quantidade, unidade, data_prevista, self.vendedor, descricao, self.Numero_Pedido, self.cnpj,data_atual)
            cursor.execute(inserir_vendas_pedidos, dados)
            mydb.commit()

            # Inserção de Data_Criacao na tabela horarios
            inserir_horario_pedidos = '''
            INSERT INTO horarios 
            (os, vendas, engenharia, pcp, compras) 
            VALUES (%s, %s, "0", "0", "0")
            '''
            dadoshora = (self.os, data_atual)
            cursor.execute(inserir_horario_pedidos, dadoshora)
            mydb.commit()

            # Limpar os campos
            self.Edit_codigo.clear()
            self.Edit_desc.clear()
            self.Edit_quantidade.clear()
            self.Edit_unidade.clear()
            self.Edit_dataprevista.clear()

        except mysql.connector.Error as err:
            print(f"Erro ao inserir dados: {err}")
            mydb.rollback()

    def validar_quantidade(self, quantidade_text):
        try:
            return float(quantidade_text)
        except ValueError:
            return None

    def exibir_aviso(self, mensagem):
        self.label_aviso.setText(f'<div align="center"><font color="red"><b>{mensagem}</b></font></div>')
        QTimer.singleShot(1000, self.restore_label_text)

    def restore_label_text(self):
        self.label_aviso.setText('')  # Ou defina o texto original que deseja exibir

    def voltar_para_adicionar_itens(self):
        self.close()
        self.parent_window.show()  # Mostra a janela pai, que é Adicionar_Itens
# Classe para a janela de Adicionar Clientes
class Adicionar_Clientes(QMainWindow, Ui_AddClientes):
    def __init__(self, menu_vendas: Menu_Vendas):
        super(Adicionar_Clientes, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Vendas')
        self.menu_vendas = menu_vendas
       

        # Conectar os botões aos métodos correspondentes
        self.Btn_Voltar.clicked.connect(self.voltar_para_menu_vendas)
        self.Btn_Avancar.clicked.connect(self.adicionar_cliente_bd)

    # Método para voltar à tela Menu de Vendas
    def voltar_para_menu_vendas(self):
        self.menu_vendas.show()
        self.close()

    # Método para adicionar cliente ao banco de dados
    def adicionar_cliente_bd(self):
        Nome_Empresa = self.Edit_NomeEmpresa.text().strip()
        Telefone = self.Edit_Telefone.text().strip()
        Endereco = self.Edit_Enderecos.text().strip()
        Cep = self.Edit_CEP.text().strip()
        Email = self.Edit_Email.text().strip()
        Inscricao_Estadual = self.Edit_InscricaoEstadual.text().strip()
        Cnpj = self.Edit_CNPJ.text().strip()

        # Verifica se todos os campos estão preenchidos
        if Nome_Empresa and Telefone and Endereco and Cep and Email and Inscricao_Estadual and Cnpj:
            add_table_vendasclientes = '''
            INSERT INTO vendas_clientes
            (nome_empresa, telefone, endereco, cep, email, inscricao_estadual, cnpj)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
            dados = (Nome_Empresa, Telefone, Endereco, Cep, Email, Inscricao_Estadual, Cnpj)
                
            cursor.execute(add_table_vendasclientes, dados)
            mydb.commit()
            
            self.Label_Aviso.setText(f'<div align="center"><font color="green"<b>Cliente adicionado com sucesso</b></font></div>')
            QTimer.singleShot(1000, self.restore_label_text)

        else:
            self.Label_Aviso.setText(f'<div align="center"><font color="red"><b>Verifique os campos inseridos</b></font></div>')
            QTimer.singleShot(1000, self.restore_label_text)

    
       
    def restore_label_text(self):
        self.Label_Aviso.setText('')
# Classe para a janela de Verificar Cliente
class Verificar_Clientes(QMainWindow, Ui_Verify1):
    def __init__(self, menu_vendas: Menu_Vendas):
        super(Verificar_Clientes, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Vendas')
        self.menu_vendas = menu_vendas
       

        # Conectar os botões aos métodos correspondentes
        self.Btn_Voltar.clicked.connect(self.voltar_para_menu_vendas)
        self.Btn_Avancar.clicked.connect(self.verificar_cliente_bd)

    def verificar_cliente_bd(self):
        nome_empresa = self.Edit_OS.text()

    
        try:
            consulta_cliente = '''
            SELECT nome_empresa, telefone, cep,  email, endereco, inscricao_estadual
            FROM vendas_clientes 
            WHERE cnpj = %s
            '''
            cursor.execute(consulta_cliente, (nome_empresa,))
            cliente = cursor.fetchall()

            if cliente:
                # Passar dados para a janela verify2
                self.w = Verificar_Clientes2(cliente, self)
                self.w.show()
                self.close()
            
        except mysql.connector.Error as err:
            print(f"Erro ao consultar cliente: {err}")

    

    def voltar_para_menu_vendas(self):
        self.menu_vendas.show()
        self.close()
# Classe para a janela de Verificar Cliente (p2)
class Verificar_Clientes2(QMainWindow, Ui_Verify2):
    def __init__(self, cliente, parent_window):
        super(Verificar_Clientes2, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Vendas')
        self.parent_window = parent_window
       

        # Desempacotar dados do cliente
       
        self.treeWidget.clear()  # Limpa a treeWidget antes de adicionar novos dados

        for mp in cliente:
            # Cria um QTreeWidgetItem para cada linha de dados
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(mp[0]))  # Coluna 1: ID
            item.setText(1, str(mp[1]))
            item.setText(2, str(mp[2]))
            item.setText(3, str(mp[3]))
            item.setText(4, str(mp[4]))
            item.setText(5, str(mp[5]))
            

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            item.setTextAlignment(4, Qt.AlignCenter)
            item.setTextAlignment(5, Qt.AlignCenter)
            


        

        # Conectar botões aos métodos correspondentes
        self.Btn_Voltar.clicked.connect(self.voltar_para_verificar_clientes)

    def voltar_para_verificar_clientes(self):
        self.parent_window.show()
        self.close()
# Classe para a janela de Adicionar Matérias Primas
class ADD_ItensMP_Engenharia(QMainWindow, Ui_MP_Engenharia):
    def __init__(self, menu_vendas: Menu_Vendas):
        super(ADD_ItensMP_Engenharia, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Engenharia')
        self.menu_vendas = menu_vendas
       

        self.verificar_mp_engenharia = Verificar_MP_Engenharia(self)
        self.Btn_Voltar.clicked.connect(self.voltar_para_menu_vendas)
        self.Btn_Adicionar.clicked.connect(self.Adicionar)
        self.Btn_Verify.clicked.connect(self.redirecionar_para_verificar_mp)
        self.Btn_Chechar.clicked.connect(self.verificar_engenharia_check)

    def voltar_para_menu_vendas(self):
        self.menu_vendas.show()
        self.close()

    def redirecionar_para_verificar_mp(self):
        self.verificar_mp_engenharia.show()
        self.hide()

    def verificar_engenharia_check(self):
        # Cria uma nova janela que é um QMainWindow
        self.w = Verificar_Engenharia_os(self)  # Passa a janela atual
        self.w.show()
        self.close()

    def Adicionar(self):
        os = self.Edit_OS.text().strip()
        Codigo_Item = self.Edit_CodigoItem.text().strip()
        Codigo_MP = self.Edit_Codigo_MP.text().strip()
        Quantidade = self.Edit_QuantiaMP.text().strip()
        Unidade = self.Edit_Unidade.text().strip()
        data_atual = datetime.now().strftime("%d/%m/%Y")

        # Verifica se todos os campos estão preenchidos
        if os and Codigo_Item and Codigo_MP and Quantidade and Unidade:
            try:
                consulta_descmp = '''   
                    SELECT desc_mp FROM engenharia_mp 
                    WHERE id_mp LIKE %s
                '''
                cursor.execute(consulta_descmp, (Codigo_MP,))
                descricao_mp = cursor.fetchone()
                
                if descricao_mp:  # Verifica se o resultado não é None
                    descricao_mp = descricao_mp[0]  # Extrair o primeiro elemento da tupla
                else:
                    descricao_mp = "Descrição não encontrada"  # Valor padrão se não encontrado

                consulta_desciten = '''
                    SELECT `desc` FROM vendas_pedidos 
                    WHERE codigo_item LIKE %s
                '''
                cursor.execute(consulta_desciten, (Codigo_Item,))
                descricao_item = cursor.fetchone()
                
                if descricao_item:  # Verifica se o resultado não é None
                    descricao_item = descricao_item[0]  # Extrair o primeiro elemento da tupla
                else:
                    descricao_item = "Descrição do item não encontrada"  # Valor padrão se não encontrado

                inserir_vendas_pedidos = '''
                    INSERT INTO engenharia 
                    (os, codigo_item, `desc`, codigo_mp, desc_mp, quantidade, unidade, horario_att) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
                '''

                dados = (os, Codigo_Item, descricao_item, Codigo_MP, descricao_mp, Quantidade, Unidade,data_atual)
                cursor.execute(inserir_vendas_pedidos, dados)
                mydb.commit()

                # Inserção de Data_Criacao na tabela horarios
                inserir_horario_pedidos = '''
                UPDATE horarios
                SET engenharia = %s
                WHERE os LIKE %s;
                '''

                dadoshora = (data_atual, os)
                cursor.execute(inserir_horario_pedidos, dadoshora)
                mydb.commit()

                self.label_8.setText(f'<div align="center"><font color="green"><b>Dados inseridos com sucesso</b></font></div>')
                QTimer.singleShot(1000, self.restore_label_text)

            except mysql.connector.Error as e:
                # Adicionar print de erro para ajudar no debug
                print(f"Erro no banco de dados: {e}")
                self.label_8.setText(f'<div align="center"><font color="red"><b>Erro ao inserir dados</b></font></div>')
                QTimer.singleShot(1000, self.restore_label_text)
        else:
            self.label_8.setText(f'<div align="center"><font color="red"><b>Verifique os dados inseridos</b></font></div>')
            QTimer.singleShot(1000, self.restore_label_text)


    def restore_label_text(self):
        self.label_8.setText('')
# Classe para a janela de Verificar Matérias Primas
class Verificar_MP_Engenharia(QMainWindow, Ui_Verificar_MP):
    def __init__(self, add_itens_mp_engenharia: ADD_ItensMP_Engenharia):
        super(Verificar_MP_Engenharia, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Engenharia')
        self.add_itens_mp_engenharia = add_itens_mp_engenharia
       

        # Conectar botões aos métodos correspondentes
        self.Btn_Voltar.clicked.connect(self.voltar_para_add_mp_engenharia)
        self.Btn_Consultar.clicked.connect(self.consultar_nomes)  
        self.Btn_Adicionar.clicked.connect(self.redirecionar_para_add_mp)  
        self.Btn_Remover.clicked.connect(self.remover_mp_engenharia)

        consulta_materias_primas = '''
            SELECT id_mp, desc_mp
            FROM engenharia_mp 
            
        '''

        cursor.execute(consulta_materias_primas)
        materias_primas = cursor.fetchall()

        self.treeWidget.clear()  # Limpa a treeWidget antes de adicionar novos dados

        for mp in materias_primas:
            # Cria um QTreeWidgetItem para cada linha de dados
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(mp[0]))  # Coluna 1: ID
            item.setText(1, str(mp[1]))  # Coluna 2: Descrição

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            
        

    def voltar_para_add_mp_engenharia(self):
        self.add_itens_mp_engenharia.show()
        self.close()

    def remover_mp_engenharia(self):
        # Criar uma instância da página REMOVE_MP_Engenharia
        self.remover_mp_engenharia = REMOVE_MP_Engenharia(self.add_itens_mp_engenharia)
        
        # Exibe a página de remoção de matéria-prima
        self.remover_mp_engenharia.show()
        
        # Fecha a página atual
        self.close()

    def redirecionar_para_add_mp(self):
        # Cria uma nova instância de ADD_MP_Engenharia usando add_itens_mp_engenharia
        self.add_mp = ADD_MP_Engenharia(self.add_itens_mp_engenharia)
        
        # Exibe a nova página
        self.add_mp.show()
        
        # Fecha a página atual
        self.close()

    def consultar_nomes(self):
        nome_input = self.Edit_Nome.text().strip()  # Obtém o texto do campo de entrada

        # Consulta SQL para buscar as matérias-primas
        consulta_materias_primas = '''
            SELECT id_mp, desc_mp
            FROM engenharia_mp 
            WHERE desc_mp LIKE %s
        '''
        cursor.execute(consulta_materias_primas, (f"%{nome_input}%",))
        materias_primas = cursor.fetchall()

        self.treeWidget.clear()  # Limpa a treeWidget antes de adicionar novos dados

        for mp in materias_primas:
            # Cria um QTreeWidgetItem para cada linha de dados
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(mp[0]))  # Coluna 1: ID
            item.setText(1, str(mp[1]))  # Coluna 2: Descrição

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)

        if not materias_primas:
            QMessageBox.information(self, "Informação", "Nenhuma matéria-prima encontrada.")
# Classe para a janela de linkar Matéria Prima nos itens
class ADD_MP_Engenharia(QMainWindow, Ui_ADD_MP):
    def __init__(self, add_itens_mp_engenharia: ADD_ItensMP_Engenharia):
        super(ADD_MP_Engenharia, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Engenharia')
        self.add_itens_mp_engenharia = add_itens_mp_engenharia
       

        # Usa a instância correta de Verificar_MP_Engenharia
        self.verificar_mp_engenharia = add_itens_mp_engenharia.verificar_mp_engenharia
        
        self.Btn_Voltar.clicked.connect(self.voltar_para_verificar_mp)
        self.Btn_Adicionar.clicked.connect(self.Adicionar)
        
    def voltar_para_verificar_mp(self):
        self.verificar_mp_engenharia.show()
        self.close()  # Fecha a janela atual ao invés de escondê-la

    def Adicionar(self):

        Codigo_MP = self.Edit_CodigoItem.text().strip()
        descricao_mp = self.Edit_OS.text().strip()

        # Verifica se todos os campos estão preenchidos
        if Codigo_MP and descricao_mp:
            inserir_vendas_pedidos = '''
            INSERT INTO engenharia_mp 
            (id_mp, desc_mp) 
            VALUES (%s, %s)
            '''
            dados = (descricao_mp,Codigo_MP)
            cursor.execute(inserir_vendas_pedidos, dados)
            mydb.commit()

            self.label_8.setText(f'<div align="center"><font color="green"><b>Dados inseridos com sucesso</b></font></div>')
            QTimer.singleShot(1000, self.restore_label_text)
        else:
            self.label_8.setText(f'<div align="center"><font color="red"><b>Preencha todos os campos</b></font></div>')
            QTimer.singleShot(1000, self.restore_label_text)

    def restore_label_text(self):
        self.label_8.setText('')
# Classe para a janela de Remover Matérias Primas
class REMOVE_MP_Engenharia(QMainWindow, UI_REMOVE_MP):
    def __init__(self, add_itens_mp_engenharia: ADD_ItensMP_Engenharia):
        super(REMOVE_MP_Engenharia, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Engenharia')
        self.add_itens_mp_engenharia = add_itens_mp_engenharia
       

        # Usa a instância correta de Verificar_MP_Engenharia
        self.verificar_mp_engenharia = add_itens_mp_engenharia.verificar_mp_engenharia
        
        self.Btn_Voltar.clicked.connect(self.voltar_para_verificar_mp)
        self.Btn_Adicionar.clicked.connect(self.Adicionar)
        
    def voltar_para_verificar_mp(self):
        self.verificar_mp_engenharia.show()
        self.close()

    def Adicionar(self):
        Codigo_MP = self.Edit_CodigoMP.text().strip()

        # Verifica se todos os campos estão preenchidos
        if Codigo_MP:
            remover_mp = '''DELETE FROM engenharia_mp WHERE id_mp = %s'''
            cursor.execute(remover_mp, (Codigo_MP,))
            mydb.commit()

            self.label_8.setText(f'<div align="center"><font color="green">Matéria-prima removida com sucesso</font></div>')
            QTimer.singleShot(1000, self.restore_label_text)
        else:
            self.label_8.setText(f'<div align="center"><font color="red">Preencha todos os campos</font></div>')
            QTimer.singleShot(1000, self.restore_label_text)

    def restore_label_text(self):
        self.label_8.setText('')

class Verificar_Engenharia_os(QMainWindow, UI_Engenharia_OS):
    def __init__(self, Engenharia_Menu: Ui_MP_Engenharia):
        super(Verificar_Engenharia_os, self).__init__()
        self.setupUi(self)  # Configura a interface
        self.setWindowTitle('Engenharia')
        self.Engenharia_Menu = Engenharia_Menu

        # Conectar os botões
        self.Btn_Voltar.clicked.connect(self.voltar_para_menu_vendas)
        self.Btn_Avancar.clicked.connect(self.passar_os)  # Chama o método para passar a os

    def voltar_para_menu_vendas(self):
        self.Engenharia_Menu.show()
        self.close()

    def passar_os(self):
        os_value = self.Edit_OS.text()  # Captura o valor da os
        self.w = Verificar_Engenharia_Check(os_value, self)  # Passa o valor da os para a próxima janela
        self.w.show()
        self.close()

class Verificar_Engenharia_Check(QMainWindow, UI_Engenharia_Check):
    def __init__(self,os, verificar_os: Verificar_Engenharia_os):
        super(Verificar_Engenharia_Check, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Engenharia')
        self.verificar_os = verificar_os
    
        self.Btn_Voltar_os.clicked.connect(self.voltar_para_os)
        #self.Btn_Avancar.clicked.connect(self.verificar_pedido)
        consulta_cliente = '''
                SELECT os, codigo_Item, `desc`, codigo_mp, desc_mp, quantidade, unidade, horario_att
                FROM engenharia 
                WHERE os LIKE %s
                '''
        
        cursor.execute(consulta_cliente, (os,))
        cliente = cursor.fetchall()
        

        for mp in cliente:
    # Cria um QTreeWidgetItem para cada linha de dados
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(mp[0]))  # Coluna 1: ID
            item.setText(1, str(mp[1]))
            item.setText(2, str(mp[2]))
            item.setText(3, str(mp[3]))
            item.setText(4, str(mp[4]))
            item.setText(5, str(mp[5]))
            item.setText(6, str(mp[6]))
            item.setText(7, str(mp[7]))
            
            

            # Centralizar o texto em todas as colunas
            for col in range(8):  # Supondo que tenha 10 colunas
                item.setTextAlignment(col, Qt.AlignCenter)

            # Definir a cor branca para o texto
            brush = QBrush(QColor(255, 255, 255))  # Branco (R=255, G=255, B=255)
            for col in range(8):
                item.setForeground(col, brush)

    def voltar_para_os(self):
        self.verificar_os.show()
        self.close()
# Classe para a janela de Passar a os
class PCP_os(QMainWindow, Ui_PCP_OS):
    def __init__(self):
        super(PCP_os, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('PCP')

        # Variável para armazenar o valor do LineEdit
        self.os_Value = ""
        
        # Conectar botões aos métodos correspondentes
        self.Btn_Avancar.clicked.connect(self.avancar_para_estoque)
        self.Btn_Voltar_Login.clicked.connect(self.voltar_pg)
        self.Btn_Checar.clicked.connect(self.verificar_pcp_os_check)


    def avancar_para_estoque(self):
        self.os_Value = self.Edit_OS.text().strip()
        

        if self.os_Value:
            self.compras_itens = PCP_Estoque(self.os_Value)
            self.compras_itens.show()
            self.close()
        else:
            QMessageBox.warning(self, "<b>Aviso</b>", "<b>Por favor, preencha o campo.</b>")

    def voltar_pg(self):
        # Exibe a tela anterior (provavelmente a tela de login ou outra página)
        self.voltar_pg = LoginWindow()  # Altere para a tela que deve ser exibida
        self.voltar_pg.show()
        self.close()

    def verificar_pcp_os_check(self):
        # Cria uma nova janela que é um QMainWindow
        self.w = Verificar_PCP_os_CHECK(self)  # Passa a janela atual
        self.w.show()
        self.close()

class Verificar_PCP_os_CHECK(QMainWindow, UI_PCP_OS_CHECK):
    def __init__(self, PCP_Estoque: Ui_PCP_Estoque):
        super(Verificar_PCP_os_CHECK, self).__init__()
        self.setupUi(self)  # Configura a interface
        self.setWindowTitle('PCP')
        self.PCP_Estoque = PCP_Estoque

        # Conectar os botões
        self.Btn_Voltar_Login.clicked.connect(self.voltar_para_menu_vendas)
        self.Btn_Avancar.clicked.connect(self.passar_os)  # Chama o método para passar a os

    def voltar_para_menu_vendas(self):
        self.PCP_Estoque.show()
        self.close()

    def passar_os(self):
        os_value = self.Edit_OS.text()  # Captura o valor da os
        self.w = Verificar_PCP_Check(os_value, self)  # Passa o valor da os para a próxima janela
        self.w.show()
        self.close()

class Verificar_PCP_Check(QMainWindow, UI_PCP_Check):
    def __init__(self, os, verificar_os: Verificar_PCP_os_CHECK):
        super(Verificar_PCP_Check, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('PCP')
        self.verificar_os = verificar_os
        self.os = os  # Armazena o valor de os para uso posterior

        # Conectar os botões
        self.Btn_Voltar_os.clicked.connect(self.voltar_para_os)
        self.Btn_Vendas.clicked.connect(self.avancar_para_vendas)
        self.Btn_Compras.clicked.connect(self.avancar_para_compras)
        self.Btn_Engenharia.clicked.connect(self.avancar_para_engenharia)
    
     # Consultar os dados do banco e preencher o QTreeWidget
        consulta_cliente = '''
            SELECT os, codigo_mp, `desc`, estoque, quantidade, unidade, data_att
            FROM pcp_estoque 
            WHERE os LIKE %s
        '''

        cursor.execute(consulta_cliente, (os,))
        cliente = cursor.fetchall()

        # Preencher o QTreeWidget com os dados
        for mp in cliente:
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(mp[0]))  # Coluna 1: os
            item.setText(1, str(mp[1]))  # Coluna 2: código_mp
            item.setText(2, str(mp[2]))  # Coluna 3: descrição
            item.setText(3, str(mp[3]))  # Coluna 4: estoque
            item.setText(4, str(mp[4]))  # Coluna 5: quantidade
            item.setText(5, str(mp[5]))  # Coluna 6: unidade
            item.setText(6, str(mp[6]))  # Coluna 7: data_att

            # Centralizar o texto e definir a cor branca
            brush = QBrush(QColor(255, 255, 255))
            for col in range(7):  # Há 7 colunas no total
                item.setTextAlignment(col, Qt.AlignCenter)
                item.setForeground(col, brush)

    
    def avancar_para_vendas(self):
        self.verificar_vendas = Verificar_PCP_Vendas(self.os, self.verificar_os)
        self.verificar_vendas.show()
        self.close()

    def avancar_para_compras(self):
        self.verificar_compras = Verificar_PCP_Compras(self.os, self.verificar_os)
        self.verificar_compras.show()
        self.close()

    def avancar_para_engenharia(self):
        self.verificar_engenharia = Verificar_PCP_Engenharia(self.os, self.verificar_os)
        self.verificar_engenharia.show()
        self.close()

    def voltar_para_os(self):
        self.verificar_os.show()
        self.close()

class Verificar_PCP_Vendas(QMainWindow, Ui_Vendas_PCP_Check):
    def __init__(self, os, verificar_os: Verificar_PCP_os_CHECK):
        super(Verificar_PCP_Vendas, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Vendas')
        self.verificar_os = verificar_os
        self.os = os  # Armazena o valor de os para uso posterior

        # Conectar os botões
        self.Btn_Voltar_os.clicked.connect(self.voltar_para_os)
        self.Btn_PCP.clicked.connect(self.avancar_para_pcp)
        self.Btn_Compras.clicked.connect(self.avancar_para_compras)
        self.Btn_Engenharia.clicked.connect(self.avancar_para_engenharia)

        # Consultar os dados do banco e preencher o QTreeWidget
        consulta_cliente = '''
            SELECT os, numero_pedido, vendedor, cnpj_cliente, codigo_item, `desc`, quantidade, unidade, data_prevista, horario_att
            FROM vendas_pedidos 
            WHERE os LIKE %s
        '''

        cursor.execute(consulta_cliente, (os,))
        cliente = cursor.fetchall()

        # Preencher o QTreeWidget com os dados
        for mp in cliente:
            item = QTreeWidgetItem(self.treeWidget_2)
            item.setText(0, str(mp[0]))  # Coluna 1: os
            item.setText(1, str(mp[1]))  # Coluna 2: código_mp
            item.setText(2, str(mp[2]))  # Coluna 3: descrição
            item.setText(3, str(mp[3]))  # Coluna 4: estoque
            item.setText(4, str(mp[4]))  # Coluna 5: quantidade
            item.setText(5, str(mp[5]))  # Coluna 6: unidade
            item.setText(6, str(mp[6]))  # Coluna 7: data_att
            item.setText(7, str(mp[7]))
            item.setText(8, str(mp[8]))
            item.setText(9, str(mp[9]))
            

            # Centralizar o texto e definir a cor branca
            brush = QBrush(QColor(255, 255, 255))
            for col in range(10):  # Há 7 colunas no total
                item.setTextAlignment(col, Qt.AlignCenter)
                item.setForeground(col, brush)

    def avancar_para_pcp(self):
        self.verificar_pcp = Verificar_PCP_Check(self.os, self.verificar_os)
        self.verificar_pcp.show()
        self.close()

    def avancar_para_compras(self):
        self.verificar_compras = Verificar_PCP_Compras(self.os, self.verificar_os)
        self.verificar_compras.show()
        self.close()

    def avancar_para_engenharia(self):
        self.verificar_engenharia = Verificar_PCP_Engenharia(self.os, self.verificar_os)
        self.verificar_engenharia.show()
        self.close()

    def voltar_para_os(self):
        self.verificar_os.show()
        self.close()

class Verificar_PCP_Engenharia(QMainWindow, UI_PCP_Engenharia):
    def __init__(self, os, verificar_os: Verificar_PCP_os_CHECK):
        super(Verificar_PCP_Engenharia, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Engenharia')
        self.verificar_os = verificar_os
        self.os = os  # Armazena o valor de os para uso posterior

        # Conectar os botões
        self.Btn_Voltar_os.clicked.connect(self.voltar_para_os)
        self.Btn_Pcp.clicked.connect(self.avancar_para_pcp)
        self.Btn_Compras.clicked.connect(self.avancar_para_compras)
        self.Btn_Vendas.clicked.connect(self.avancar_para_vendas)

        consulta_cliente = '''
            SELECT os, codigo_Item, `desc`, codigo_mp, desc_mp, quantidade, unidade, horario_att
            FROM engenharia
            WHERE os LIKE %s
        '''

        cursor.execute(consulta_cliente, (os,))
        cliente = cursor.fetchall()

        # Preencher o QTreeWidget com os dados
        for mp in cliente:
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(mp[0]))  # Coluna 1: os
            item.setText(1, str(mp[1]))  # Coluna 2: código_mp
            item.setText(2, str(mp[2]))  # Coluna 3: descrição
            item.setText(3, str(mp[3]))  # Coluna 4: estoque
            item.setText(4, str(mp[4]))  # Coluna 5: quantidade
            item.setText(5, str(mp[5]))  # Coluna 6: unidade
            item.setText(6, str(mp[6]))  # Coluna 7: data_att
            item.setText(7, str(mp[7]))

            # Centralizar o texto e definir a cor branca
            brush = QBrush(QColor(255, 255, 255))
            for col in range(8):  # Há 7 colunas no total
                item.setTextAlignment(col, Qt.AlignCenter)
                item.setForeground(col, brush)

    # Métodos para navegação entre as telas (usando o valor de os)
    def avancar_para_pcp(self):
        self.verificar_pcp = Verificar_PCP_Check(self.os, self.verificar_os)
        self.verificar_pcp.show()
        self.close()

    def avancar_para_compras(self):
        self.verificar_compras = Verificar_PCP_Compras(self.os, self.verificar_os)
        self.verificar_compras.show()
        self.close()

    def avancar_para_vendas(self):
        self.verificar_vendas = Verificar_PCP_Vendas(self.os, self.verificar_os)
        self.verificar_vendas.show()
        self.close()

    def voltar_para_os(self):
        self.verificar_os.show()
        self.close()

class Verificar_PCP_Compras(QMainWindow, UI_PCP_Compras):
    def __init__(self, os, verificar_os: Verificar_PCP_os_CHECK):
        super(Verificar_PCP_Compras, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Compras')
        self.verificar_os = verificar_os
        self.os = os  # Armazena o valor de os para uso posterior

        # Conectar os botões
        self.Btn_Voltar_os.clicked.connect(self.voltar_para_os)
        self.Btn_PCP.clicked.connect(self.avancar_para_pcp)
        self.Btn_Vendas.clicked.connect(self.avancar_para_vendas)
        self.Btn_Engenharia.clicked.connect(self.avancar_para_engenharia)

        # Consultar os dados do banco e preencher o QTreeWidget
        consulta_cliente = '''
            SELECT os, nome, quantidade, unidade, valor, transporte, cnpj, previsao, data_att
            FROM compras_itens
            WHERE os LIKE %s
        '''

        cursor.execute(consulta_cliente, (os,))
        cliente = cursor.fetchall()

        # Preencher o QTreeWidget com os dados
        for mp in cliente:
            item = QTreeWidgetItem(self.treeWidget_2)
            item.setText(0, str(mp[0]))  # Coluna 1: os
            item.setText(1, str(mp[1]))  # Coluna 2: código_mp
            item.setText(2, str(mp[2]))  # Coluna 3: descrição
            item.setText(3, str(mp[3]))  # Coluna 4: estoque
            item.setText(4, str(mp[4]))  # Coluna 5: quantidade
            item.setText(5, str(mp[5]))  # Coluna 6: unidade
            item.setText(6, str(mp[6]))
            item.setText(7, str(mp[7]))
            item.setText(8, str(mp[8]))  # Coluna 7: data_att

            # Centralizar o texto e definir a cor branca
            brush = QBrush(QColor(255, 255, 255))
            for col in range(9):  # Há 7 colunas no total
                item.setTextAlignment(col, Qt.AlignCenter)
                item.setForeground(col, brush)

    def avancar_para_pcp(self):
        self.verificar_pcp = Verificar_PCP_Check(self.os, self.verificar_os)
        self.verificar_pcp.show()
        self.close()

    def avancar_para_engenharia(self):
        self.verificar_engenharia = Verificar_PCP_Engenharia(self.os, self.verificar_os)
        self.verificar_engenharia.show()
        self.close()

    def avancar_para_vendas(self):
        self.verificar_vendas = Verificar_PCP_Vendas(self.os, self.verificar_os)
        self.verificar_vendas.show()
        self.close()

    def voltar_para_os(self):
        self.verificar_os.show()
        self.close()
# Classe para a janela de Verificar no estoque
class PCP_Estoque(QMainWindow, Ui_PCP_Estoque):
    def __init__(self, os_Value):
        super(PCP_Estoque, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('PCP Estoque')

        # Armazenar o valor do os passado
        self.os_Value = os_Value
        data_atual = datetime.now().strftime("%d/%m/%Y")

        # Variável para armazenar o item selecionado
        self.selected_item = None

        # Consulta SQL para buscar as matérias-primas
        consulta_mp = '''
        SELECT codigo_mp, desc_mp, quantidade, unidade
        FROM engenharia 
        WHERE os LIKE %s AND Quantidade > 0
        '''

        try:
            cursor.execute(consulta_mp, (f"%{os_Value}%",))
            materias_primas = cursor.fetchall() # Verifique os resultados
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")

        # Inserção de Data_Criacao na tabela horarios
        inserir_horario_pedidos = '''
        UPDATE horarios
        SET pcp = %s
        WHERE os LIKE %s;
        '''

        dadoshora = (data_atual, os_Value)
        cursor.execute(inserir_horario_pedidos, dadoshora)
        mydb.commit()

        self.Tabela_pcp.clear()  # Limpa a treeWidget antes de adicionar novos dados

        for mp in materias_primas:
            # Cria um QTreeWidgetItem para cada linha de dados
            item = QTreeWidgetItem(self.Tabela_pcp)
            item.setText(0, str(mp[0]))  # Coluna 1: Codigo_MP
            item.setText(1, str(mp[1]))  # Coluna 2: Descricao_MP
            item.setText(2, str(mp[2]))  # Coluna 3: Quantidade
            item.setText(3, str(mp[3]))  # Coluna 4: Unidade
            item.setText(4, self.os_Value)  # Coluna 5: os

            # Centralizar o texto em todas as colunas
            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            item.setTextAlignment(4, Qt.AlignCenter)

        if not materias_primas:
            QMessageBox.information(self, "<b>Informação</b>", "<b>Nenhuma matéria-prima encontrada.</b>")

        # Conectar botões aos métodos correspondentes
        self.Btn_Voltar_os.clicked.connect(self.voltar_pg)
        self.Btn_Estoque.clicked.connect(self.inserir_estoque_ok)
        self.Btn_Fallta.clicked.connect(self.inserir_estoque_pendente)

        # Conectar o evento de seleção de item
        self.Tabela_pcp.itemClicked.connect(self.on_item_selected)

    def on_item_selected(self, item):
        # Função que armazena o item selecionado.
        self.selected_item = item

    def inserir_estoque_ok(self):
        if self.selected_item:
            codigo_mp = self.selected_item.text(0)  # Pega o valor do Codigo_MP
            quantidade_atual = float(self.selected_item.text(2))
            descricao = self.selected_item.text(1)  # Pega a descrição da Tabela_pcp
            quantidade_inserida = self.Edit_Quantidade.text()
            unidade = self.selected_item.text(3)
            os_value = self.selected_item.text(4)  # Pega o valor do os
            data_atual = datetime.now().strftime("%d/%m/%Y")
            try:
                quantidade_inserida = float(quantidade_inserida)  # Verifica se a quantidade inserida é numérica

                if quantidade_inserida <= quantidade_atual:
                    try:
                        # Insere 'OK' no banco de dados para o item selecionado com a quantidade inserida
                        insert_query = "INSERT INTO pcp_estoque (codigo_mp, `desc`, estoque, quantidade, unidade, os, data_att) VALUES (%s, %s, 'OK', %s, %s, %s, %s)"
                        cursor.execute(insert_query, (codigo_mp, descricao, quantidade_inserida, unidade, os_value, data_atual))

                        # Atualiza a quantidade no banco de dados subtraindo a quantidade inserida
                        update_query = "UPDATE engenharia SET quantidade = quantidade - %s WHERE codigo_mp = %s"
                        cursor.execute(update_query, (quantidade_inserida, codigo_mp))

                        mydb.commit()  # Confirma a transação no banco de dados

                        # Atualiza a quantidade na Tabela_pcp
                        nova_quantidade = quantidade_atual - quantidade_inserida
                        if nova_quantidade > 0:
                            self.selected_item.setText(2, str(nova_quantidade))  # Atualiza a quantidade na interface
                        else:
                            # Remove o item da Tabela_pcp se a quantidade for 0
                            index = self.Tabela_pcp.indexOfTopLevelItem(self.selected_item)
                            self.Tabela_pcp.takeTopLevelItem(index)

                        QMessageBox.information(self, "Sucesso", "Estoque atualizado com sucesso.")
                    except Exception as e:
                        QMessageBox.warning(self, "Erro", f"Erro ao atualizar estoque: {e}")
                else:
                    QMessageBox.warning(self, "Aviso", "Quantidade inserida maior que a quantidade disponível.")
            except ValueError:
                QMessageBox.warning(self, "Aviso", "Por favor, insira uma quantidade válida.")
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum item selecionado.")

    def inserir_estoque_pendente(self):
        if self.selected_item:
            codigo_mp = self.selected_item.text(0)  # Pega o valor do Codigo_MP
            descricao = self.selected_item.text(1)  # Pega a descrição da Tabela_pcp
            quantidade_atual = float(self.selected_item.text(2))
            quantidade_inserida = self.Edit_Quantidade.text()
            unidade = self.selected_item.text(3)  # Pega a unidade da Tabela_pcp
            os_value = self.selected_item.text(4)  # Pega o valor do os
            data_atual = datetime.now().strftime("%d/%m/%Y")


            try:
                quantidade_inserida = float(quantidade_inserida)  # Verifica se a quantidade inserida é numérica

                if quantidade_inserida <= quantidade_atual:
                    try:
                        # Insere 'PENDENTE' no banco de dados para o item selecionado com a quantidade inserida
                        insert_query = "INSERT INTO pcp_estoque (codigo_mp, `desc`, estoque, quantidade, unidade, os, data_att) VALUES (%s, %s, 'PENDENTE', %s, %s, %s, %s)"
                        cursor.execute(insert_query, (codigo_mp, descricao, quantidade_inserida, unidade, os_value, data_atual))

                        # Atualiza a quantidade no banco de dados subtraindo a quantidade inserida
                        update_query = "UPDATE engenharia SET quantidade = quantidade - %s WHERE codigo_mp = %s"
                        cursor.execute(update_query, (quantidade_inserida, codigo_mp))

                        mydb.commit()  # Confirma a transação no banco de dados

                        # Atualiza a quantidade na Tabela_pcp
                        nova_quantidade = quantidade_atual - quantidade_inserida
                        if nova_quantidade > 0:
                            self.selected_item.setText(2, str(nova_quantidade))  # Atualiza a quantidade na interface
                        else:
                            # Remove o item da Tabela_pcp se a quantidade for 0
                            index = self.Tabela_pcp.indexOfTopLevelItem(self.selected_item)
                            self.Tabela_pcp.takeTopLevelItem(index)

                        QMessageBox.information(self, "Sucesso", "Estoque atualizado como PENDENTE.")
                        
                        
                    except Exception as e:
                        QMessageBox.warning(self, "Erro", f"Erro ao atualizar estoque: {e}")
                else:
                    QMessageBox.warning(self, "Aviso", "Quantidade inserida maior que a quantidade disponível.")
            except ValueError:
                QMessageBox.warning(self, "Aviso", "Por favor, insira uma quantidade válida.")
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum item selecionado.")

    def voltar_pg(self):
        # Exibe a tela anterior (provavelmente a tela de onde o usuário veio)
        self.voltar_pg = PCP_os()  # Se você quer voltar para a tela 'PCP_os'
        
        # Exibe a nova página
        self.voltar_pg.show()
        
        # Fecha a página atual
        self.close()
# Classe para a janela do início de compras  
class compras_inicio(QMainWindow, UI_Compras_Inicio):
    def __init__(self, login_window: LoginWindow):
        super(compras_inicio, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Compras')
        self.login_window = login_window
       
        self.Btn_Voltar.clicked.connect(self.voltar_para_login)
        self.Btn_Add.clicked.connect(self.addfornecedor)
        self.Btn_Verify.clicked.connect(self.abrir_verificar_fornecedor)  # Conectar o Btn_Verify ao método correto
        self.Btn_Pedidos.clicked.connect(self.abrir_compras_os)
        self.Btn_Checar.clicked.connect(self.verificar_compras_check)
    # Método para voltar à tela de login
    def voltar_para_login(self):
        self.login_window.show()
        self.close()
    def abrir_compras_os(self):
        self.compras_os_window = Compras_os(self)  # Cria uma instância da classe Compras_os
        self.compras_os_window.show()  # Exibe a nova janela
        self.close() 
    # Método para abrir a tela de adicionar fornecedor
    def addfornecedor(self):
        self.fornecedor_window = self.addfornecedorpg(self)  # Cria a instância da classe addfornecedorpg
        self.fornecedor_window.show()  # Exibe a janela de adicionar fornecedor
        self.close()  # Opcional: Fecha a janela atual de compras_inicio, se desejar

    def verificar_compras_check(self):
        # Cria uma nova janela que é um QMainWindow
        self.w = Verificar_Compras_os(self)  # Passa a janela atual
        self.w.show()
        self.close()
        
    # Método para abrir a tela Verificar Fornecedor
    def abrir_verificar_fornecedor(self):
        self.verificar_fornecedor_window = Verificar_Fornecedor(self)  # Cria uma instância da classe Verificar_Fornecedor
        self.verificar_fornecedor_window.show()  # Exibe a nova janela
        self.close()  # Opcional: Fecha a janela atual de compras_inicio

    # Classe addfornecedorpg que representa a janela de adicionar fornecedor
    class addfornecedorpg(QMainWindow, Ui_AdicionarFornecedor):
        def __init__(self, parent_window):
            super().__init__()
            self.setupUi(self)
            self.setWindowTitle('Compras')
            self.parent_window = parent_window  # Referência à janela pai

            # Conectar o botão de salvar fornecedor ao método de inserção no banco de dados
            self.Btn_Avancar.clicked.connect(self.addfornecedorbd)
            self.Btn_Voltar.clicked.connect(self.voltar_para_parent)

        def voltar_para_parent(self):
            self.parent_window.show()
            self.close()

        def addfornecedorbd(self):
            Nome_Empresa = self.Edit_NomeEmpresa.text().strip()
            Telefone = self.Edit_Telefone.text().strip()
            Endereco = self.Edit_Enderecos.text().strip()
            Cep = self.Edit_CEP.text().strip()
            Email = self.Edit_Email.text().strip()
            Inscricao_Estadual = self.Edit_InscricaoEstadual.text().strip()
            Cnpj = self.Edit_CNPJ.text().strip()

            # Verifica se todos os campos estão preenchidos
            if Nome_Empresa and Telefone and Endereco and Cep and Email and Inscricao_Estadual and Cnpj:
                add_table_vendasclientes = '''
                INSERT INTO compras_fornecedor
                (nome_frncdr, telefone_frncdr, endereco_frncdr, cep_frncdr, email_frncdr, inscestadual_frncdr, cnpj_frncdr)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                '''
                dados = (Nome_Empresa, Telefone, Endereco, Cep, Email, Inscricao_Estadual, Cnpj)
                    
                cursor.execute(add_table_vendasclientes, dados)
                mydb.commit()
                
                self.Label_Aviso.setText(f'<div align="center"><font color="green"><b>Fornecedor adicionado com sucesso</b></font></div>')
                QTimer.singleShot(1000, self.restore_label_text)

            else:
                self.Label_Aviso.setText(f'<div align="center"><font color="red"><b>Verifique os campos inseridos</b></font></div>')
                QTimer.singleShot(1000, self.restore_label_text)

        def restore_label_text(self):
            self.Label_Aviso.setText('')
# Classe para a janela de Verificar Fornecedor
class Verificar_Fornecedor(QMainWindow, UI_VerificarFornecedor):
    def __init__(self, parent_window):
        super(Verificar_Fornecedor, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Compras')
        self.parent_window = parent_window  # Referência à janela pai
        
        # Conecta os botões
        self.Btn_Voltar.clicked.connect(self.voltar_para_parent)
        self.Btn_Consultar.clicked.connect(self.consultar_nomes)
        
        # Consulta SQL sem o placeholder
        consulta_materias_primas = '''
            SELECT nome_frncdr, telefone_frncdr, endereco_frncdr, cep_frncdr, email_frncdr, inscestadual_frncdr, cnpj_frncdr
            FROM compras_fornecedor
        '''
        
        # Executa a consulta sem parâmetros
        cursor.execute(consulta_materias_primas)
        materias_primas = cursor.fetchall()

        self.treeWidget.clear()  # Limpa a treeWidget antes de adicionar novos dados

        for mp in materias_primas:
            # Cria um QTreeWidgetItem para cada linha de dados
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(mp[0]))  
            item.setText(1, str(mp[1]))
            item.setText(2, str(mp[2]))
            item.setText(3, str(mp[3]))
            item.setText(4, str(mp[4]))
            item.setText(5, str(mp[5]))
            item.setText(6, str(mp[6]))  

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            item.setTextAlignment(4, Qt.AlignCenter)
            item.setTextAlignment(5, Qt.AlignCenter)
            item.setTextAlignment(6, Qt.AlignCenter)
            
    def voltar_para_parent(self):
        self.parent_window.show()
        self.close()

    def consultar_nomes(self):
        nome_input = self.Edit_Nome.text().strip()  # Obtém o texto do campo de entrada

        # Verifica se o campo de nome foi preenchido
        if nome_input:
            # Consulta SQL para buscar os fornecedores
            consulta_materias_primas = '''
                SELECT nome_frncdr, telefone_frncdr, endereco_frncdr, cep_frncdr, email_frncdr, insestadual_frncdr, cnpj_frncdr
                FROM compras_fornecedor 
                WHERE nome_frncdr LIKE %s
            '''
            cursor.execute(consulta_materias_primas, (f"%{nome_input}%",))
            materias_primas = cursor.fetchall()

            self.treeWidget.clear()  # Limpa a treeWidget antes de adicionar novos dados

            for mp in materias_primas:
                # Cria um QTreeWidgetItem para cada linha de dados
                item = QTreeWidgetItem(self.treeWidget)
                item.setText(0, str(mp[0]))  
                item.setText(1, str(mp[1]))
                item.setText(2, str(mp[2]))
                item.setText(3, str(mp[3]))
                item.setText(4, str(mp[4]))
                item.setText(5, str(mp[5]))
                item.setText(6, str(mp[6]))  

                item.setTextAlignment(0, Qt.AlignCenter)
                item.setTextAlignment(1, Qt.AlignCenter)
                item.setTextAlignment(2, Qt.AlignCenter)
                item.setTextAlignment(3, Qt.AlignCenter)
                item.setTextAlignment(4, Qt.AlignCenter)
                item.setTextAlignment(5, Qt.AlignCenter)
                item.setTextAlignment(6, Qt.AlignCenter)

            if not materias_primas:
                QMessageBox.information(self, "Informação", "Nenhum fornecedor encontrado.")
        else:
            QMessageBox.warning(self, "Aviso", "Digite um nome para a consulta.")
# Classe para a janela do os em compras
class Compras_os(QMainWindow, UI_Compras_OS):
    def __init__(self,parent_window):
        super(Compras_os, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Compras')
       

        # Variável para armazenar o valor do LineEdit
        self.os_Value = ""
        self.parent_window = parent_window
        # Conectar botões aos métodos correspondentes
        self.Btn_Avancar.clicked.connect(self.avancar_para_estoque)
        self.Btn_Voltar_Login.clicked.connect(self.voltar_para_parent)

    def voltar_para_parent(self):
        self.parent_window.show()
        self.close()
    def avancar_para_estoque(self):
        # Atualiza o valor de self.os_Value com o texto do LineEdit
        self.os_Value = self.Edit_OS.text().strip()  # Substitua Edit_OS pelo nome correto do seu LineEdit

        if self.os_Value:
            # Criar uma instância da tela Compras_Itens e passar a informação
            self.compras_itens = Compras_Itens(self.os_Value)
            self.compras_itens.show()
            self.close()  # Fecha a janela atual
        else:
            QMessageBox.warning(self, "<b>Aviso</b>", "<b>Por favor, preencha o campo.</b>")

    def voltar_pg(self):
        # Exibe a tela anterior (provavelmente a tela de onde o usuário veio)
        self.voltar_pg = LoginWindow()  # Se você quer voltar para a tela 'PCP_os'
        
        # Exibe a nova página
        self.voltar_pg.show()
        
        # Fecha a página atual
        self.close()
# Classe para a compra dos itens
class Compras_Itens(QMainWindow, UI_Compras_Estoque):
    def __init__(self, os_Value):
        super(Compras_Itens, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Compras')
        self.Btn_Estoque.clicked.connect(self.ir_para_compras_preencher)
        self.os_Value = os_Value

        self.selected_item = None

        self.atualizar_treewidget()  # Inicializa a tabela ao abrir a tela
        
        self.Tabela_pcp.itemClicked.connect(self.on_item_selected)

    def ir_para_compras_preencher(self):
        if self.selected_item:
            codigo_mp = self.selected_item.text(0)  # Adiciona o código da matéria-prima
            descricao = self.selected_item.text(1)
            quantidade = self.selected_item.text(2)
            self.compras_preencher = UI_Compras_Preencher(
                codigo_mp, descricao, quantidade, self.os_Value, self.atualizar_treewidget, self
            )
            self.compras_preencher.show()
            self.close()
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum item selecionado.")
            
    def atualizar_treewidget(self):
        consulta_mp = '''
        SELECT codigo_mp, `desc`, quantidade, unidade
        FROM pcp_estoque
        WHERE os LIKE %s AND estoque LIKE "PENDENTE"
        '''
        cursor.execute(consulta_mp, (f"%{self.os_Value}%",))
        Itens_Comprar = cursor.fetchall()
        mydb.commit()
        self.Tabela_pcp.clear()

        for mp in Itens_Comprar:
            item = QTreeWidgetItem(self.Tabela_pcp)
            item.setText(0, str(mp[0]))
            item.setText(1, str(mp[1]))
            item.setText(2, str(mp[2]))
            item.setText(3, str(mp[3]))

            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)

        if not Itens_Comprar:
            QMessageBox.information(self, "Informação", "Nenhuma matéria-prima encontrada.")

    def on_item_selected(self, item):
        self.selected_item = item
# Classe para o preenchemento da info das compras
class Verificar_Compras_os(QMainWindow, UI_Compras_OS_Check):
    def __init__(self, Compras_check_os: UI_Compras_Inicio):
        super(Verificar_Compras_os, self).__init__()
        self.setupUi(self)  # Configura a interface
        self.setWindowTitle('Compras')
        self.Compras_check_os = Compras_check_os

        # Conectar os botões
        self.Btn_Voltar.clicked.connect(self.voltar_para_menu_vendas)
        self.Btn_Avancar.clicked.connect(self.passar_os)  # Chama o método para passar a os

    def voltar_para_menu_vendas(self):
        self.Compras_check_os.show()
        self.close()

    def passar_os(self):
        os_value = self.Edit_OS.text()  # Captura o valor da os
        self.w = Verificar_Compras_Check(os_value, self)  # Passa o valor da os para a próxima janela
        self.w.show()
        self.close()

class Verificar_Compras_Check(QMainWindow, UI_Compras_Check):
    def __init__(self,os, verificar_os: Verificar_Compras_os):
        super(Verificar_Compras_Check, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Compras')
        self.verificar_os = verificar_os
    
        self.Btn_Voltar_os.clicked.connect(self.voltar_para_os)
        #self.Btn_Avancar.clicked.connect(self.verificar_pedido)
        consulta_cliente = '''
                SELECT os, nome, quantidade, unidade, valor, transporte, cnpj, previsao, data_att
                FROM compras_itens 
                WHERE os LIKE %s
                '''
        
        cursor.execute(consulta_cliente, (os,))
        cliente = cursor.fetchall()
        

        for mp in cliente:
    # Cria um QTreeWidgetItem para cada linha de dados
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(mp[0]))  # Coluna 1: ID
            item.setText(1, str(mp[1]))
            item.setText(2, str(mp[2]))
            item.setText(3, str(mp[3]))
            item.setText(4, str(mp[4]))
            item.setText(5, str(mp[5])) 
            item.setText(6, str(mp[6]))
            item.setText(7, str(mp[7]))
            item.setText(8, str(mp[8]))
            
            

            # Centralizar o texto em todas as colunas
            for col in range(9):  # Supondo que tenha 10 colunas
                item.setTextAlignment(col, Qt.AlignCenter)

            # Definir a cor branca para o texto
            brush = QBrush(QColor(255, 255, 255))  # Branco (R=255, G=255, B=255)
            for col in range(9):
                item.setForeground(col, brush)

    def voltar_para_os(self):
        self.verificar_os.show()
        self.close()

class UI_Compras_Preencher(QMainWindow, UI_Compras_Preencher):
    def __init__(self, codigo_mp, descricao, quantidade, os_value, atualizar_treewidget, parent_window):
        super(UI_Compras_Preencher, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Compras')

        # Armazenar as informações recebidas
        self.codigo_mp = codigo_mp  # Armazena o código da matéria-prima
        self.descricao = descricao
        self.quantidade = quantidade
        self.os_value = os_value
        self.atualizar_treewidget = atualizar_treewidget  # Função para atualizar a tabela
        self.parent_window = parent_window  # Referência da tela anterior

        # Inicializa a UI
        self.init_ui()

        # Conectar o botão de salvar aos métodos
        self.Btn_Avancar.clicked.connect(self.salvar_dados)
        self.Btn_Voltar.clicked.connect(self.voltar_para_anterior)


    def init_ui(self):
        # Inicialize os componentes da interface com os dados fornecidos
        self.Edit_Nome.setText(self.descricao)
        self.Edit_Quantidade.setText(str(self.quantidade))

    def salvar_dados(self):
        nome = self.Edit_Nome.text().strip()
        quantidade = self.Edit_Quantidade.text().strip()
        valor = self.Edit_Valor.text().strip()
        previsao = self.Edit_Previsao.text().strip()
        transporte = self.comboBox.currentText()
        cnpj = self.Edit_Previsao_2.text().strip()
        os_value = self.os_value
        codigo_mp = self.codigo_mp  # Usa o código da matéria-prima
        quantidade_inserida = float(self.Edit_Quantidade.text().strip())
        data_atual = datetime.now().strftime("%d/%m/%Y")
        unidade = self.Edit_Unidade.text().strip()

        if nome and quantidade and valor and previsao and transporte:
            try:
                # Inserir dados na tabela compras_itens, incluindo o codigo_mp
                inserir_dados = '''
                INSERT INTO compras_itens (codigo_mp, nome, quantidade, unidade, valor, previsao, transporte, cnpj, os, data_att) 
                VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
                cursor.execute(inserir_dados, (codigo_mp, nome, quantidade, unidade , valor, previsao, transporte, cnpj, os_value, data_atual))

                # Inserir data atual na tabela horarios
                inserir_horario_pedidos = '''
                UPDATE horarios
                SET compras = %s
                WHERE os LIKE %s;
                '''
    
                dadoshora = (data_atual, os_value)
                cursor.execute(inserir_horario_pedidos, dadoshora)
                
                # Atualiza a quantidade no banco de dados subtraindo a quantidade inserida
                update_query = '''
                UPDATE pcp_estoque 
                SET quantidade = quantidade - %s 
                WHERE os = %s AND codigo_mp = %s AND estoque = 'PENDENTE'
                '''
                cursor.execute(update_query, (quantidade_inserida, os_value, codigo_mp))
                

                # Confirma as alterações no banco de dados
                mydb.commit()

                # Atualiza a QTreeWidget na tela anterior
                if self.atualizar_treewidget:
                    self.atualizar_treewidget()

                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso.")
                

            except Exception as e:
                QMessageBox.warning(self, "Erro", f"Erro ao salvar os dados: {e}")
        else:
            QMessageBox.warning(self, "Aviso", "Por favor, preencha todos os campos.")

    def voltar_para_anterior(self):
        # Exibe a tela anterior
        if self.parent_window:
            self.parent_window.show()
        self.close()









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())