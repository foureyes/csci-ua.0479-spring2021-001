---
layout: slides
title: "Views, Functions, and Triggers"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## 
CREATE OR REPLACE FUNCTION
percent_change(new_value numeric,
               old_value numeric,
               decimal_places integer DEFAULT 1)
RETURNS numeric AS
'SELECT round(
        ((new_value - old_value) / old_value) * 100, decimal_places
);'
LANGUAGE SQL
IMMUTABLE
RETURNS NULL ON NULL INPUT;

</section>


<section markdown="block">
## 

create or replace function parse_name(
    s varchar
  )
  returns varchar[] as $$
declare
  result varchar[];
begin
  select
         array[trim(array_to_string(parts[1:array_length(parts, 1) - 1], ' '))::varchar,
         trim(parts[array_length(parts, 1)])::varchar]
  into result
  from (select string_to_array(s, ' ') as parts) as name_parts;
  return result;
end;
</section>
<section markdown="block">
## 

</section>

{% comment %}
<section markdown="block">
## 

https://github.com/anthonydb/practical-sql/blob/master/Chapter_04/Chapter_04.sql
https://learning-oreilly-com.proxy.library.nyu.edu/library/view/practical-sql/9781492067580/xhtml/ch04.xhtml:q
https://github.com/anthonydb/practical-sql/blob/master/Chapter_04/us_counties_2010.csv

</section>

<section markdown="block">
## 

</section>
{% endcomment %}
