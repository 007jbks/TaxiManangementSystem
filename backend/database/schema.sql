
-- --------------------------
-- CUSTOMER TABLE
-- --------------------------
CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    password VARCHAR(100)
);

-- --------------------------
-- TAXI TABLE
-- --------------------------
CREATE TABLE Taxi (
    taxi_id INT AUTO_INCREMENT PRIMARY KEY,
    model VARCHAR(50),
    capacity INT,
    status VARCHAR(20)
);

-- --------------------------
-- DRIVER TABLE (UPDATED, FIXED)
-- --------------------------
CREATE TABLE Driver (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    taxi_id INT,
    FOREIGN KEY (taxi_id) REFERENCES Taxi(taxi_id)
);

-- --------------------------
-- BOOKING TABLE
-- --------------------------
CREATE TABLE Booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    taxi_id INT,
    source VARCHAR(100),
    destination VARCHAR(100),
    date DATETIME,
    fare DECIMAL(10,2),
    payment_status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (taxi_id) REFERENCES Taxi(taxi_id)
);
