from heap import steps
from messages import messages
from funcs import get_step, hash_phone, push_to_firebase


def process_response(phone, response, c_step):
    # checking firebase with phone hash what step the user is at
    phone_hash = hash_phone(phone) # do a deterministic hash 
    current_step = get_step(phone_hash, c_step)
    if current_step != None:
        # take next step in the tree
        print("response", response)
        current_step, text_message = take_next_step(current_step, response, phone_hash)

        
        # update step to firebase 
        push_to_firebase(phone_hash, 'step', current_step)

        # send information back to user
        send_message(phone, text_message)
        return current_step
    return None

def take_next_step(current_step, response, user):
    # now we should do:
    print("step is", steps[current_step], current_step)
    
    nextStep =  steps[current_step](current_step, response, user)
    if nextStep != None:
        text_message = messages[nextStep]

        return nextStep, text_message
    return None, None



def send_message(phone, m):
    print(m)


# print(messages)