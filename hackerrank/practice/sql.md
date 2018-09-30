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
## Advanced Select
### Type of Triangle
```sql
-- MySQL
select 
if(a>b and a>c and a>=b+c,"Not A Triangle",
   if(b>a and b>c and b>=a+c,"Not A Triangle",
      if(c>a and c>b and c>=a+b,"Not A Triangle",
         if(a=b and b=c,"Equilateral",
            if(a=b or b=c or a=c,"Isosceles","Scalene")
           )
        )
     )
  )
from TRIANGLES 
```
```sql
-- MySQL
select 
if(2*GREATEST(a,b,c)>=a+b+c,"Not A Triangle",
    if(a=b and b=c,"Equilateral",
        if(a=b or b=c or a=c,"Isosceles","Scalene")
    )
)
from TRIANGLES 
```
### The PADS
```sql
-- MySQL
select CONCAT(name,if(OCCUPATION='Doctor',"(D)",
            if(OCCUPATION='Professor',"(P)",
                if(OCCUPATION='Singer',"(S)","(A)")
                )
            )
       )
from OCCUPATIONS
order by name;

SELECT concat('There are a total of ',count(name),' ',LOWER(OCCUPATION),'s.')
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(name), OCCUPATION;
```
