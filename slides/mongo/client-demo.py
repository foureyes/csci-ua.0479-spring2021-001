
from pymongo import MongoClient
dsn = 'mongodb://localhost'
client = MongoClient(dsn)
db = client.test # database name

print('hello')
sal_freq_filter = {"$match": {"Salary Frequency": 'Hourly'}}
group_by = {"$group": {"_id": "$Agency", "count_pos": {"$sum": "$# Of Positions"}}}
order_by = {"$sort": {"count_pos": -1}}
having = {"$match": {"count_pos": {"$gt": 100}}}
result = db.jobs.aggregate([sal_freq_filter, group_by, order_by])


res = db.jobs.find({
    "Agency":"DEPT OF PARKS & RECREATION",
    "Salary Range To": {"$gt": 30000}
})


for r in res:
    print(r["Agency"], r["Business Title"])
'''
fields = {
        "id": "#Job ID", 
        "agency": "$Agency", 
        "title": "$Business Title", 
        "sal_from": "$Salary Range From",
}
projection = {"$project": fields} 
'''
#tmp = [(d['_id'], d['averagePrice']) for d in result]

