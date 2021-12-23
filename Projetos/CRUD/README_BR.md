# CRUD

Este é o meu primeiro CRUD.

Dentro da pasta source você irá encontrar um arquivo chamado "sql_configs.json" ele irá ter as informações para fazer login no mysql server, mude elas depedendo das suas configurações.

É recomendado o uso do Mysql 8.0.27 e do python 3.8.10.

No mysql console cole os seguintes comandos :

```
CREATE DATABASE TEST;
USE TEST;
CREATE TABLE TEST;
CREATE TABLE IF NOT EXISTS TEST (ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(50) NOT NULL, PASS VARCHAR(20) NOT NULL);
INSERT INTO TEST (NAME, PASS) VALUES ('root', 'root');
```

Com isso o mysql estará pronto para ser utilizado pelo sistema.

O usuário root é primario e não deve ser deletado, ele é essencial para que o sistema funcione corretamente.

# SCREENSHOTS

## Login

<p align="center">
  <img src="https://user-images.githubusercontent.com/81983803/147279676-c1eac9d1-0c2f-4ece-b3fa-ae85178fa345.png" alt="login-screen"/>
</p>

## Create Account

<p align="center">
  <img src="https://user-images.githubusercontent.com/81983803/147279731-9609a66e-9eb0-4cd9-bda6-3fe9acf88365.png" alt="create-screen"/>
</p>

## List Accounts

<p align="center">
  <img src="https://user-images.githubusercontent.com/81983803/147283143-2841caaa-4b38-4cd8-be20-646ff60d7135.png" alt="list-screen"/>
</p>