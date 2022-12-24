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
response = Label()
response.pack()

complete = False
counter = 0
counterg = 0 
group = 0
def add_custom_team():
    global counterg , response
    counterg+=1
    if counterg <= 32:
        teams.append(str(team.get()))
        level = {"team" : str(team.get()) , "strength" : int(strength.get())}
        classification.append(level)
        response.config(text="created successfuly")

    else :
        response.config(text="you created more than 32 team")

        return
# dd
tables , results = [0]*8 , [0]*8
tableLable = Label()
resultLable = Label()
tableLable.pack()
resultLable.pack()
def random_complete():
    global tables ,results, classification,complete,counter,generate,addTeamB
    complete = True
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
        tables[i] , results[i] = groups[i].results()
        tables[i] = sorted(tables[i], key=itemgetter('score'),reverse=True) 
    tableLable.config(text=str('Group : '+ str(counter%8) +'\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
    generate.destroy()
    addTeamB.destroy()



def next():
    global counter
    counter+=1
    tableLable.config(text=str('Group : '+ str(counter%8) +'\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
        
def back():
    global counter
    counter-=1
    tableLable.config(text=str('Group : '+ str(counter%8) +'\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
        


    
nextb , backb = Button(text="next",command=next),Button(text="back",command=back) 


nextb.pack()
backb.pack()

generate = Button(text="generate and view",command=random_complete)
generate.pack()

addTeamB = Button(text="append",command=add_custom_team )
addTeamB.pack()






top.mainloop()