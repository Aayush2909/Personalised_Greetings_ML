#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import datetime
import pandas as pd

f = open("E:/Ml Project/Information.log","a+")

print("Please Greet the system 'Alex' in correct English! He will not respond to improper sentence. <3")

bot = ChatBot('Bot',
    logic_adapter= 
    [
        'chatterbot.logic.BestMatch',
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",

    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
)
	
trainer = ListTrainer(bot)

df = pd.read_csv('E:/Ml Project/gender_refine-csv.csv')

print('Alex : Hey, there! Who are you?')
x = datetime.datetime.now().strftime("%B %d, %Y - %I:%M %p")
f.write(x + " Alex : Hey, there! Who are you?")
f.write("\n")

urName = input('You : I am ')
x = datetime.datetime.now().strftime("%B %d, %Y - %I:%M %p")
f.write(x + " " + urName + ": I am " + urName)
f.write("\n")

if sum(df["name"].astype("str").str.contains(urName)) > 0:
    new = df[df["name"]==urName]
    if new.iloc[0]['gender'] == 1 :
        gen = 'M'
    else:
        gen = 'F'
else:
    print('Alex : Mr. ' + urName + ' or Mrs. '+ urName + '?')
    msg = input('You : ')
    if msg.split()[0] == 'Mr.' :
        df_new = pd.DataFrame({"name": [urName], "gender": 1, "score": 1.000000})
        df.append(df_new, sort=True)
        gen = 'M'
    else:
        df_new = pd.DataFrame({"name": [urName], "gender": 0, "score": 1.000000})
        df.append(df_new, sort=True)
        gen = 'F'
        
if gen == 'M':
    data = open('E:/Ml Project/greet_m.yml', 'r').readlines()
    trainer.train(data)
else:
    data = open('E:/Ml Project/greet_f.yml', 'r').readlines()
    trainer.train(data)
    

while True:
    try:
        msg = input('You : ')
        x = datetime.datetime.now().strftime("%B %d, %Y - %I:%M %p")
        f.write(x + " " + urName + ": " + msg)
        f.write("\n")
    except KeyboardInterrupt:
        print ('Alex : Invalid Input... Aborting!!')
        x = datetime.datetime.now().strftime("%B %d, %Y - %I:%M %p")
        f.write(x + " Alex : Invalid Input... Aborting!!")
        f.write("\n")
        break
        
    if msg.strip() == 'Bye' or msg.strip() == 'bye' :
        print('Alex : Bye Bye! Have a good day!! :-)')
        x = datetime.datetime.now().strftime("%B %d, %Y - %I:%M %p")
        f.write(x + " Alex : Bye Bye! Have a good day!! :-)")
        f.write("\n")
        break
    if msg.strip() != 'bye' or msg.strip() != 'Bye'  :
        reply = bot.get_response(msg)
        if reply.confidence>0.05:
            print('Alex : ',reply)
            x = datetime.datetime.now().strftime("%B %d, %Y - %I:%M %p")
            f.write(x + " Alex : ")
            f.write(str(reply))
            f.write("\n")
        elif reply.confidence<=0.05 :
            print("Alex : Sorry! Can't figure out wat'ch ya tryin' to say!!!")
            x = datetime.datetime.now().strftime("%B %d, %Y - %I:%M %p")
            f.write(x + " Alex : Sorry! Can't figure out wat'ch ya tryin' to say!!!")
            f.write("\n")

df.to_csv('E:/Ml Project/gender_refine-csv.csv') 
            
f.write("\n")
f.write("--------------------------------------------------------------------------------------------------------------------------------------------------")
f.write("\n")


# In[ ]:





# In[ ]:




