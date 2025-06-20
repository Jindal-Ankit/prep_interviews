## 1.  
> Problem: Find accounts with no transactions in the last 12 months (as of 2025-06-18)
```SQL 
-- Schema
CREATE TABLE accounts (
  account_id INT PRIMARY KEY,
  customer_id INT,
  open_date DATE,
  close_date DATE NULL
);

CREATE TABLE txns (
  txn_id INT PRIMARY KEY,
  account_id INT,
  txn_date DATE,
  amount NUMERIC(10,2),
  type VARCHAR(10)
);

-- Data
INSERT INTO accounts VALUES
 (100,1,'2020-01-15',NULL),
 (101,2,'2024-03-01',NULL),
 (102,3,'2022-06-10',NULL);
 (103,4,'2023-06-10',NULL);

INSERT INTO accounts VALUES
 (103,4,'2023-06-10',NULL);

INSERT INTO txns VALUES
 (201,100,'2024-10-01',100.00,'deposit'),
 (202,100,'2025-03-15',200.00,'deposit'),
 (203,101,'2025-01-10',300.00,'withdrawal'),
 (204,102,'2023-11-05',400.00,'deposit');

INSERT INTO txns VALUES
(205,102,'2023-11-06',1100.00,'deposit');
```