from heap import steps
from messages import messages, options
from funcs import get_step, hash_phone, push_to_firebase
import random 

def process_response(phone, response, c_step):
    # checking firebase with phone hash what step the user is at
    phone_hash = hash_phone(phone) # do a deterministic hash 
    current_step = get_step(phone_hash, c_step)
    print("step", current_step)
    if current_step != None and current_step < len(steps):
        # take next step in the tree
        # print("response", response)
        current_step, text_message = take_next_step(current_step, response, phone_hash)
        print("message :", text_message)
        
        # update step to firebase 
        push_to_firebase(phone_hash, 'step', current_step)

        # send information back to user
        # send_message(phone, text_message)
        return text_message
    else:
        print("Thank you\n\n")
        return "Thank you"

def take_next_step(current_step, response, user):
    # now we should do:
    print("step is", steps[current_step], current_step)
    
    nextStep =  steps[current_step](current_step, response, user)
    # print(nextStep, len(steps))
    if nextStep < len(steps):
        text_message = messages[nextStep]
        print('\n')

        return nextStep, text_message
    else:
        print("\n\nThank you\n\n")
        exit()