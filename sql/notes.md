users can post articles
articles are links

articles can have tags on them

there's voting involved, so users (that are logged in can upvote an article, only positive)


create table article (
	article_id serial,
	title varchar(255) unique not null
	user_id integer references user(user_id) on delete cascade
	primary key(article_id, title)
) 






user
====
user_id pk
username
password (hash)
salt
 |
 =
 |
 |    user id = 1, article id = 2
 |    user id = 1, article id = 7
 |
 ^
article
====
article_id pk
title
description
tag
votes
user_id fk
  V
  |
  |
  =
  |
article_tag
====
article_id fk
tag_id fk
  |
  =
  |
  |
  ^
tag
====
tag_id
name

















