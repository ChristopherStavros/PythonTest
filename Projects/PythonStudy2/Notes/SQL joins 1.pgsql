SELECT * 
FROM items 
INNER JOIN purchases ON items.id = purchases.item_id;

SELECT * 
FROM customers
INNER JOIN purchases ON customers.id = purchases.customer_id
INNER JOIN items ON purchases.item_id = items.id;

