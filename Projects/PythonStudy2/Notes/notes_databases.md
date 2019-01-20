# Databases and SQL

## Basic Info

- Tables should store data related to one thing.  Related data should be stored in separate tables.
- The PostgreSQL PGAdmin tool requires single quotes for strings
- **DDL** - Data Definition Danguage
- **DML** - Data Manipulation Language

### Run PostgreSQL in VS Code

    F5

## SQL

### Comments

Using comments

```sql
/* THIS IS A COMMENT */
```

### SELECT

Select all rows and columns from a table

```sql
SELECT * FROM customers
```

Select all rows and only specific columns from a table

```sql
SELECT id, last_name
FROM customers
```

### WHERE

Use the 'WHERE' clause to filter returned rows

```sql
SELECT id, last_name 
FROM customers
WHERE last_name='Adam' OR last_name='Watson'
```

### AS

Give a friendly name to a column or table

```sql
SELECT customers.id AS custID
FROM customers
```

### LIMIT

Limit the number of rows returned

```sql
SELECT customers.first_name, customers.last_name 
FROM customers LIMIT 1;
```

### UPDATE

Update specific values

```sql
UPDATE items
SET price = 4.00
WHERE id = 3;
```

### DELETE rows

Delete rows that meet specific criteria

```sql
DELETE FROM items WHERE id=4;
```

### LIKE

Use LIKE for more advanced filtering

**NOTE:** This is taxing to the server so it should be avoided where possible

#### Using underscores to denote the number of characters

```SQL
SELECT * FROM customers
WHERE last_name LIKE '____'  /* returns last names with 4 chars*/
```

#### Using the wildcard symbol '%'

```sql
SELECT * FROM customers
WHERE last_name LIKE '%'
/* returns all rows */
```

```sql
SELECT * FROM customers
WHERE last_name LIKE 'S%' 
/* returns last names that start with a capital S */
```

```sql
SELECT * FROM customers
WHERE last_name LIKE '%a%' 
/* returns last names that contain an lower case a */
```

#### Combining wildcards and underscores

```sql
SELECT * FROM customers
WHERE last_name LIKE '%t_'
/* returns last names where 't' is the second to last character */
```

### JOINS

- JOINs treat rows of data as if they were Sets
- We can perform set operations on the tables
- JOINs are fairly quick and do not caue a major performance hit

#### INNER JOIN

- Set intersection is the elements common to two sets
- INNER JOIN is similar to **set intersection**
- INNER JOIN selects rows from table 1 and table2 where they match the selecting column

    ```sql
    SELECT * FROM Customers
    INNER JOIN Orders
    ON Customers.ID = Orders.Customer_ID
    ```

#### LEFT JOIN

- This selects all rows from the table1 (on the left), and the rows from table2 (on the right) **if they match**
- If they don't match, the data for the right table is blank

    ```sql
    SELECT * FROM Customers
    LEFT JOIN Orders
    ON Customer.ID = Orders.Customer_ID
    ```

#### RIGHT JOIN

- Opposite of LEFT JOIN
- - This selects all rows from the table2 (on the right), and the rows from table1 (on the left) **if they match**
- If they don't match, the data for the left table is blank

    ```sql
    SELECT * FROM Customers
    RIGHT JOIN Orders
    ON Customer.ID = Orders.Customer_ID
    ```

#### FULL JOIN

- This selects all rows from both tables, matching them if there is a match on the selected column

    ```sql
    SELECT * FROM Customers
    FULL JOIN Orders
    ON Customer.ID = Orders.Customer_ID
    ```








### CREATE Table

```SQL
CREATE USER hans_gruber WITH
    LOGIN
    NOSUPERUSER
    CREATEDB
    NOCREATEROLE
    INHERIT
    NOREPLICATION
    CONNECTION LIMIT -1
    PASSWORD 'xxxxxx';

CREATE DATABASE learning
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

create table course(
    course_id   varchar(8) primary key,
    title       varchar(50),
    dept_name   varchar(20),
    credits     varchar(2,0),
    foreign key (dept_name) references department
);
```