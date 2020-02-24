#jobs
#-------------------------------------------
insert into jobs
(id, job_name)values
(1, 'Надзиратель');

insert into jobs
(id, job_name)values
(2, 'Раб');

insert into jobs
(id, job_name)values
(3, 'Царь');
#-------------------------------------------
#stuff
#-------------------------------------------
insert into staff
(worker_id, first_name, second_name, job_id, salary)values
(null, 'Иван', 'Добров', 3, 60000);

insert into staff
(worker_id, first_name, second_name, job_id, salary)values
(null, 'Даниил', 'Алексеевич', 3, 160000);

insert into staff
(worker_id, first_name, second_name, job_id, salary)values
(null, 'Насяльнике', 'Рыжов', 1, 29999.99);

insert into staff
(worker_id, first_name, second_name, job_id, salary)values
(null, 'Равшан', 'Ахамбаев', 2, 12000);

insert into staff
(worker_id, first_name, second_name, job_id, salary)values
(null, 'Джамшут', 'Ахамбаев', 2, 42000);
