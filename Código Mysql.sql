drop database if exists Jdbc_exemplo_03;
create database jdbc_exemplo_03;

use jdbc_exemplo_03;

create table usuario (
id int primary key auto_increment not null,
nome varchar(200) not null,
pin int not null,
data_nascimento date not null,
data_acesso datetime not null
);

select * from usuario;