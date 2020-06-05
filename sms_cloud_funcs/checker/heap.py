import funcs
import messages

# Simplified version of the symptom checker into a binary tree

def childNodes(i):
     return (2*i)+1, (2*i)+2

def traversed(a, i=0, d = 0):
    if i >= len(a):
        return 
    if a[i] == None:
        return
    l, r =  childNodes(i)
    traversed(a, r, d = d+1)
    print("  "*(5**d) , str(a[i]))
    traversed(a, l, d = d+1)

l0 = [
    
    funcs.isIll
]

l1 = [

    funcs.hasLifeThreatingSymptoms,
    # "Yes/Some => Have life threatning symptoms?",
    "No =>  Contact with person?"
]

l2 = [
    funcs.call911,
    "No => Have Experienced symptoms?",

    "Yes => Quarantine and dr",
    "No/Maybe => Contact with symptoms?"
]

l3 = [
    None,
    None,

    "Yes => symptoms",
    "No => symptoms",

    None,
    None,

    "Yes => Call dr",
    "No => No testing"

]

l4 = [
    funcs.race,
    # "gender",
    funcs.location
]

steps = l0+l1+l2+l3+l4
# traversed(steps)
# print(len(steps))