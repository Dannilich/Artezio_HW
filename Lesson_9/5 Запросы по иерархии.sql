# Запрос на подчинённых
select master_id,slave_id from hierarchy
where master_id = 3;

# Запрос на начальников
select master_id,slave_id from hierarchy
where slave_id = 3;
