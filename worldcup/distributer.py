from random import randint,choice
from operator import itemgetter

teams = []
classification = []
def create_game(team1 , team2):
    score1 = randint(0,4)
    score2 = randint(0,4)
    return {'team1':team1 , 'team2':team2 , 'score1':str(score1) , 'score2':str(score2)}

class Group:
    def __init__(self):
        self.table = []
        self.teams = []
        self.games = []
        self.result = []    
    
    def add_team(self,team):
        self.teams.append(team)
        self.table.append({"team_name":team['team'] , "score" : 0})
    
    def game(self,team1,team2,score1,score2):
        if eval(score1)> eval(score2):
            for team in self.table:
                if team['team_name'] == team1['team']:
                    team['score']+=3
            result = {
                "team1":team1['team'],
                "team2":team2['team'],
                "score" : score1 + ' - ' + score2,
                "winner":team1['team']
            }
        elif eval(score1) < eval(score2):
            for team in self.table:
                if team['team_name'] == team2['team']:
                    team['score']+=3
            result = {
                "team1":team1['team'] ,
                "team2":team2['team'],
                "score" : score1 + ' - ' + score2,
                "winner":team2['team']
            }
        else :
            for team in self.table:
                if team['team_name'] == team1['team'] or team['team_name'] == team2['team'] :
                    team['score']+=1
            result = {
                "team1":team1['team'],
                "team2":team2['team'],
                "score" : score1 + ' - ' + score2,
                "winner":'tie'
            }
        self.result.append(result)

    def semulate(self):
        for i in range(4):
            for j in range(i+1,4):
                self.game(**create_game(self.teams[i] , self.teams[j]))
    


    def results(self):
        return [self.table , self.result]



def print_table(table):
    tables=""
    tables+='   team name     |     points     \n'
    tables+='-----------------------------------\n'

    for i in range(4):
        tables+= '     ' + table[i]['team_name'] + '      |' +'     ' + str(table[i]['score']) + '     ' + ('qulified\n' if i < 2 else '\n')
    
    return tables

def print_result(result):
    results = ""
    results+= '     team 1       |     team 2      |  score          |     winner   \n'
    results+= '----------------------------------------------------------------------\n'

    for i in range(6):
        results+= '     ' + result[i]['team1'] + '      |' \
            '     ' + str(result[i]['team2']) + '     |'+\
                '     ' + result[i]['score'] + '      |' \
                '     ' + str(result[i]['winner']) + '     \n'
    results += '============================================================\n'
    return results
    