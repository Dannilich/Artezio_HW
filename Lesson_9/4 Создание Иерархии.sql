create table if not exists hierarchy(
	id_of_relation int not null auto_increment primary key,
    master_id int not null,
    slave_id int not null
);

insert into hierarchy
(id_of_relation, master_id, slave_id)values
(null, 1,3);

insert into hierarchy
(id_of_relation, master_id, slave_id)values
(null, 2,3);

insert into hierarchy
(id_of_relation, master_id, slave_id)values
(null, 3,4);

insert into hierarchy
(id_of_relation, master_id, slave_id)values
(null, 3,5);
