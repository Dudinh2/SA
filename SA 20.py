
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Função para conectar ao banco de dados
def conectar_bc():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Usuário do banco
            password="root",  # Senha do banco
            database="bc_livraria"  # Nome do banco
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None
#___________________ BANCO DE DADOS   ⬆️ _________________________________________________________________________________________________________________________________________________

# Tela inicial pesquisa cliente
#Variavel p = pesquisa

def criar_tela_pesquisa():
    # Janela principal
    p = tk.Tk()
    p.title("Livraria Versos & Universos")
    p.geometry("1000x600")
    p.configure(bg="#faf4ec")

    tk.Label(
        p, text="👑 Livraria Versos & Universos", font=("Arial", 24, "bold"),
        bg="#6c4f47", fg="#f4d2a1"
    ).pack(pady=20)

    # Campos de filtro
    frame_filtros = tk.Frame(p, bg="#faf4ec", pady=20)
    frame_filtros.pack()

    tk.Label(frame_filtros, text="Nome do Livro:", bg="#6c4f47",  fg="#f4d2a1", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
    nome = tk.Entry(frame_filtros, font=("Arial", 12))
    nome.grid(row=1, column=0, padx=5, pady=5)

    tk.Label(frame_filtros, text="Autor:",  bg="#6c4f47",  fg="#f4d2a1", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=5)
    autor = tk.Entry(frame_filtros, font=("Arial", 12))
    autor.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_filtros, text="Gênero:", bg="#6c4f47",  fg="#f4d2a1", font=("Arial", 12)).grid(row=0, column=2, padx=5, pady=5)
    genero = tk.Entry(frame_filtros, font=("Arial", 12))
    genero.grid(row=1, column=2, padx=5, pady=5)

    tk.Label(frame_filtros, text="Ano:", bg="#6c4f47",  fg="#f4d2a1", font=("Arial", 12)).grid(row=0, column=3, padx=5, pady=5)
    ano = tk.Entry(frame_filtros, font=("Arial", 12))
    ano.grid(row=1, column=3, padx=5, pady=5)

    tk.Label(frame_filtros, text="Editora:", bg="#6c4f47",  fg="#f4d2a1", font=("Arial", 12)).grid(row=0, column=4, padx=5, pady=5)
    editora = tk.Entry(frame_filtros, font=("Arial", 12))
    editora.grid(row=1, column=4, padx=5, pady=5)

    def busca():
        # Recuperar valores dos filtros
        filtros = {
            "nome": nome.get(),
            "autor": autor.get(),
            "genero": genero.get(),
            "ano": ano.get(),
            "editora": editora.get(),
        }

        conn = conectar_bc()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT titulo, autor, genero, ano, editora FROM livros WHERE 1=1"
                params = []

                if filtros["nome"]:
                    query += " AND titulo LIKE %s"
                    params.append(f"%{filtros['nome']}%")
                if filtros["autor"]:
                    query += " AND autor LIKE %s"
                    params.append(f"%{filtros['autor']}%")
                if filtros["genero"]:
                    query += " AND genero LIKE %s"
                    params.append(f"%{filtros['genero']}%")
                if filtros["ano"]:
                    query += " AND ano = %s"
                    params.append(filtros["ano"])
                if filtros["editora"]:
                    query += " AND editora LIKE %s"
                    params.append(f"%{filtros['editora']}%")

                cursor.execute(query, params)
                livros = cursor.fetchall()
                conn.close()

                # Exibir resultados
                resultados_window = tk.Toplevel()
                resultados_window.title("Resultados da Pesquisa")
                resultados_window.geometry("800x400")
                resultados_window.configure(bg="#efece7")

                if livros:
                    tk.Label(resultados_window, text="Resultados da Pesquisa", font=("Arial", 16, "bold"), bg="#efece7").pack(pady=10)
                    frame = tk.Frame(resultados_window, bg="#efece7")
                    frame.pack(fill="both", expand=True, padx=20, pady=10)

                    headers = ["Título", "Autor", "Gênero", "Ano", "Editora"]
                    for col, header in enumerate(headers):
                        tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg="#efece7").grid(row=0, column=col, padx=5, pady=5)

                    for i, livro in enumerate(livros, start=1):
                        for j, value in enumerate(livro):
                            tk.Label(frame, text=value, bg="#efece7", font=("Arial", 10)).grid(row=i, column=j, padx=5, pady=5)
                else:
                    tk.Label(resultados_window, text="Nenhum livro encontrado.", font=("Arial", 14), bg="#efece7").pack(pady=20)

            except mysql.connector.Error as e:
                messagebox.showerror("Erro", f"Erro ao buscar no banco de dados: {e}")
        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

    tk.Button(
        p, text="Buscar 🔍", font=("Arial", 12, "bold"), bg="#b57b50", fg="white", command=busca
    ).pack(pady=10)
    tk.Button(
        p, text="Funcionário", font=("Arial", 12, "bold"), bg="#b57b50", fg="white", command=abrir_login
    ).pack(pady=10)



    p.mainloop()

