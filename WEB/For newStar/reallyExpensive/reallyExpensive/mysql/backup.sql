create database db_buy_flag;
use db_buy_flag;
create table tb_user (
    id int primary key auto_increment,
    username varchar(100) not null ,
    password varchar(300) not null ,
    balance double default 10 not null
) character set utf8;

create table tb_good(
    id   int primary key auto_increment,
    name varchar(200) not null ,
    description varchar(200) not null ,
    cost double not null
) character set utf8;

insert into tb_good values (null, 'flag1', 'too young too simple!', 3);
insert into tb_good values (null, 'flag2', 'you are closer to flag',10);
insert into tb_good values (null, 'flag3', 'haha,this is fake flag',7);
insert into tb_good values (null, 'flag4','Are you crazy?Can true flag be so cheap?' ,1);
insert into tb_good values (null, 'flag5', 'You win!True flag is flag{^==^Y0uG@t$(t]$[r)^u^(e)-F10g!^<>^}', 999999999);
