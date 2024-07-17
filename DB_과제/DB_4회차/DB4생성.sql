-- insert into customers(
-- customerNumber,
-- customerName,
-- contactLastName,
-- contactFirstName,
-- phone,addressLine1,
-- addressLine2,
-- city,
-- state,
-- postalCode,
-- country,
-- salesRepEmployeeNumber,
-- creditLimit)
-- value (
-- '497',
-- 'hello',
-- 'lee',
-- 'donghyuk',
-- '010 1234 5678',
-- 'gwangju',
-- null,
-- 'gwangju2',
-- null,
-- null,
-- 'korea',
-- null,
-- 123000.00);

-- INSERT INTO products(productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
-- VALUES ('S10_1677', '붕부이', 'Classic Cars', '1:10', 'Diecast', 'This replica features working kickstand, front suspension, gear-shift lever, footrests, and rear suspension.', 7933, 48.81, 95.70);

-- INSERT INTO employees(employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
-- VALUES (1708, 'Kim', 'Seoyoon', 'x556', 'skim@classicmodels.com', '7', null, 'Sales Rep');

-- INSERT INTO `classicmodels`.`offices` (`officeCode`, `city`, `phone`, `addressLine1`, `country`) VALUES ('8', 'Korea', '+82 010 1234 5678', 'address', 'Korea');

-- INSERT INTO `classicmodels`.`orders` (`orderNumber`, `orderDate`, `requiredDate`, `status`, `customerNumber`) VALUES ('10426', '2024-07-17', '2024-07-17', 'In Process', '363');

-- INSERT INTO orderdetails(orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
-- VALUES (10426, 'S72_3212', 2, 48.81, 1);

-- INSERT INTO payments(customerNumber, checkNumber, paymentDate, amount)
-- VALUES (497, 'CH34567', '2024-07-17', 150.00);

-- INSERT INTO productlines(productLine, textDescription, htmlDescription, image)
-- VALUES ('Super car', 'Motorcycle models from various manufacturers.', '<p>Explore our collection of detailed motorcycle models.</p>', NULL);

-- INSERT INTO `classicmodels`.`customers` (`customerNumber`, `customerName`, `contactLastName`, `contactFirstName`, `country`, `salesRepEmployeeNumber`) VALUES ('501', 'hi', 'mol', 'ra', 'Africa', '1708');

-- INSERT INTO productlines (productLine, textDescription) 
-- VALUES ('Electronics', 'Modern electronic devices and gadgets');