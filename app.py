from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)

# --- ESSA FUNÇÃO PRECISA ESTAR AQUI ---
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
# --------------------------------------

@app.route('/')
def index():
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos').fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

@app.route('/cadastrar', methods=('GET', 'POST'))
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        contato_nome = request.form['contato_nome']
        whatsapp = request.form['whatsapp']
        descricao = request.form['descricao']

        conn = get_db_connection()
        conn.execute('INSERT INTO produtos (nome, preco, contato_nome, whatsapp, descricao) VALUES (?, ?, ?, ?, ?)',
                     (nome, preco, contato_nome, whatsapp, descricao))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)