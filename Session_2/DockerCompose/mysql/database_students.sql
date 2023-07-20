create database db;

use db;

create table student(stdid int not null auto_increment primary key, name varchar(20), email varchar(20));

insert into student(name,email) values("Logesh","logeshmano@gmail.com"),("Vasanth","vasanthvk@gmail.com"); 