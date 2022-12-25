from tkinter import *
from worldcup.distributer import *
top = Tk()

top.title("hommos")
top.geometry('1024x700')

addTeamLable = Label(text="Add Team")
addTeamLable.pack()
team = Entry()
team.pack()

strengthLable = Label(text="Strength")
strengthLable.pack()
strength = Entry()
strength.pack()
response = Label(text='')
response.pack()

complete = False
counter = 0
counterg = 0 
group = 0
qualified = []
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
tables , results = [0]*8 , [0]*8
tableLable = Label()
resultLable = Label()
tableLable.pack()
resultLable.pack()



def random_complete():
    global tables ,results, classification,complete,counter,generate,addTeamB ,nextb ,backb
    
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
        temp = groups[i].qualified()
        qualified.append(temp[0])
        qualified.append(temp[1])
    
    
    tableLable.config(text=str('Group : '+ str(counter%8) +'\n'+'----------\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
    generate.destroy()
    addTeamB.destroy()
    nextb.place(x=950, y=250)
    backb.place(x=20, y = 250)
    nextStageB = Button(text='next stage' , command=next_stage)
    nextStageB.place(x=440 , y=500)
    response.config(text='')




def next():
    global counter
    counter+=1
    tableLable.config(text=str('Group : '+ str(counter%8) +'\n'+'----------\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
        
def back():
    global counter
    counter-=1
    tableLable.config(text=str('Group : '+ str(counter%8) +'\n'+'----------\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
        
def next_stage():
    global qualified , nextStageB
    if len(qualified) == 1:
        tableLable.config(text='the champion is : '+str(qualified[0]))
        nextStageB.destroy()
        return
    if len(qualified) == 8:
        response.config(text='----------------\n| quarter final |\n-----------------')
    elif len(qualified) == 4:
        response.config(text='---------------\n| semi final |\n----------------')
    elif len(qualified) == 2:
        response.config(text='----------\n| final |\n----------')
    else :
        response.config(text='-------------\n| round 16 |\n--------------')
    
    stage = KnockOut(len(qualified) , qualified)
    stage.create_matches()
    qualified = stage.qualified()
    tableLable.config(text=str(stage.print_games()))
        
        
    if resultLable:
        resultLable.destroy()
    if nextb:
        nextb.destroy()
    if backb:
        backb.destroy()
    


nextStageB = Button(text='next stage' , command=next_stage)

    
nextb , backb = Button(text="next",command=next),Button(text="back",command=back) 



generate = Button(text="generate and view",command=random_complete)
generate.pack()
space = Label()
space.pack()
addTeamB = Button(text="add team",command=add_custom_team )
addTeamB.pack()






top.mainloop()