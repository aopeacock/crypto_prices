create table if not exists price_history (
    price_history_id serial PRIMARY KEY,
    ticker varchar(10),
    coin_name varchar(40),
    price_dt date,
    open numeric(15,2),
    high numeric(15,2),
    low numeric(15,2),
    close numeric(15,2),
    volume numeric(15,2),
    currency varchar(10)
);

create sequence seq_price_history start 1000 owned by price_history.price_history_id;