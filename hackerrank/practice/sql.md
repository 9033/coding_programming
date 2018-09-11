# Practice > SQL
## Basic Select
### Weather Observation Station 5
```sql
/* MySQL */
select city,CHAR_LENGTH(city) from station order by CHAR_LENGTH(city),city limit 1;
select city,CHAR_LENGTH(city) from station order by CHAR_LENGTH(city) desc,city limit 1;
```
### Weather Observation Station 8
```sql
/* MySQL */
select distinct city from station where LEFT(city, 1) in ('a','e','o','i','u') and right(city, 1) in ('a','e','o','i','u');
```