#___________________ pesquisa de livro  ⬆️ ________________________________________________________________________________________________________________________________________________

def abrir_login():
    # Criar a janela de login
    janela_login = tk.Toplevel()
    janela_login.title("Login - Livraria Versos & Universos")
    janela_login.geometry("400x400")
    janela_login.configure(bg="#faf4ec")

    # Cabeçalho
    tk.Label(
        janela_login, text="Login", font=("Arial", 18, "bold"),
        bg="#faf4ec", fg="#6c4f47"
    ).pack(pady=20)

    # Campo de entrada para login
    tk.Label(
        janela_login, text="Usuário", font=("Arial", 12),
        bg="#faf4ec", fg="#6c4f47"
    ).pack(pady=10)
    entrada_login = tk.Entry(janela_login, font=("Arial", 12), width=30)
    entrada_login.pack(pady=10)

    # Campo de entrada para senha
    tk.Label(
        janela_login, text="Senha", font=("Arial", 12),
        bg="#faf4ec", fg="#6c4f47"
    ).pack(pady=10)
    entrada_senha = tk.Entry(janela_login, font=("Arial", 12), show="*", width=30)
    entrada_senha.pack(pady=10)

    # Função para autenticar o usuário
    def autenticar():
        usuario = entrada_login.get()
        senha = entrada_senha.get()
        if verificar_login(usuario, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            janela_login.destroy()
            tela_menu()
        else:
            messagebox.showerror("Erro", "Login ou senha inválidos.")


    # Botões
    tk.Button(
        janela_login, text="Entrar", font=("Arial", 12, "bold"), bg="#b57b50", fg="white",
        command=autenticar
    ).pack(pady=20)



#____________________________________________login⬆️_____________________________________________________________________________________________________________________________________

# Função para verificar login
def verificar_login(login, senha):
    conn = conectar_bc() # BANCO DE DADOS _________________________________________________________________________________________________
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM cadastro_funci WHERE login = %s AND senha = %s"
        cursor.execute(query, (login, senha))
        resultado = cursor.fetchone()
        conn.close()
        return resultado
    return None

# Função para trocar senha
def trocar_senha(email, nova_senha):
    conn = conectar_bc() # BANCO DE DADOS _________________________________________________________________________________________________
    if conn:
        cursor = conn.cursor()
        query = "UPDATE cadastro_funci SET senha = %s WHERE email = %s"
        cursor.execute(query, (nova_senha, email))
        conn.commit()
        conn.close()
        return True
    return False


#___________________ pesquisa de LOGIN ⬆️ ________________________________________________________________________________________________________________________________________________

# Tela principal finci
def tela_menu():
    menu= tk.Toplevel()
    menu.title("Tela Principal")
    menu.geometry("800x600")
    menu.configure(bg="#faf4ec")


    tk.Label(menu, text="Bem-vindo à Livraria!", font=("Arial", 24, "bold"), bg="#faf4ec").pack(pady=20)

    tk.Button(
        menu, text="    Cadastrar Livro No Site  ", font=("Arial", 12, "bold"), bg="#b57b50", fg="white",
        command=cadastrar_livros
    ).pack(pady=10)

    tk.Button(
        menu, text="    Cadastrar Livro no Estoque  ", font=("Arial", 12, "bold"), bg="#b57b50", fg="white",
        command= cadastrar_livros_es

    ).pack(pady=10)

    tk.Button(
        menu, text="  Consulta de Estoque  ", font=("Arial", 12, "bold"), bg="#b57b50", fg="white",
        command=tela_consulta_estoque

    ).pack(pady=10)

    tk.Button(
        menu, text="Cadastro de funcionário", font=("Arial", 12, "bold"), bg="#b57b50", fg="white",
        command=tela_funcionario
    ).pack(pady=10)

    tk.Button(
        menu, text="             sair             ", font=("Arial", 12, "bold"), bg="#b57b50", fg="white",
        command=criar_tela_pesquisa
    ).pack(pady=10)

#___________________ pesquisa de menu ⬆️ ________________________________________________________________________________________________________________________________________________

# Função para conectar ao banco de dados
def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",   # Altere se necessário
            user="root",        # Usuário do banco
            password="root",    # Senha do banco
            database="bc_livraria" # Nome do banco
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para salvar as informações do cadastro
def salvar_cadastro():
    global nomes, telefone, email, cargo, CEP, LOGIN, senha, data  # Declarar as variáveis como globais

    nome = nomes.get()
    telefone = telefone.get()
    email = email.get()
    cargo = cargo.get()
    cep = CEP.get()
    login = LOGIN.get()
    senha = senha.get()
    data_entrada = data.get()

    if not (nome and telefone and email and cargo and cep and login and senha and data_entrada):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    # Conectar ao banco de dados
    conn = conectar_bd()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO cadastro_funci (nome, tel, email, cargo, cep, login, senha, data_entrada)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (nome, telefone, email, cargo, cep, login, senha, data_entrada)
            cursor.execute(query, valores)
            conn.commit()
            messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")
            limpar_tela()
        except mysql.connector.Error as e:
            messagebox.showerror("Erro", f"Erro ao salvar no banco de dados: {e}")
        finally:
            conn.close()
    else:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

# Função para limpar os campos da tela
def limpar_tela():
    nomes.delete(0, tk.END)
    telefone.delete(0, tk.END)
    email.delete(0, tk.END)
    cargo.delete(0, tk.END)
    CEP.delete(0, tk.END)
    LOGIN.delete(0, tk.END)
    senha.delete(0, tk.END)
    data.delete(0, tk.END)

# Função para a tela de cadastro
def tela_funcionario():
    global nomes, telefone, email, cargo, CEP, CODIGO, LOGIN, senha, data  # Declarar as variáveis globalmente para acesso em outras funções
    
    c = tk.Toplevel()
    c.title("Tela de Cadastro de Funcionário")
    c.geometry("800x600")
    c.configure(bg="#faf4ec")

    # Título
    tk.Label(c, text="CADASTRO DE FUNCIONÁRIO", font=("Arial", 24, "bold"), bg="#b57b50", fg="white").pack(pady=20)

    # Container para organização em colunas
    frame = tk.Frame(c, bg="#faf4ec")
    frame.pack(pady=10)

    # Labels e campos do lado esquerdo
    tk.Label(frame, text="Nome", font=("Arial", 12), bg="#faf4ec").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    nomes = tk.Entry(frame, font=("Arial", 12), width=30)
    nomes.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Número de telefone", font=("Arial", 12), bg="#faf4ec").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    telefone = tk.Entry(frame, font=("Arial", 12), width=30)
    telefone.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="Cargo", font=("Arial", 12), bg="#faf4ec").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    cargo = tk.Entry(frame, font=("Arial", 12), width=30)
    cargo.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame, text="CEP", font=("Arial", 12), bg="#faf4ec").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    CEP = tk.Entry(frame, font=("Arial", 12), width=30)
    CEP.grid(row=3, column=1, padx=10, pady=5)

    # Labels e campos do lado direito
    tk.Label(frame, text="E-mail", font=("Arial", 12), bg="#faf4ec").grid(row=0, column=2, sticky="e", padx=10, pady=5)
    email = tk.Entry(frame, font=("Arial", 12), width=30)
    email.grid(row=0, column=3, padx=10, pady=5)

    tk.Label(frame, text="LOGIN", font=("Arial", 12), bg="#faf4ec").grid(row=1, column=2, sticky="e", padx=10, pady=5)
    LOGIN = tk.Entry(frame, font=("Arial", 12), width=30)
    LOGIN.grid(row=1, column=3, padx=10, pady=5)

    tk.Label(frame, text="SENHA", font=("Arial", 12), bg="#faf4ec").grid(row=2, column=2, sticky="e", padx=10, pady=5)
    senha = tk.Entry(frame, font=("Arial", 12), show="*", width=30)
    senha.grid(row=2, column=3, padx=10, pady=5)

    tk.Label(frame, text="DATA DE ENTRADA", font=("Arial", 12), bg="#faf4ec").grid(row=3, column=2, sticky="e", padx=10, pady=5)
    data = tk.Entry(frame, font=("Arial", 12), width=30)
    data.grid(row=3, column=3, padx=10, pady=5)

    # Botão para salvar
    tk.Button(
        c, text="Salvar", font=("Arial", 12, "bold"), bg="#b57b50", fg="white", command=salvar_cadastro
    ).pack(pady=20)

    tk.Button(
        c, text="Limpar", font=("Arial", 12, "bold"), bg="#b57b50", fg="white", command=limpar_tela
    ).pack(pady=20)




