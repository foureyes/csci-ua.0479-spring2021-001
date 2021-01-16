import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate('/tmp/csci0480-007-scratch-6b18d-firebase-adminsdk-n6o7d-f2e8c58f19.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection('scooters').document()
doc_ref.set({
    'model': 'Wheelie Max',
    'retired': False,
    'acquired': datetime.datetime(2018, 5, 28),
    'manufacturer': '123 Scootz'
})
