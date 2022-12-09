
# create databae 
```commandline
mysql> use protectpe
Database changed
mysql> CREATE TABLE `transaction` (
    ->   `id` varchar(50) NOT NULL,
    ->   `user_id` varchar(50) NOT NULL,
    ->   `merchant_upi_id` varchar(50) NOT NULL,
    ->   `transaction_amount` int NOT NULL,
    ->   `status` varchar(255) DEFAULT NULL,
    ->   `created_at` datetime NOT NULL,
    ->   PRIMARY KEY (`id`),
    ->   UNIQUE KEY `id` (`id`)
    -> ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
Query OK, 0 rows affected (0.02 sec)

mysql> CREATE TABLE `registration` (
    ->   `phone_number` varchar(20) NOT NULL,
    ->   `primary_owner` varchar(20) NOT NULL,
    ->   `description` varchar(255) DEFAULT NULL,
    ->   `regular_limit` int NOT NULL,
    ->   `max_limit` int NOT NULL,
    ->   `is_active` tinyint(1) DEFAULT NULL,
    ->   `qr_code` varchar(255) DEFAULT NULL,
    ->   `verification_status` varchar(20) DEFAULT NULL,
    ->   `created_at` datetime NOT NULL,
    ->   PRIMARY KEY (`phone_number`),
    ->   CONSTRAINT `registration_chk_1` CHECK ((`is_active` in (0,1)))
    -> ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    -> ;
Query OK, 0 rows affected, 1 warning (0.01 sec)
```