#___________________ cadastro de funcionário ⬆️ ________________________________________________________________________________________________________________________________________________

def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",   # Altere se necessário
            user="root",        # Usuário do banco
            password="root",    # Senha do banco
            database="bc_livraria" # Nome do banco
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None


def cadastrar_livros_estoc():
    global titulos, autor_nome, ano, genero, qtd, editora, data_entrada  # Declarar as variáveis como globais

    titulos = titulo.get()
    autor = autor_nome.get()  # Corrigido para autor_nome, já que a variável é autor_nome
    ano = ano.get()
    genero = genero.get()
    qtd = qtd.get()  # Aqui deve ser a variável 'qtd'
    editora = editora.get()
    data_entrada = data.get()

    if not (titulos and autor and ano and genero and qtd and editora and data_entrada):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    conn = conectar_bd()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO livros (titulo, autor, ano, genero, qtd, editora, data_entrada)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (titulos, autor, ano, genero, qtd, editora, data_entrada)
            cursor.execute(query, valores)
            conn.commit()
            messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")
            limpar_tela()  # Chama a função de limpar os campos após o cadastro
        except mysql.connector.Error as e:
            messagebox.showerror("Erro", f"Erro ao salvar no banco de dados: {e}")
        finally:
            conn.close()
    else:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")


