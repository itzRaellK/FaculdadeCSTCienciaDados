
-- Exercícios para Faculdade
-- ATIVIDADE 1

CREATE DATABASE tabelaFormulaUm;

-- DROP TABLE tb_pais, tb_piloto, tb_equipe, tb_circuito, tb_prova, tb_resultado;

CREATE TABLE tb_pais(
	id SERIAL PRIMARY KEY,
	nm_pais VARCHAR(20) NOT NULL,
	nr_populacao NUMERIC(8,3) NOT NULL
);

CREATE TABLE tb_piloto(
	id SERIAL PRIMARY KEY,
	nm_piloto VARCHAR(30) NOT NULL,
	dt_nascimento DATE NOT NULL,
	id_pais INT NOT NULL,
	id_equipe INT NOT NULL
);

CREATE TABLE tb_equipe(
	id SERIAL PRIMARY KEY,
	nm_equipe VARCHAR(20),
	id_pais INT NOT NULL
);

CREATE TABLE tb_circuito(
	id SERIAL PRIMARY KEY,
	nm_circuito VARCHAR(30),
	nr_extensao NUMERIC(8,3) NOT NULL,
	id_pais INT NOT NULL
);

CREATE TABLE tb_prova(
	id SERIAL PRIMARY KEY,
	dt_prova DATE NOT NULL,
	nm_situacao VARCHAR(30) NOT NULL,
	id_circuito INT NOT NULL
);

CREATE TABLE tb_resultado(
	id_prova INT NOT NULL,
	id_piloto INT NOT NULL,
	nr_tempo_prova TIME NOT NULL,
	nr_colocacao_final INT NOT NULL,
	nr_posicao_grid INT NOT NULL,
	nr_melhor_volta TIME NOT NULL
);