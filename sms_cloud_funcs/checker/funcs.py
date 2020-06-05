# Assumin 0 is yes
# 1 is a little
# 2 is no
# from tree import push_to_firebase

def push_to_firebase(user, field, data):
    step = data
    print(user ,"has", field, ":", data)

def isIll(current_step, response, user ):
    if response == 0 or response == 1:
        push_to_firebase(user, "symptoms", "mild")
        response = 1
    print("current", current_step, "response is ", response)

    
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
    r = {
        0: 'black',
        1: 'asian'
    }
    push_to_firebase(user, "race", r[response])
    return current_step+1
def location(current_step, response, user):
    push_to_firebase(user, "location", response)
    return None