-- creating a trigger that reduce quantity of orders --

DELIMITER $$

create Trigger decreases AFTER INSERT ON orders
for each row update items
set quantity = quantity - new.number
where name = new.item_name