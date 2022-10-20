quiz ={
    "question 1":{
        "question" :"How many sides makes up an octagon?\n(a) 10\n(b) 20\n(c) 15\n(d) 5\n\n",
        "answer": "a"
    },
    "question 2":{
        "question" :"What are two things you can never eat for breakfast?\n(a) Lunch and Dinner\n(b) Bread\n(c) Ice-cream\n(d) People\n\n",
        "answer": "a"
    },
    "question 3":{
        "question" :"What is always coming but never arrives?\n(a) Today\n(b) One-day\n(c) Someday\n(d) Tomorrow\n\n",
        "answer": "d"
    },
    "question 4":{
        "question" :"What gets wetter the more it dries?\n(a) Sand\n(b) A towel\n(c) Ocean\n(d) Clothes\n\n",
        "answer": "b"
    },
    "question 5":{
        "question" :"What can be broken but never held?\n(a) Baby\n(b) Heart\n(c) Promise\n(d) Life\n\n",
        "answer": "c"
    },
    "question 6":{
        "question" :"What word is spelled incorrectly in every single dictionary?\n(a) Incorrectly\n(b) Wrong\n(c) Right\n(d) Try\n\n",
        "answer": "a"
    },
    "question 7":{
        "question" :"What is it that lives if it is fed, and dies if you give it a drink?\n(a) Snow\n(b) Fire\n(c) Water\n(d) Sun\n\n",
        "answer": "b"
    },
    "question 8":{
        "question" :"What never asks a question but gets answered all the time?\n(a) Cellphone\n(b) Questions\n(c) Hello\n(d) Words\n\n",
        "answer": "a"
    },
    "question 9":{
        "question" :"What goes up but never ever comes down?\n(a) Age\n(b) Ballon\n(c) Bullet\n(d) Rocket\n\n",
        "answer": "a"
    },
    "question 10":{
        "question" :"What can one catch that is not thrown?\n(a) A cold\n(b) Epilepsy\n(c) Disk\n(d) Feelings\n\n",
        "answer": "a"
    },

}
score = 0
for k,v in quiz.items():
    print(v["question"])
    response = input("Enter your answer: ")
    if response.lower() == v["answer"]:
        score += 1

print(f'Your total score is {score}/{len(quiz)}')
