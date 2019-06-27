drop table if exists user;
create table user (
  id varchar(45) primary key,
  password varchar(25) not null,
  username varchar(20) not null,
  money_plus int not null default 0,
  money_minus int not null default 0,
  amount int not null default 0
);

drop table if exists goal;
create table goal (
  goal_id int auto_increment primary key,
  goal_name varchar(45) not null,
  duration int not null ,
  amount int not null ,
  user_limit int not null ,
  money_stack int not null ,
  status boolean not null,
  description text
);

drop table if exists team;
create table team (
    goal_id int primary key references goal(goal_id) on update cascade,
    user_id varchar(45) primary key references user(id) on update cascade,
    date date primary key,
    image text primary key
);