def cadastrar_livros():
    global titulo, autor_nome, ano, genero, qtd, editora, data  # Declarar as variáveis como globais
    
    ca = tk.Toplevel()
    ca.title("Tela de Cadastro de Livros")
    ca.geometry("800x600")
    ca.configure(bg="#faf4ec")

    # Título
    tk.Label(ca, text="CADASTRO DE LIVROS", font=("Arial", 24, "bold"), bg="#b57b50", fg="white").pack(pady=20)

    # Frame para organizar os campos
    frame = tk.Frame(ca, bg="#faf4ec")
    frame.pack(pady=10)

    # Campos de cadastro
    tk.Label(frame, text="Nome do Livro", font=("Arial", 12), bg="#faf4ec").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    titulo = tk.Entry(frame, font=("Arial", 12), width=30)
    titulo.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Autor(a)", font=("Arial", 12), bg="#faf4ec").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    autor_nome = tk.Entry(frame, font=("Arial", 12), width=30)
    autor_nome.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="Gênero", font=("Arial", 12), bg="#faf4ec").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    genero = tk.Entry(frame, font=("Arial", 12), width=30)
    genero.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame, text="Editora", font=("Arial", 12), bg="#faf4ec").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    editora = tk.Entry(frame, font=("Arial", 12), width=30)
    editora.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame, text="Ano", font=("Arial", 12), bg="#faf4ec").grid(row=4, column=0, sticky="w", padx=10, pady=5)
    ano = tk.Entry(frame, font=("Arial", 12), width=30)
    ano.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame, text="Quantidade", font=("Arial", 12), bg="#faf4ec").grid(row=5, column=0, sticky="w", padx=10, pady=5)
    qtd = tk.Entry(frame, font=("Arial", 12), width=30)
    qtd.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(frame, text="Data de Lançamento", font=("Arial", 12), bg="#faf4ec").grid(row=6, column=0, sticky="w", padx=10, pady=5)
    data = tk.Entry(frame, font=("Arial", 12), width=30)
    data.grid(row=6, column=1, padx=10, pady=5)

    # Botão de Cadastro
    tk.Button(ca, text="Cadastrar Livro", font=("Arial", 12, "bold"), bg="#b57b50", fg="white", command=cadastrar_livros_estoc).pack(pady=10)


#___________________ cadastro de livro site⬆️ ________________________________________________________________________________________________________________________________________________

def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",   # Altere se necessário
            user="root",        # Usuário do banco
            password="root",    # Senha do banco
            database="bc_livraria" # Nome do banco
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None

