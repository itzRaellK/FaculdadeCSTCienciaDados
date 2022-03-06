
-- Exercício Faculdade
-- Atividade 2 - Inserindo dados nas tabelas

-- TRUNCATE TABLE tb_pais, tb_equipe, tb_piloto, tb_circuito RESTART IDENTITY;
-- SELECT * FROM tb_piloto;
SELECT * FROM tb_circuito;

-- Tabela País
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('Holanda', 17.673);		-- id = 1
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('Inglaterra', 55.450);	-- id = 2
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('Finlândia', 5.531);		-- id = 3
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('México', 128.9);		-- id = 4
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('Austrália', 25.69);		-- id = 5
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('França', 67.39);		-- id = 6
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('Espanha', 47.35);		-- id = 7
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('Alemanha', 83.24);		-- id = 8
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('Áustria', 8.917);		-- id = 9
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('Bélgica', 11.56);		-- id = 10
INSERT INTO tb_pais(nm_pais, nr_populacao) VALUES ('Itália', 59.55)			-- id = 11

-- Tabela Equipe
INSERT INTO tb_equipe(nm_equipe, id_pais) VALUES ('Mercedes', 8); 			-- id = 1
INSERT INTO tb_equipe(nm_equipe, id_pais) VALUES ('Red Bull', 9);			-- id = 2
INSERT INTO tb_equipe(nm_equipe, id_pais) VALUES ('Alpino', 6);				-- id = 3
INSERT INTO tb_equipe(nm_equipe, id_pais) VALUES ('McLaren', 2);			-- id = 4

-- Tabela Piloto
INSERT INTO tb_piloto(nm_piloto, dt_nascimento, id_pais, id_equipe) VALUES ('Max Verstappen', '30/09/1997', 10, 2);
INSERT INTO tb_piloto(nm_piloto, dt_nascimento, id_pais, id_equipe) VALUES ('Lewis Hamilton', '07/01/1985', 2, 1);
INSERT INTO tb_piloto(nm_piloto, dt_nascimento, id_pais, id_equipe) VALUES ('Valtteri Bottas', '28/07/1989', 3, 3);
INSERT INTO tb_piloto(nm_piloto, dt_nascimento, id_pais, id_equipe) VALUES ('Sergio Pérez', '26/01/1990', 4, 2);
INSERT INTO tb_piloto(nm_piloto, dt_nascimento, id_pais, id_equipe) VALUES ('Daniel Ricciardo', '01/06/1989', 5, 4);
INSERT INTO tb_piloto(nm_piloto, dt_nascimento, id_pais, id_equipe) VALUES ('Fernando Alonso', '29/07/1981', 7, 3);

-- Tabela Circuito
INSERT INTO tb_circuito(nm_circuito, nr_extensao, id_pais) VALUES ('Autodromo Imola', 310, 11);
INSERT INTO tb_circuito(nm_circuito, nr_extensao, id_pais) VALUES ('Circuito da Catalunha', 307, 7);
INSERT INTO tb_circuito(nm_circuito, nr_extensao, id_pais) VALUES ('Paul Ricard Circuit', 309, 6);

-- Tabela Prova
