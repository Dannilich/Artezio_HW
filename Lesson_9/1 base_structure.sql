create database if not exists staff_db;
use staff_db;

create table if not exists staff(
	worker_id int not null auto_increment primary key,
	first_name varchar(30) not null,
    second_name varchar(30) not null,
    job_id integer not null,
    salary decimal(15,2) not null
);

create table if not exists jobs(
	id int not null auto_increment primary key,
    job_name varchar(20) not null unique
);
