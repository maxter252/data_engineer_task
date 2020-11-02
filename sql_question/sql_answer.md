The total revenue is 4390

```SQL
SELECT SUM(price*quantity) FROM (
  SELECT product, price_effective_date as start_date,  
    LEAD(price_effective_date, 
      1, 
      ((select MAX(sales_date) + INTERVAL '1' day from sales) )::DATE 
      ) 
      OVER
    (PARTITION BY product ORDER BY price_effective_date) AS end_date,
    price
  FROM prices) prices_window
INNER JOIN sales 
  on sales.sales_date >= prices_window.start_date 
  and sales.sales_date < prices_window.end_date 
  and sales.product = prices_window.product; 
```


The following can be used to set up the data to test:
```SQL
CREATE TABLE IF NOT EXISTS prices (
  product CHAR(254),
  price_effective_date DATE,
  price int
);

CREATE TABLE IF NOT EXISTS sales (
  product CHAR(254),
  sales_date DATE,
  quantity int
);

INSERT INTO prices VALUES ('product_1', '2018-01-01', 50);
INSERT INTO prices VALUES ('product_2', '2018-01-01', 40);
INSERT INTO prices VALUES ('product_1', '2018-01-03', 25);
INSERT INTO prices VALUES ('product_2', '2018-01-05', 20);
INSERT INTO prices VALUES ('product_1', '2018-01-10', 50);
INSERT INTO prices VALUES ('product_2', '2018-01-12', 40);

INSERT INTO sales VALUES ('product_1', '2018-01-01', 10);
INSERT INTO sales VALUES ('product_2', '2018-01-02', 12);
INSERT INTO sales VALUES ('product_1', '2018-01-04', 50);
INSERT INTO sales VALUES ('product_2', '2018-01-06', 70);
INSERT INTO sales VALUES ('product_1', '2018-01-12', 8);
INSERT INTO sales VALUES ('product_2', '2018-01-15', 9);
```