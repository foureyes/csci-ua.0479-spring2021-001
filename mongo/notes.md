json
====

* data interchange format
	* xml
	* yml
 	* rdf
* python dictionary literal {"k": val, "k2": val2....}
* in JavaScript {"k1": v1....}
* JSON takes its syntax from JavaScript's object literal notation
* keys must be double quoted!!!!
* values:
	* numbers
	* strings
	* arrays
	* other json objects / documents
* if we have one json doc in another json doc.... that's called an "embedded doc"
{
	"child": {"foo": [
		{},
		{}
	]}
}


mongodb:

instance of mongodb
databases
collections
documents
key-value pairs

find
=====

`db.collectionname.find(query, projection)`

find will return a cursor:

* call `next`
* or... if you don't assign to var
* then iteration over cursor is automatic and all objs are printed
* once you've exhausted cursor, you can't use it anymore

arguments

* `query` - will match on exactly key and value
	* multiple key and val... will be and
* `projections` - doc that specifies which keys/props appear
	* id is always present (so you have to suppress it explicitly)
	* `{k: 1}` <--- appear
	* `{_id: 0}` <--- suppress
	* the column list in select
* `sort`.... accepts object as arg:
	* keys as key names... 
		* 1 for ascending
		* -1 for descending
		* you can have multiple k/v pairs
* `count`
* `pretty`

## operators

allows more sophisticated query objects

prefixed with $

* $gt for greater than 
* $gte
* $in and $nin
* $or and $and



## comparison


`{k: {$op: v}}`
`{lives: {$gte: 6}}`

* same thing: key first as actually key
* but val is an object containing op


## $or

`{$or: [query_obj1, query_obj2]}`

* for $or.... there's no implicit version like and
* for and... there is an explicit $and
* you have to use explicit and for multiple ors joined


## findOne


## limit



## update

`db.collection.update(query, update, options)`

* query is same as find
	* if you want to match by ObjectId: ObjectID('whatever id is')
* `update`: new document, $set or $push
* options: set whether it will upsert.... (if it doesn't exist, then insert)
	* multi.... allow updating of multiple docs
	* bunch of others

{"author.first": "william"}
{
	title: 'neuromance',
	published: 1990,
	author: {
		first: 'william',	
		last: 'gibson',	
	}

}
{
	title: 'pattern recognition',
	published: 1990,
	author: {
		first: 'william',	
		last: 'gibson',	
	}

}










































db.books.aggregate( [{$group : { _id: "$YEAR_WRITTEN", books: {$push: "$TITLE"} }}])


db design / data modeling
=====


books
{
	title: 'children of dune',
	published: 'frank herbert'
}

authors
{
	name: 'frank herbert'
}

{
	name: 'frank herbert'
	books: [{title: 'children of dune'}, {title: 'dune'}]
}
{
	name: 'frank herbert'
	books: [123, 456]
}


1. embed docs
2. relate docs








