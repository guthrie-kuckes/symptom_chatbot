options = "\n0: Yes\n1: Somewhat/Don't Know\n2: No"
prompt = "\n\nAre you willing to share information for research purposes? It cannot be linked to you.\n0: yes, 1: no"
l0 = [
  
    "Do you feel sick?"
]

l1 = [
    "Do you have any life threatning symptoms?"+options,
    "Have you had contact with person diagnosed with COVID-19?"+options
]

l2 = [
    "Please call 911"+prompt,
    "In the past two weeks, how many of the following symptoms have you experienced?\nCough, Shortness of breath or difficulty breathing, chest feels tight when you breathe, gasping for air, hard to talk, Pain or pressure in chest, Fever, chills,New loss of taste or smell, dizziness , confusion, lightheadedness, Muscle pain, Sore throat, Nausea, vomiting, or diarrhea, tirednesss",

    "Please self-quarantine and call your doctor."+prompt,
    "Have you had contact with anyone that has experience the following symptoms?\nCough, fever, chills, or chest pain"
]

l3 = [
    prompt,
    prompt,

    "Get Tested"+prompt,
    "No testing needed"+prompt,

    prompt,
    prompt,

    "Call Dr"+prompt,
    "Do testing"+prompt

]

l4 = [
    # "We will now ask you to provide other info. Is this okay?",
    "What is your race?\n0: black\n1: asian\n2: white\n3: hispanic\n4: other",
    "What is your gender?\n0: female\n1: male\n2: other",
    "What is your age?\n0: 0-18" +"\n1: 19-25" +"\n2: 26-45" +"\n3: 45-65" +"\n4: 65-80" +"\n5: Above 80",
    "Please type in your five digit zip code"
    # ""
]

messages = l0+l1+l2+l3+l4