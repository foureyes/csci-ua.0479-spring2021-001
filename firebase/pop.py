import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import datetime
import random

cred = credentials.Certificate('../../firebase/csci0480-007-scratch-firebase-adminsdk-y5bsv-2f4819f1b0.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

'''
doc_ref = db.collection('scooters').document()
doc_ref.set({
    'model': 'Wheelie Max',
    'retired': False,
    'acquired': datetime.datetime(2018, 5, 28),
    'manufacturer': '123 Scootz'
})
'''

models = [
    {'manufacturer': 'Rocket Inc', 'name': 'Speedter X1'}, 
    {'manufacturer': 'Rocket Inc', 'name': 'Lightning Mark III'}, 
    {'manufacturer': '123 Scootz', 'name': 'Wheelie Max' },
    {'manufacturer': 'Super Fast Co', 'name': 'SFS Pro' },
    {'manufacturer': 'Super Fast Co', 'name': 'SFS Standard' },
    {'manufacturer': 'Super Fast Co', 'name': 'SFS Nomad' }
]

for i in range(25):
    model = random.choice(models)
    doc_ref = db.collection('scooters').document()
    doc_ref.set({
        'manufacturer': model["manufacturer"],
        'retired': random.choice([True, False]),
        'acquired': datetime.datetime(random.randint(2014, 2018), random.randint(1, 12), random.randint(1, 28)),
        'model': model["name"]
    })


