create table livros(

id int not null AUTO_INCREMENT primary key,
titulo varchar (45) not null,
autor varchar (45) not null,
ano int not null,
genero varchar (45),
qtd int not null,
editora VARCHAR(45) not null,
data_entrada date not null

);

INSERT INTO livros (titulo, autor, ano, genero, qtd, editora, data_entrada) 
VALUES
('Dom Casmurro', 'Machado de Assis', 1899, 'Romance', 12, 'Editora Abril', '2024-11-01'),
('O Primo Basílio', 'José de Alencar', 1878, 'Romance', 8, 'Editora Martins Fontes', '2024-11-02'),
('O Alquimista', 'Paulo Coelho', 1988, 'Aventura', 15, 'Editora Rocco', '2024-11-03'),
('1984', 'George Orwell', 1949, 'Distopia', 10, 'Editora Companhia das Letras', '2024-11-04'),
('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia', 20, 'Editora Martins Fontes', '2024-11-05'),
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997, 'Fantasia', 30, 'Editora Rocco', '2024-11-06'),
('A Moreninha', 'Joaquim Manuel de Macedo', 1844, 'Romance', 5, 'Editora Saraiva', '2024-11-07'),
('A Caverna', 'José Saramago', 2000, 'Filosofia', 3, 'Editora Companhia das Letras', '2024-11-08'),
('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943, 'Infantil', 25, 'Editora Globo', '2024-11-09'),
('Moby Dick', 'Herman Melville', 1851, 'Aventura', 6, 'Editora Companhia das Letras', '2024-11-10');

CREATE TABLE estoque (
    ids INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45) NOT NULL,
    data_entradas DATE NOT NULL,  
    data_saida DATE,              
    quant INT NOT NULL,           
    id_livro INT NOT NULL,        
    preco FLOAT NOT NULL,         -- 
    codigo VARCHAR(45),
    FOREIGN KEY (id_livro) REFERENCES livros(id)
);

-- Dom Casmurro - 6 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('Dom Casmurro', CURDATE(), 1, 1, 35.00, 'DC001'),
('Dom Casmurro', CURDATE(), 1, 1, 35.00, 'DC002'),
('Dom Casmurro', CURDATE(), 1, 1, 35.00, 'DC003'),
('Dom Casmurro', CURDATE(), 1, 1, 35.00, 'DC004'),
('Dom Casmurro', CURDATE(), 1, 1, 35.00, 'DC005'),
('Dom Casmurro', CURDATE(), 1, 1, 35.00, 'DC006');

-- O Primo Basílio - 8 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('O Primo Basílio', CURDATE(), 1, 2, 30.00, 'PB001'),
('O Primo Basílio', CURDATE(), 1, 2, 30.00, 'PB002'),
('O Primo Basílio', CURDATE(), 1, 2, 30.00, 'PB003'),
('O Primo Basílio', CURDATE(), 1, 2, 30.00, 'PB004'),
('O Primo Basílio', CURDATE(), 1, 2, 30.00, 'PB005'),
('O Primo Basílio', CURDATE(), 1, 2, 30.00, 'PB006'),
('O Primo Basílio', CURDATE(), 1, 2, 30.00, 'PB007'),
('O Primo Basílio', CURDATE(), 1, 2, 30.00, 'PB008');

-- O Alquimista - 15 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA001'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA002'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA003'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA004'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA005'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA006'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA007'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA008'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA009'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA010'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA011'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA012'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA013'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA014'),
('O Alquimista', CURDATE(), 1, 3, 40.00, 'OA015');

-- 1984 - 10 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('1984', CURDATE(), 1, 4, 25.00, '1984001'),
('1984', CURDATE(), 1, 4, 25.00, '1984002'),
('1984', CURDATE(), 1, 4, 25.00, '1984003'),
('1984', CURDATE(), 1, 4, 25.00, '1984004'),
('1984', CURDATE(), 1, 4, 25.00, '1984005'),
('1984', CURDATE(), 1, 4, 25.00, '1984006'),
('1984', CURDATE(), 1, 4, 25.00, '1984007'),
('1984', CURDATE(), 1, 4, 25.00, '1984008'),
('1984', CURDATE(), 1, 4, 25.00, '1984009'),
('1984', CURDATE(), 1, 4, 25.00, '1984010');

