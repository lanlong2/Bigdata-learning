show databases;

create database lanlong1;

use lanlong1;

select database();

select 1;

show databases;

use sql_learning;

show tables;

use lanlong1;

create table student(
id int comment "编号",
name varchar(50) comment "名字",
age int comment "年龄",
gender varchar(1) comment "性别"
) comment "用户表";

show tables;

desc student;

show create table student;

show create table student;

create table emp (
id int comment "编号",
workno varchar(10) comment "工号",
name varchar(4)  comment "姓名",
gender varchar(1) comment "性别",
age tinyint unsigned comment "年龄",
idcard char(18) comment "身份证号",
entrydate date comment "入职时间"
);

insert into emp value (01,'D0001',"崔浩","男",20,0314052400502,"2025-08-25");

select * from emp;

delete from emp where id = 1;

select * from emp;

select * from user；