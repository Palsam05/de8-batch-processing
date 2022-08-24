DROP TABLE IF EXISTS fact_orders;
CREATE TABLE fact_orders(
	order_item_id INT NOT NULL ,
    order_date DATE NOT NULL,
	user_first_name VARCHAR(255) NOT NULL,
	order_item_quantity INT,
	product_name VARCHAR(255) NOT NULL,
	order_price INT NOT NULL,
	order_discount INT,
	voucher_price VARCHAR(25),
	order_total INT NOT NULL,
    PRIMARY KEY (order_item_id)
);