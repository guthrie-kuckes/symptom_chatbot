from tree import process_response
from funcs import get_step, hash_phone


phone = "325629e2rfd3452"

h = hash_phone(phone)
step = get_step(h , 0)
print("Do you feel sick?")
while step != None:
    
    response = input("Response: ")
    if response == "0" or response == "1" or response == "2":
        response = eval(response)

    step = process_response(phone, response, step)
    step = get_step(h , 0)
    # print("STEP", step)