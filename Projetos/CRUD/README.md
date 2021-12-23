# CRUD

This is my first CRUD.

Inside the source folder you will find a file called "sql_configs.json" it will have the information to login to mysql server, change them depending on your settings.

It is recommended to use MySQL 8.0.27 and python 3.8.10.

In mysql console paste the following commands:

```
CREATE DATABASE TEST;
USE TEST;
CREATE TABLE TEST;
CREATE TABLE IF NOT EXISTS TEST (ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(50) NOT NULL, PASS VARCHAR(20) NOT NULL);
INSERT INTO TEST (NAME, PASS) VALUES ('root', 'root');
```

With that mysql will be ready to be used by the system.

The root user is primary and should not be deleted, he is essential for the system to work correctly.

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