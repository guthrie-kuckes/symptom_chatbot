# Assumin 0 is yes
# 1 is a little
# 2 is no
# from tree import push_to_firebase
from google.cloud import firestore
import hashlib
from binascii import hexlify


db = firestore.Client()
collection = db.collection(u'test2')


def get_step(user, cstep):
    
    snap = collection.document(user).get()
    snap = snap.to_dict()
    # print(snap)
    if snap == {} or snap ==None or snap['step'] == 'None':
        push_to_firebase(user, "step", 0)
        return 0
    # print("\nUser is at step",snap['step'] )
    return int(snap['step'])
    
def hash_phone(phone):
    m = hashlib.sha256()
    m.update(phone.encode())
    h = hexlify( m.digest()).decode()
    return h

def push_to_firebase(user, field, data):
    # print("data ", data)
    doc_ref = collection.document(u'{}'.format(user))
    doc_ref.set({
        u'{}'.format(field): u'{}'.format(data)
    }, merge=True)
    print(u'{}'.format(field), ":", u'{}'.format(data))


def isIll(current_step, response, user):
    if response == 0 or response == 1:
        push_to_firebase(user, "symptoms", "mild")
        response = 1
    # print("current", current_step, "response is ", response)

    return 2*current_step + response


def hasLifeThreatingSymptoms(current_step, response, user):
    # print("life threat")
    if response == 0 or response == 1:
        push_to_firebase(user, "symptoms", "severe")
        response = 1
    # print("response is ", response)
    # push_to_firebase(user, "symptoms", "severe")
    return 2*current_step + response


def call911(current_step, response, user):
    # print("returning none")
    return 15


def callDoctor(current_step, response, user):
    return 15


def race(current_step, response, user):
    print("race", response)
    r = {
        0: 'black',
        1: 'asian'
    }
    push_to_firebase(user, "race", r[response])
    return current_step+1


def location(current_step, response, user):
    print("location", location)
    push_to_firebase(user, "location", response)
    return None
