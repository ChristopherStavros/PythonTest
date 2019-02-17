DROP TABLE IF EXISTS learning.users;

CREATE TABLE learning.users(
    id SERIAL PRIMARY KEY,
    email character VARYING(255),
    first_name character VARYING(255),
    last_name character VARYING(255)
);