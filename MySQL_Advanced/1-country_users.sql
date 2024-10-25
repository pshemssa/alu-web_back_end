-- creating user table if it doesn't exist --
create Table if NOT exists users (
    id int not NULL auto_increment primary key,
    email VARCHAR(255) not null UNIQUE,
    name varchar (255),
    country CHAR(2) not null DEFAULT'US' check (country in ('US', 'CO', 'TN'))

);