-- O Senhor dos Anéis - 20 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA001'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA002'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA003'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA004'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA005'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA006'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA007'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA008'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA009'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA010'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA011'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA012'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA013'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA014'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA015'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA016'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA017'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA018'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA019'),
('O Senhor dos Anéis', CURDATE(), 1, 5, 50.00, 'OSA020');

-- Harry Potter e a Pedra Filosofal - 30 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP001'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP002'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP003'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP004'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP005'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP006'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP007'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP008'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP009'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP010'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP011'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP012'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP013'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP014'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP015'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP016'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP017'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP018'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP019'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP020'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP021'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP022'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP023'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP024'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP025'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP026'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP027'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP028'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP029'),
('Harry Potter e a Pedra Filosofal', CURDATE(), 1, 6, 60.00, 'HP030');

-- A Moreninha - 5 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('A Moreninha', CURDATE(), 1, 7, 35.00, 'AM001'),
('A Moreninha', CURDATE(), 1, 7, 35.00, 'AM002'),
('A Moreninha', CURDATE(), 1, 7, 35.00, 'AM003'),
('A Moreninha', CURDATE(), 1, 7, 35.00, 'AM004'),
('A Moreninha', CURDATE(), 1, 7, 35.00, 'AM005');

-- A Caverna - 3 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('A Caverna', CURDATE(), 1, 8, 45.00, 'AC001'),
('A Caverna', CURDATE(), 1, 8, 45.00, 'AC002'),
('A Caverna', CURDATE(), 1, 8, 45.00, 'AC003');

-- O Pequeno Príncipe - 25 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP001'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP002'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP003'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP004'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP005'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP006'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP007'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP008'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP009'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP010'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP011'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP012'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP013'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP014'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP015'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP016'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP017'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP018'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP019'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP020'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP021'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP022'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP023'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP024'),
('O Pequeno Príncipe', CURDATE(), 1, 9, 28.00, 'OP025');

-- Moby Dick - 6 cópias
INSERT INTO estoque (nome, data_entradas, quant, id_livro, preco, codigo) 
VALUES
('Moby Dick', CURDATE(), 1, 10, 50.00, 'MD001'),
('Moby Dick', CURDATE(), 1, 10, 50.00, 'MD002'),
('Moby Dick', CURDATE(), 1, 10, 50.00, 'MD003'),
('Moby Dick', CURDATE(), 1, 10, 50.00, 'MD004'),
('Moby Dick', CURDATE(), 1, 10, 50.00, 'MD005'),
('Moby Dick', CURDATE(), 1, 10, 50.00, 'MD006');

create table cadastro_funci(

codigo int not null auto_increment primary key,
nome varchar (50) not null,
tel int not null,
email varchar (45) not null,
cargo varchar (45) not null,
cep float not null,
login varchar (45) not null,
senha varchar (45) not null,
data_entr date not null

);

INSERT INTO cadastro_funci (nome, tel, email, cargo, cep, login, senha, data_entr)
VALUES 
('João Silva', 1198765, 'joao.silva@gmail.com', 'Gerente', '12345678', 'joao123', 'senha123', '2023-05-15'),
('Maria Oliveira', 2197654, 'maria.oliveira@gmail.com', 'Vendedor', '23456789', 'maria123', 'senha456', '2024-01-10'),
('Carlos Lima', 3196543, 'carlos.lima@gmail.com', 'Vendedor', '34567890', 'cadastro_funcicarlos123', 'senha789', '2023-08-20'),
('Ana Souza', 4195432, 'ana.souza@gmail.com', 'Caixa', '45678901', 'ana123', 'senha321', '2024-02-25'),
('Fernanda Costa', 5194321, 'fernanda.costa@gmail.com', 'Caixa', '56789012', 'fernanda123', 'senha654', '2023-11-15');

create table pagamento(

id int not null AUTO_INCREMENT primary key,
nome varchar (45) not null,
autor varchar (45) not null,
ano int not null,
genero varchar (45),
qtd int not null

);







