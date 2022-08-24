SELECT
	z.order_item_id,
	a.order_date,
	d.user_first_name,
	z.order_item_quantity,
	b.product_name,
	a.order_price,
	a.order_discount,
	h.voucher_price,
	a.order_total 
FROM
	tb_order_items z
	LEFT JOIN tb_orders a ON z.order_id = a.order_id
	LEFT JOIN tb_products b ON z.product_id = b.product_id
	LEFT JOIN tb_payments e ON a.payment_id = e.payment_id
	LEFT JOIN tb_shippers f ON a.shipper_id = f.shipper_id
	LEFT JOIN tb_ratings G ON a.rating_id = G.rating_id
	LEFT JOIN tb_vouchers h ON a.voucher_id = h.voucher_id
	LEFT JOIN tb_users d ON a.user_id = d.user_id
	LEFT JOIN tb_product_category pc ON b.product_category_id = pc.product_category_id