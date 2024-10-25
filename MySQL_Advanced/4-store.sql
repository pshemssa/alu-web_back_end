-- creating a trigger that reduce quantity of orders --

DELIMITER //
create Trigger decreases 
AFTER insert on orders
for each row 
begin 
update items
set quantity = quantity - new.number
where name = new.item_name
end //
DELIMITER;