# Assumin 0 is yes
# 1 is a little
# 2 is no
# from tree import push_to_firebase
from google.cloud import firestore
import hashlib
from binascii import hexlify


db = firestore.Client()
collection = db.collection(u'test')


def get_step(user, cstep):
    
    snap = collection.document(user).get()
    snap = snap.to_dict()
    # print(snap)
    if snap == {} or snap ==None:
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
def getTested(current_step, response, user):
    return 15
def noTest(current_step, response, user):
    return 15


def race(current_step, response, user):
    print("race", response)
    if type(response) != int:
        response = eval(response)
    r = {
        0: 'black',
        1: 'asian',
        2: 'white',
        3: 'hispanic',
        4: 'other'
    }
    push_to_firebase(user, "race", r[response])
    return current_step+1
def gender(current_step, response, user):
    if response == 0:
        push_to_firebase(user, 'gender', 'female')
    elif response == 1:
        push_to_firebase(user, 'gender', 'male')
    else:
        push_to_firebase(user, 'gender', 'other')
    return current_step+1

def age(current_step, response, user):
    if type(response) != int:
        reponse = eval(response)
    _age = {
        0:'0-18',
        1: '19-25',
        2: '26-45',
        3: '45-65',
        4: '65-80',
        5: 'Above 80'
    }
    push_to_firebase(user, "age", _age[response])
    return current_step+1

def location(current_step, response, user):
    print("location", response)
    push_to_firebase(user, "location", response)
    return current_step+1
def have_symptoms(current_step, response, user):
    if type(response) != int:
        response = eval(response)
    s = None
    n = None
    if response <= 2:
        s = "mild"
        n= 2
    elif response <= 4:
        s = "moderate"
        n = 2
    else:
        s = "severe"
        n = 1
    print("symptoms", s)
    push_to_firebase(user, 'symptoms', s)

    return current_step*2 + n


def have_contact_with_symptoms(current_step, response, user):
    contact = None
    step = None
    if response: 
        contact = 'yes'
        step = 0
    else:
        contact = 'no'
        step = 1
    push_to_firebase(user, 'contact', contact)
    return current_step*2 + step
def hasContact(current_step,response, user):
    if not response:
        push_to_firebase(user, 'symptoms', 'yes')
        return current_step*2 +1
    else:
        push_to_firebase(user,'contact', 'yes')
        return current_step*2 + 2

def r(a,b,c):
    return 15