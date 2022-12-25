from tkinter import *
from worldcup.distributer import *
import sys
top = Tk()

top.title("World Cup simulation_Group 6")
top.geometry('1024x500')
top.configure(bg = '#0A2647')

addTeamLable = Label(text="Add Team",bg = '#0A2647',fg ='white', font=('Helvetica bold', 24))
addTeamLable.pack()
teamEntry = Entry(width=50, font=('Helvetica bold', 24))
teamEntry.pack()

strengthLable = Label(text="Strength",bg = '#0A2647',fg ='white', font=('Helvetica bold', 24))
strengthLable.pack()
strength = Entry(width=50, font=('Helvetica bold', 24))
strength.pack()
response = Label(text='' , bg= '#0A2647' , fg = 'white',font=('Helvetica bold', 24))
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
        response.config(text="Created successfuly")
    else :
        response.config(text="You created more than 32 team")
    return

tables , results = [0]*8 , [0]*8
tableLable = Label(fg = 'white' , bg = '#0A2647')
resultLable = Label(fg = 'white' , bg = '#0A2647')
tableLable.pack()
resultLable.pack()

def random_complete():
    global tables ,results, classification,complete,counter,generate,addTeamB ,nextb ,backb,team,strength
    
    complete = True
    global counterg
    for i in range(counterg,32):
        teams.append("Team_"+str(i) if i >= 10 else 'team_0'+str(i) )
        team = {"team" : 'Team_'+str(i) if i >= 10 else 'Team_0'+str(i) , "strength" : randint(1,4)}
        classification.append(team)
        
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
    
    tableLable.config(text=str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
    generate.destroy()
    addTeamB.destroy()
    teamEntry.destroy()
    strength.destroy()
    addTeamLable.destroy()
    strengthLable.destroy()
    nextb.place(x=910, y=250)
    backb.place(x=20, y = 250)
    nextStageB.place(x=425 , y=430)
    response.config(text=str('Group : '+ str((counter+1)%8 if (counter+1) % 8 != 0 else '8') +'\n'+'----------\n'))

def next():
    global counter
    counter+=1
    response.config(text='Group : '+ str((counter+1)%8 if (counter+1) % 8 != 0 else '8') +'\n'+'----------\n', font=('Helvetica bold', 24))
    tableLable.config(text=str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))
        
def back():
    global counter
    counter-=1
    tableLable.config(text=str('Group : '+ str((counter+1)%8 if (counter+1) % 8 != 0 else 8) +'\n'+'----------\n')+str(print_table(tables[counter%8])))
    resultLable.config(text=str(print_result(results[counter%8])))

def exit():
    sys.exit(0)
    

def next_stage():
    global qualified , nextStageB
    if len(qualified) == 1:
        tableLable.config(text='The CHAMPION is : '+str(qualified[0]), font=('Helvetica bold', 48))
        response.config(text='---------\n| Winner |\n----------', font=('Helvetica bold', 24))
        exitb = Button(text='EXIT' , command=exit , font=('Helvetica bold', 24))
        exitb.place(x=460 , y=430)
        nextStageB.destroy()
        return
    
    if len(qualified) == 8:
        response.config(text='----------------\n| Quarter final |\n-----------------', font=('Helvetica bold', 24))
    elif len(qualified) == 4:
        response.config(text='------------\n| Semi final |\n-------------', font=('Helvetica bold', 24))
    elif len(qualified) == 2:
        response.config(text='--------\n| Final |\n--------', font=('Helvetica bold', 24))
    else :
        response.config(text='-------------\n| Round 16 |\n--------------', font=('Helvetica bold', 24))
    
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
nextStageB = Button(text='Next stage' , command=next_stage, font=('Helvetica bold', 24))

nextb = Button(text="Next",command=next, bg = 'white',font=('Helvetica bold', 24))
backb = Button(text="Back",command=back,bg = 'white', font=('Helvetica bold', 24)) 

addTeamB = Button(text="Add team",command=add_custom_team,width=25, bg = 'white',font=('Helvetica bold', 24))
addTeamB.pack()
space = Label(bg = '#0A2647')
space.pack()
generate = Button(text="Generate and view",command=random_complete,width=30, bg = 'white',font=('Helvetica bold', 24))
generate.pack()




top.mainloop()