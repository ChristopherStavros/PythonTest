DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    email character VARYING(255),
    first_name character VARYING(255),
    last_name character VARYING(255)
);