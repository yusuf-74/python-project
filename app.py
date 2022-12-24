from tkinter import *
from worldcup.distributer import *
top = Tk()

top.title("hommos")
top.minsize(1024,1024)

addTeamLable = Label(text="Add Team")
addTeamLable.pack()
team = Entry()
team.pack()

strengthLable = Label(text="Strength")
strengthLable.pack()
strength = Entry()
strength.pack()

counter = 0

def add_custom_team():
    global counter
    counter+=1
    if counter <= 32:
        teams.append(str(team.get()))
        level = {"team" : str(team.get()) , "strength" : int(strength.get())}
        classification.append(level)
        response = Label(text="created successfuly")

        response.pack()
    else :
        response = Label(text="you created more than 32 team")

        response.pack()
    return

def random_complete():

    global classification
    for i in range(32-len(teams)):
        teams.append("team_"+str(i))

    for i in range(32-len(classification)):
        team = {"team" : teams[i] , "strength" : randint(1,4)}
        classification.append(team)

    classification = sorted(classification, key=itemgetter('strength'),reverse=True) 

    levels = [classification[0:8], classification[8:16] ,classification[16:24] ,classification[24:32]]
    groups = []
    for i in range(8):
        groups.append(Group())
        for j in range(4):
            idx = randint(0,len(levels[j])-1)
            groups[i].add_team(levels[j][idx])
            del levels[j][idx]
    for i in range(8):
        groups[i].semulate()
        table , result = groups[i].results()
        table = sorted(table, key=itemgetter('score'),reverse=True) 
        tableLable = Label(text=str(print_table(table)))
        tableLable.pack()
        resultLable = Label(text=str(print_result(result)))
        resultLable.pack()

    
        


    


generate = Button(text="generate and view",command=random_complete )
generate.pack()

addTeamB = Button(text="append",command=add_custom_team )
addTeamB.pack()






top.mainloop()