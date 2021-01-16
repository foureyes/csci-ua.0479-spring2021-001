# Agenda

## aggregation slides

## import school districts as review / demo

* using copy vs \copy
	* `\copy school_district from Gaz_unsd_national.txt csv header delimiter as E'\t' encoding 'latin1'`
* show largest school district
* show total population of each state by summing population in each school district
* show number of school districts per state
* show largest school district's population in each state
* do the same, including name of school district (is this even possible)
	* show group by error!
	* how to????
	* btw, note no pk... sooo
```
select school_district.state, school_district.name, mp.max_pop 
from school_district 
	inner join (
			select state, max(population) as max_pop 
			from school_district 
			group by state 
			order by max_pop desc) as mp 
		on mp.state = school_district.state 
		and mp.max_pop = school_district.population; 
```

## using metals as demo

* create table (exercise / see sql file)
	* varchar vs text, check constraint can be changed "faster"
* tasks - work with data set to determine the highest concentration of some metal in a product, per country
	1. show our tables columns as a check
	2. explore - show some rows
	3. what are the possible units for concentrations, but without duplicates?
	4. how many entries are there for each unit?
	5. what are the countries in the list, no duplicates?
	6. how many product entries does each country have? <-- or what is the average concentration of metal
		* show the same, by sorted such that most entries are at the top 
		* does it work without an alias and with alias?
		* now, only show the ones that have more than one product
		* with alias and without!
	7. show the concentration of the product with the highest concentration for each country, do so for concentration measurements w most frequent
	8. same as above, but show the name of the product as well
	9. max concentration overall
	10. get the name associated with?
		* difference with this and order by and limit

## constraints and naming conventions

## joins
