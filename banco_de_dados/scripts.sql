CREATE DATABASE dados_abertos;
USE dados_abertos;

CREATE TABLE demonstracoes_contabeis (
    data DATE,
    reg_ans INT,
    cd_conta_contabil VARCHAR(100),
    descricao TEXT,
    vl_saldo_inicial DECIMAL(16, 2),
    vl_saldo_final DECIMAL(16, 2)
);

CREATE TABLE operadoras (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(40),
    fax VARCHAR(20),
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_de_comercializacao TEXT,
    data_registro_ans DATE
);

DROP TABLE operadoras;

SELECT * FROM demonstracoes_contabeis;
SELECT COUNT(*) FROM demonstracoes_contabeis;

SELECT * FROM operadoras;
SELECT COUNT(*) FROM operadoras;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_data/processed_1T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_data/processed_1T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_data/processed_2T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_data/processed_2T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_data/processed_3T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_data/processed_3T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_data/processed_4T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_data/processed_4T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/processed_data/processed_Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@registro_ans, @cnpj, @razao_social, @nome_fantasia, @modalidade, @logradouro, @numero, @complemento, @bairro, @cidade, @uf, @cep, @ddd, @telefone, @fax, @endereco_eletronico, @representante, @cargo_representante, @regiao_de_comercializacao, @data_registro_ans)
SET
    registro_ans = @registro_ans,
    cnpj = @cnpj,
    razao_social = @razao_social,
    nome_fantasia = @nome_fantasia,
    modalidade = @modalidade,
    logradouro = @logradouro,
    numero = @numero,
    complemento = @complemento,
    bairro = @bairro,
    cidade = @cidade,
    uf = @uf,
    cep = @cep,
    ddd = @ddd,
    telefone = @telefone,
    fax = @fax,
    endereco_eletronico = @endereco_eletronico,
    representante = @representante,
    cargo_representante = @cargo_representante,
    regiao_de_comercializacao = @regiao_de_comercializacao,
    data_registro_ans = STR_TO_DATE(@data_registro_ans, '%Y-%m-%d');

SELECT oc.razao_social, dc.descricao, SUM(dc.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras oc ON dc.reg_ans = oc.registro_ans
WHERE 
	LOWER(dc.descricao) LIKE LOWER('%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE%')
	AND dc.data >= DATE_SUB((SELECT MAX(data) FROM demonstracoes_contabeis), INTERVAL 3 MONTH)
GROUP BY dc.reg_ans, oc.razao_social, dc.descricao
ORDER BY total_despesas DESC
LIMIT 10;

SELECT oc.razao_social, descricao, SUM(dc.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN operadoras oc ON dc.reg_ans = oc.registro_ans
WHERE 
    LOWER(dc.descricao) LIKE LOWER('%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE%')
    AND YEAR(dc.data) = 2024
GROUP BY dc.reg_ans, oc.razao_social, dc.descricao
ORDER BY total_despesas DESC
LIMIT 10;
