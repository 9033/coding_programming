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
### Occupations
```sql
-- MySQL
set @d=0, @p=0, @s=0, @a=0;
select min(d),min(p),min(s),min(a)
from(
    select
     case when occupation='Doctor' then @d:=@d+1
          when occupation='Professor' then @p:=@p+1
          when occupation='Singer' then @s:=@s+1
          when occupation='Actor' then @a:=@a+1
     end as i
    ,case when occupation='Doctor' then name end as d
    ,case when occupation='Professor' then name end as p
    ,case when occupation='Singer' then name end as s
    ,case when occupation='Actor' then name end as a
    from OCCUPATIONS
    order by name
) f
group by i
;
```
