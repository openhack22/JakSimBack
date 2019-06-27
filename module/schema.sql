drop database if exists jaksim;

create database jaksim;

use jaksim;

drop table if exists user;
create table user (
  id varchar(45) primary key,
  password varchar(25) not null,
  username varchar(20) not null,
  income int not null default 0,
  outcome int not null default 0,
  amount int not null default 0,
  bank varchar(20) default null,
  cardnum varchar(45) default null,
  cvc varchar(3) default null,
  carddue date default null,
  cardpassword varchar(45) default null
) DEFAULT CHARSET=utf8 COLLATE utf8_general_ci;

drop table if exists goal;
create table goal (
  goal_id int primary key,
  goal_name varchar(20) not null,
  user_id varchar(45) not null,
  duration int not null ,
  amount int not null ,
  user_limit int not null ,
  description text,
  status boolean not null default 0
) DEFAULT CHARSET=utf8 COLLATE utf8_general_ci;

drop table if exists team;
create table team (
  goal_id int references goal(goal_id) on update cascade,
  goal_name varchar(20) not null,
  user_id varchar(45) references user(id) on update cascade,
  date datetime,
  image text,
  status boolean not null default 0,
  PRIMARY KEY( goal_id, user_id, date )
) DEFAULT CHARSET=utf8 COLLATE utf8_general_ci;

