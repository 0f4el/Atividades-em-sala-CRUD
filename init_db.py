import sqlite3

def criar_banco():
    conn = sqlite3.connect('jogos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            plataforma TEXT NOT NULL,
            ano_lancamento INTEGER,
            desenvolvedora TEXT,
            preco REAL
        )
    ''')
    
    jogos_exemplo = [ 
    ('The Legend of Zelda', 'Aventura', 'Nintendo Switch', 2017, 'Nintendo', 249.90), 
    ('God of War Ragnarök', 'Ação-Aventura', 'PlayStation 5', 2022, 'Santa Monica Studio', 299.90), 
    ('Elden Ring', 'RPG', 'PC', 2022, 'FromSoftware', 199.90), 
    ('Red Dead Redemption 2', 'Ação-Aventura', 'PC', 2018, 'Rockstar Games', 129.90), 
    ('Super Mario Odyssey', 'Plataforma', 'Nintendo Switch', 2017, 'Nintendo', 299.90) 
    ] 
    cursor.executemany(''' INSERT OR IGNORE INTO jogos (titulo, genero, plataforma, ano_lancamento, desenvolvedora, preco) VALUES (?, ?, ?, ?, ?, ?) ''', jogos_exemplo)

    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso")

if __name__ == '__main__':
    criar_banco()