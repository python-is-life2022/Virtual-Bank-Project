CREATE TABLE users (user_id INT PRIMARY KEY AUTO_INCREMENT,
					f_name VARCHAR(30) NOT NULL,
                    l_name VARCHAR(30) NOT NULL,
                    age INT NOT NULL,
                    b_date DATE NOT NULL,
                    n_id VARCHAR(10) UNIQUE NOT NULL,
                    tel VARCHAR(11) UNIQUE NOT NULL,
                    email VARCHAR(55) UNIQUE NOT NULL,
                    address VARCHAR(120) NOT NULL,
                    b_save INT NOT NULL,
                    username VARCHAR(20) UNIQUE NOT NULL,
                    pass_w VARCHAR(20) NOT NULL,
                    create_time DATETIME DEFAULT(current_timestamp()));

SELECT * FROM users;

-- ALTER TABLE users ADD COLUMN account_number VARCHAR(16) UNIQUE NOT NULL;
-- ALTER TABLE users ADD COLUMN cart_pass VARCHAR(4) NOT NULL;
ALTER TABLE users MODIFY email VARCHAR(60) UNIQUE NOT NULL;