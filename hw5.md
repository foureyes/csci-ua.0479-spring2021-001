
referrals: one to many

* one being the person doing the referring
* many... person being referred
* if you made different assumptions, plz add it in the notes

implementing referrals

have a foreign to itself: one to many

* self join

introduce a second table, with foreign keys (both to person): many-many

categories of notes: "malfunction", "broken", "other"

1. create a staging table w/ very loose constraints (types are loose, lots of things are text, etc.)
2. import your data
3. create your normalized data model (all of your other tables)
4. begin inserting into them
	insert into ...
	subquery
5. focus on getting the subquery right:
	* resulting query set should match columns in new table
	* when it does, add it as a subq to insert








