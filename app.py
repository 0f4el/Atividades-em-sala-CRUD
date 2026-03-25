from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = 'jogos.db'

# Função genérica para executar queries
def executar_query(query, params=(), fetch=False, commit=False):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultado = None

    try:
        cursor.execute(query, params)

        if commit:
            conn.commit()

        if fetch:
            resultado = cursor.fetchall()

    finally:
        conn.close()

    return resultado



# GET - LISTAR TODOS
@app.route('/jogos', methods=['GET'])
def listar_jogos():
    dados = executar_query("SELECT * FROM jogos", fetch=True)
    jogos = [dict(jogo) for jogo in dados]
    return jsonify(jogos), 200


# GET - BUSCAR POR ID
@app.route('/jogos/<int:id>', methods=['GET'])
def buscar_jogo(id):
    jogo = executar_query(
        "SELECT * FROM jogos WHERE id = ?",
        (id,),
        fetch=True
    )

    if jogo:
        return jsonify(dict(jogo[0])), 200

    return jsonify({"erro": "Jogo não encontrado"}), 404


# POST - INSERIR
@app.route('/jogos', methods=['POST'])
def criar_jogo():
    dados = request.get_json()

    executar_query(
        '''
        INSERT INTO jogos 
        (titulo, genero, plataforma, ano_lancamento, desenvolvedora, preco)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (
            dados.get('titulo'),
            dados.get('genero'),
            dados.get('plataforma'),
            dados.get('ano_lancamento'),
            dados.get('desenvolvedora'),
            dados.get('preco')
        ),
        commit=True
    )

    return jsonify({"mensagem": "Jogo criado com sucesso!"}), 201


# PUT - ATUALIZAR
@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    dados = request.get_json()

    # Verifica se existe
    jogo = executar_query(
        "SELECT id FROM jogos WHERE id = ?",
        (id,),
        fetch=True
    )

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query(
        '''
        UPDATE jogos SET
        titulo = ?, genero = ?, plataforma = ?,
        ano_lancamento = ?, desenvolvedora = ?, preco = ?
        WHERE id = ?
        ''',
        (
            dados.get('titulo'),
            dados.get('genero'),
            dados.get('plataforma'),
            dados.get('ano_lancamento'),
            dados.get('desenvolvedora'),
            dados.get('preco'),
            id
        ),
        commit=True
    )

    return '', 204  # padrão REST correto


# DELETE - REMOVER
@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    jogo = executar_query(
        "SELECT titulo FROM jogos WHERE id = ?",
        (id,),
        fetch=True
    )

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query(
        "DELETE FROM jogos WHERE id = ?",
        (id,),
        commit=True
    )

    return jsonify({"mensagem": f"Jogo '{jogo[0]['titulo']}' removido!"}), 200

if __name__ == '__main__':
    app.run(debug=True)