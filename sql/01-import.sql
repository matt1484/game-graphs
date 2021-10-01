ALTER TABLE games ADD COLUMN total_sales NUMERIC;

COPY games(
    id, title, platform, release_year, genre, 
    publisher, na_sales, eu_sales, jp_sales, 
    other_sales, total_sales
) FROM '/docker-entrypoint-initdb.d/vgsales.csv' NULL 'N/A' DELIMITER ',' CSV HEADER;

ALTER TABLE games DROP COLUMN total_sales;