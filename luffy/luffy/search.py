from firebase_admin import firestore
db=firestore.client()
entrepreneurs=db.collection('Entrepreneurs').stream()
ens=[doc.to_dict() for doc in entrepreneurs]
print(ens)