-- location
drop table if exists location cascade;
create table location (
    location_id serial primary key,
    city text,
    state text
);

-- donor
drop table if exists donor cascade;
create table donor (
    donor_id serial primary key,
    name text
);

-- donor_location
drop table if exists donor_location;
create table donor_location (
   donor_id integer references donor(donor_id),
   location_id integer references location(location_id)
);

-- donation
drop table if exists donation;
create table donation (
    donation_id text,
    date timestamptz,
    amount decimal,
    value_in_kind decimal,
    donor_id integer references donor(donor_id)
);


