from heap import steps
from messages import messages
# from funcs import push_to_firebase


def process_response(phone, response, c_step):
    # checking firebase with phone hash what step the user is at
    phone_hash = hash(phone) # do a deterministic hash 
    current_step = get_step(phone_hash, c_step)
    if current_step != None:
        # take next step in the tree
        current_step, text_message = take_next_step(current_step, response, phone_hash)
        # print("Now step is", current_step)
        
        # update step to firebase 
        # push_to_firebase(phone_hash, 'step', current_step)

        # send information back to user
        send_message(phone, text_message)
        return current_step
    return None

def take_next_step(current_step, response, user):
    # now we should do:
    # print("step is", steps[current_step], current_step)
    
    nextStep =  steps[current_step](current_step, response, user)
    # print(nextStep)
    if nextStep != None:
        text_message = messages[nextStep]
        # print("Next step is ", nextStep, 'with message', text_message)

        return nextStep, text_message
    return None, None


def get_step(user, cstep):
    print("\nUser is at step", cstep)
    return cstep
def send_message(phone, m):
    print(m)


# process_response(phone, response)
# print(messages)