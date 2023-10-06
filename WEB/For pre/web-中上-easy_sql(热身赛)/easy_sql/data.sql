create database hsctffinal;
use hsctffinal;

-- we don't know how to generate schema hsctffinal (class Schema) :(
create table if not exists images
(
	id int auto_increment
		primary key,
	path varchar(100) null
)
;

create table if not exists users
(
	username varchar(100) not null
		primary key,
	password varchar(100) null,
	flag varchar(100) null
)
;

INSERT INTO images (id, path) VALUES (1, 'images/jiaran1.jpg');
INSERT INTO images (id, path) VALUES (2, 'images/jiaran2.jpg');
INSERT INTO images (id, path) VALUES (3, 'images/jiaran3.jpg');

INSERT INTO users values ('admin', SUBSTR(MD5(RAND()),1,20),'flag{Gu@ng2hU_j1arAn_Dundun_ji3Chan9}');
