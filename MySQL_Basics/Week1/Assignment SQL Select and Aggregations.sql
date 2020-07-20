/*
 Assignment: SQL Select and Aggregations
Please use the tables in the flights database. Your deliverable should include the SQL queries that you write in
support of your conclusions.
*/

-- 1. Which destination in the flights database is the furthest distance away, based on information in the flights table.
-- Show the SQL query(s) that support your conclusion.
SELECT dest, distance FROM flights.flights ORDER BY distance DESC LIMIT 1;
dest	distance
HNL		4983
-- 2. What are the different numbers of engines in the planes table? For each number of engines, which aircraft have
-- the most number of seats? Show the SQL statement(s) that support your result.
SELECT engines, max(seats) from flights.planes group by engines order by engines;
1	16
2	400
3	379
4	450

-- 3. Show the total number of flights.
SELECT COUNT(*) from flights.flights;
336776

-- 4. Show the total number of flights by airline (carrier).

-- 5. Show all of the airlines, ordered by number of flights in descending order.

-- 6. Show only the top 5 airlines, by number of flights, ordered by number of flights in descending order.

-- 7. Show only the top 5 airlines, by number of flights of distance 1,000 miles or greater, ordered by number of
-- flights in descending order.

-- 8. Create a question that (a) uses data from the flights database, and (b) requires aggregation to answer it, and
-- write down both the question, and the query that answers the question.