def cadastrar_livros_estocs():
    global titulos, autor_nome, ano, genero, qtd, editora, data_entrada, preco, data_saida  # Variáveis globais para os campos

    titulos = titulo.get()
    autor = autor_nome.get()  # Correção para autor_nome
    ano = ano.get()
    genero = genero.get()
    qtd = qtd.get()  # Captura a quantidade
    editora = editora.get()
    data_entrada = data.get()
    preco = preco.get()  # Captura o preço
    data_saida = data_saida.get()  # Captura a data de saída

    # Verifica se todos os campos estão preenchidos
    if not (titulos and autor and ano and genero and qtd and editora and data_entrada and preco):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    conn = conectar_bd()
    if conn:
        try:
            cursor = conn.cursor()

            # Inserção na tabela 'livros'
            query_livros = """
                INSERT INTO livros (titulo, autor, ano, genero, qtd, editora, data_entrada)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores_livros = (titulos, autor, ano, genero, qtd, editora, data_entrada)
            cursor.execute(query_livros, valores_livros)
            conn.commit()

            # Pega o ID do livro recém-inserido
            id_livro = cursor.lastrowid

            # Inserção na tabela 'estoque' usando o id_livro
            query_estoque = """
                INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores_estoque = (titulos, data_entrada, qtd, id_livro, preco, f"Código-{id_livro}")
            cursor.execute(query_estoque, valores_estoque)
            conn.commit()

            messagebox.showinfo("Sucesso", "Cadastro salvo com sucesso!")
            limpar_tela()  # Chama a função de limpar os campos após o cadastro

        except mysql.connector.Error as e:
            messagebox.showerror("Erro", f"Erro ao salvar no banco de dados: {e}")
        finally:
            conn.close()
    else:
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

def cadastrar_livros_es():
    global titulo, autor_nome, ano, genero, qtd, editora, data, preco, data_saida  # Variáveis globais para os campos
    
    ca = tk.Toplevel()
    ca.title("Tela de Cadastro de Livros")
    ca.geometry("800x600")
    ca.configure(bg="#faf4ec")

    # Título
    tk.Label(ca, text="CADASTRO DE LIVROS", font=("Arial", 24, "bold"), bg="#b57b50", fg="white").pack(pady=20)

    # Frame para organizar os campos
    frame = tk.Frame(ca, bg="#faf4ec")
    frame.pack(pady=10)

    # Campos de cadastro
    tk.Label(frame, text="Nome do Livro", font=("Arial", 12), bg="#faf4ec").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    titulo = tk.Entry(frame, font=("Arial", 12), width=30)
    titulo.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Autor(a)", font=("Arial", 12), bg="#faf4ec").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    autor_nome = tk.Entry(frame, font=("Arial", 12), width=30)
    autor_nome.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="Gênero", font=("Arial", 12), bg="#faf4ec").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    genero = tk.Entry(frame, font=("Arial", 12), width=30)
    genero.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame, text="Editora", font=("Arial", 12), bg="#faf4ec").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    editora = tk.Entry(frame, font=("Arial", 12), width=30)
    editora.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame, text="Ano", font=("Arial", 12), bg="#faf4ec").grid(row=4, column=0, sticky="w", padx=10, pady=5)
    ano = tk.Entry(frame, font=("Arial", 12), width=30)
    ano.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame, text="Quantidade", font=("Arial", 12), bg="#faf4ec").grid(row=5, column=0, sticky="w", padx=10, pady=5)
    qtd = tk.Entry(frame, font=("Arial", 12), width=30)
    qtd.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(frame, text="Preço", font=("Arial", 12), bg="#faf4ec").grid(row=6, column=0, sticky="w", padx=10, pady=5)
    preco = tk.Entry(frame, font=("Arial", 12), width=30)
    preco.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(frame, text="Data de Lançamento", font=("Arial", 12), bg="#faf4ec").grid(row=7, column=0, sticky="w", padx=10, pady=5)
    data = tk.Entry(frame, font=("Arial", 12), width=30)
    data.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(frame, text="Data de Saída (opcional)", font=("Arial", 12), bg="#faf4ec").grid(row=8, column=0, sticky="w", padx=10, pady=5)
    data_saida = tk.Entry(frame, font=("Arial", 12), width=30)
    data_saida.grid(row=8, column=1, padx=10, pady=5)

    # Botão de Cadastro
    tk.Button(ca, text="Cadastrar Livro", font=("Arial", 12, "bold"), bg="#b57b50", fg="white", command=cadastrar_livros_estocs).pack(pady=10)



#___________________ cadastro de livro estoque⬆️ ________________________________________________________________________________________________________________________________________________

def conectar_bc():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="bc_livraria"
        )
    except mysql.connector.Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None

