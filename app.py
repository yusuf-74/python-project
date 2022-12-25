from tkinter import *
from worldcup.distributer import *
top = Tk()

top.title("Group 6")
top.geometry('1024x500')

addTeamLable = Label(text="Add Team")
addTeamLable.pack()
teamEntry = Entry(width=50)
teamEntry.pack()

strengthLable = Label(text="Strength")
strengthLable.pack()
strength = Entry(width=50)
strength.pack()
response = Label(text='')
response.pack()

complete = False
counter = 0
counterg = 0 
group = 0
qualified = []
def add_custom_team():
    global counterg , response, teamEntry,strength
    counterg+=1
    if counterg <= 32:
        teams.append(str(teamEntry.get()))
        level = {"team" : str(teamEntry.get()) , "strength" : int(strength.get())}
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
    global tables ,results, classification,complete,counter,generate,addTeamB ,nextb ,backb,team,strength
    
    complete = True
    print(classification)
    global counterg
    for i in range(counterg,32):
        teams.append("team_"+str(i) if i >= 10 else 'team_0'+str(i) )
        team = {"team" : 'teams_'+str(i) if i >= 10 else 'team_0'+str(i) , "strength" : randint(1,4)}
        classification.append(team)
        
    print(classification)


    classification = sorted(classification, key=itemgetter('strength'),reverse=True) 

    levels = [classification[0:8], classification[8:16] ,classification[16:24] ,classification[24:32]]
    groups = []
    for i in range(8):
        groups.append(Group())
        for j in range(4):
            try:
                idx = randint(0,len(levels[j])-1)
            except:
                idx = 0
            groups[i].add_team(levels[j][idx])
            del levels[j][idx]
    for i in range(8):
        groups[i].semulate()
        tables[i] , results[i] = groups[i].results()
        tables[i] = sorted(tables[i], key=itemgetter('score'),reverse=True) 
        temp = groups[i].qualified()
        qualified.append(temp[0])
        qualified.append(temp[1])
    
    
    tableLable.config(text=str('Group : '+ str((counter+1)%8 if (counter+1) % 8 != 0 else '8') +'\n'+'----------\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
    generate.destroy()
    addTeamB.destroy()
    teamEntry.destroy()
    strength.destroy()
    addTeamLable.destroy()
    strengthLable.destroy()
    nextb.place(x=950, y=250)
    backb.place(x=20, y = 250)
    nextStageB = Button(text='next stage' , command=next_stage)
    nextStageB.place(x=490 , y=410)
    response.config(text='')


def next():
    global counter
    counter+=1
    tableLable.config(text=str('Group : '+ str((counter+1)%8 if (counter+1) % 8 != 0 else '8') +'\n'+'----------\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
        
def back():
    global counter
    counter-=1
    tableLable.config(text=str('Group : '+ str((counter+1)%8 if (counter+1) % 8 != 0 else 8) +'\n'+'----------\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
        
def next_stage():
    global qualified , nextStageB
    if len(qualified) == 1:
        tableLable.config(text='The CHAMPION is : '+str(qualified[0]))
        response.config(text='---------\n| Winner |\n----------')
        nextStageB.destroy()
        return
    if len(qualified) == 8:
        response.config(text='----------------\n| quarter final |\n-----------------')
    elif len(qualified) == 4:
        response.config(text='------------\n| semi final |\n-------------')
    elif len(qualified) == 2:
        response.config(text='--------\n| final |\n--------')
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



generate = Button(text="Generate and view",command=random_complete,width=30)
generate.pack()
space = Label()
space.pack()
addTeamB = Button(text="Add team",command=add_custom_team,width=25 )
addTeamB.pack()


top.mainloop()