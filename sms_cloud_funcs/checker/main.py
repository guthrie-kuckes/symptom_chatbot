from tree import process_response


phone = "3015256629"

step = 0
print("Do you feel sick?")
while step != None:
    # response = eval( input("Response: "))
    response = 0
    # print(response)
    step = process_response(phone, 0, step)
    # print("STEP", step)