def tela_consulta_estoque():
    # Janela principal
    p = tk.Tk()
    p.title("Livraria Versos & Universos")
    p.geometry("800x600")
    p.configure(bg="#faf4ec")

    tk.Label(
        p, text=" Livraria Versos & Universos", font=("Arial", 24, "bold"),
        bg="#6c4f47", fg="#f4d2a1"
    ).pack(pady=20)

    # Campos de filtro
    frame_filtros = tk.Frame(p, bg="#efece7", pady=20)
    frame_filtros.pack()

    tk.Label(frame_filtros, text="Nome do Livro:", bg="#efece7", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
    nome = tk.Entry(frame_filtros, font=("Arial", 12))
    nome.grid(row=1, column=0, padx=5, pady=5)

    tk.Label(frame_filtros, text="Código:", bg="#efece7", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=5)
    codigo = tk.Entry(frame_filtros, font=("Arial", 12))
    codigo.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_filtros, text="Preço Mínimo:", bg="#efece7", font=("Arial", 12)).grid(row=0, column=2, padx=5, pady=5)
    preco_min = tk.Entry(frame_filtros, font=("Arial", 12))
    preco_min.grid(row=1, column=2, padx=5, pady=5)

    tk.Label(frame_filtros, text="Preço Máximo:", bg="#efece7", font=("Arial", 12)).grid(row=0, column=3, padx=5, pady=5)
    preco_max = tk.Entry(frame_filtros, font=("Arial", 12))
    preco_max.grid(row=1, column=3, padx=5, pady=5)

    def busca():
        # Recuperar valores dos filtros
        filtros = {
            "nome": nome.get(),
            "codigo": codigo.get(),
            "preco_min": preco_min.get(),
            "preco_max": preco_max.get(),
        }

        conn = conectar_bc()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT nome, codigo, preco, quant FROM estoque WHERE 1=1"
                params = []

                if filtros["nome"]:
                    query += " AND nome LIKE %s"
                    params.append(f"%{filtros['nome']}%")
                if filtros["codigo"]:
                    query += " AND codigo = %s"
                    params.append(filtros["codigo"])
                if filtros["preco_min"]:
                    query += " AND preco >= %s"
                    params.append(filtros["preco_min"])
                if filtros["preco_max"]:
                    query += " AND preco <= %s"
                    params.append(filtros["preco_max"])

                cursor.execute(query, params)
                livros = cursor.fetchall()
                conn.close()

                # Exibir resultados
                resultados_window = tk.Toplevel()
                resultados_window.title("Resultados da Pesquisa")
                resultados_window.geometry("800x400")
                resultados_window.configure(bg="#efece7")

                
                if livros:
                    tk.Label(resultados_window, text="Resultados da Pesquisa", font=("Arial", 16, "bold"), bg="#efece7").pack(pady=10)
                    frame = tk.Frame(resultados_window, bg="#efece7")
                    frame.pack(fill="both", expand=True, padx=20, pady=10)

                    headers = ["Nome", "Código", "Preço", "Quantidade"]
                    for col, header in enumerate(headers):
                        tk.Label(frame, text=header, font=("Arial", 12, "bold"), bg="#efece7").grid(row=0, column=col, padx=5, pady=5)

                    for i, livro in enumerate(livros, start=1):
                        for j, value in enumerate(livro):
                            tk.Label(frame, text=value, bg="#efece7", font=("Arial", 10)).grid(row=i, column=j, padx=5, pady=5)
                else:
                    tk.Label(resultados_window, text="Nenhum livro encontrado.", font=("Arial", 14), bg="#efece7").pack(pady=20)

            except mysql.connector.Error as e:
                messagebox.showerror("Erro", f"Erro ao buscar no banco de dados: {e}")
        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")

    tk.Button(
        p, text="Buscar 🔍", font=("Arial", 12, "bold"), bg="#b57b50", fg="white", command=busca
    ).pack(pady=10)

  

#___________________ consulta de estoque⬆️ ________________________________________________________________________________________________________________________________________________

# falta conctar com banco #############################################################################################
# Tela de pagamento
def tela_pagamento():
    pagamento_window = tk.Toplevel()
    pagamento_window.title("Pagamento")
    pagamento_window.geometry("600x400")
    pagamento_window.configure(bg="#faf4ec")

    tk.Label(pagamento_window, text="Pagamento", font=("Arial", 18, "bold"), bg="#faf4ec").pack(pady=10)

    pagamento_window.mainloop()
#___________________ pagamento ⬆️ ________________________________________________________________________________________________________________________________________________


# Inicia o programa
criar_tela_pesquisa()
