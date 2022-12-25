from tkinter import *
from worldcup.distributer import *
root = Tk()
bg = PhotoImage(file = "./qatar-2022-world-cup-logo-black-color-print-png-11668697201tgpljavrk0.png")
root.title("World Cup GUI simulation_Group 6")
root.geometry('1024x500')
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

addTeamLable = Label(text="Add Team", bg = 'white', fg = 'black')
addTeamLable.pack()
teamEntry = Entry(width=50, bg = 'white', fg = 'black')
teamEntry.pack()
x = Label(text="", bg = '#DECEC8', fg = 'black')
x.pack()
strengthLable = Label(text="Strength", bg = 'white', fg = 'black')
strengthLable.pack()
strength = Entry(width=50, bg = 'white', fg = 'black')
strength.pack()
response = Label(text='', bg = '#DECEC8')
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
        response.config(text="created successfuly", bg = 'white', fg = 'black')

    else :
        response.config(text="you created more than 32 team")
    

    return
tables , results = [0]*8 , [0]*8
tableLable = Label( bg = '#DECEC8')
resultLable = Label( bg = '#DECEC8')
tableLable.pack()
resultLable.pack()



def random_complete():
    global tables ,results, classification,complete,counter,generate,addTeamB ,nextb ,backb,team,strength
    
    complete = True
    print(classification)
    global counterg
    for i in range(counterg,32):
        teams.append("team_"+str(i) if i >= 10 else 'team_0'+str(i) )
        team = {"team" : 'team_'+str(i) if i >= 10 else 'team_0'+str(i) , "strength" : randint(1,4)}
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
        groups[i].simulate()
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
    nextStageB = Button(text='next stage' , command=next_stage, bg = 'white', fg = 'black')
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
    


nextStageB = Button(text='next stage' , command=next_stage , bg = 'white', fg = 'black')

    
nextb = Button(text="next",command=next, bg = 'white', fg = 'black')
backb = Button(text="back",command=back, bg = 'white', fg = 'black') 


addTeamB = Button(text="Add team",command=add_custom_team,width=25, bg = 'white', fg = 'black' )
addTeamB.pack()
space = Label(bg = '#DECEC8')
space.pack()
generate = Button(text="Generate and view",command=random_complete,width=30, bg = 'white', fg = 'black')
generate.pack()




mainloop()