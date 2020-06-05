from main import process_response
from heap import steps
from messages import messages
from funcs import get_step, hash_phone, push_to_firebase
from funcs import get_step, hash_phone
from messages import options
import random 
def run_test(request):
    try: 
        phone = str( random.randint(300000, 800000000) )

        h = hash_phone(phone)
        step = get_step(h , 0)
        print("Do you feel sick?"+options)
        while step != None:
            
            # response = input("Response: ")
            # if response == "0" or response == "1" or response == "2":
            #     response = eval(response)
            response = random.randint(0,2)

            step = process_response(phone, response, step)
            step = get_step(h , 0)
            # print("STEP", step)
    except Exception as e:
        print(e)