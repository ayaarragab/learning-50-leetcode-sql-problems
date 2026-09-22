select s.name from SalesPerson s 
where not exists (
    select o.order_id from Orders o inner join Company c on o.com_id = c.com_id where s.sales_id = o.sales_id and c.name = "RED"
);