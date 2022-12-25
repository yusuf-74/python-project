from random import randint,choice
from operator import itemgetter

teams = []
classification = []
def create_game(team1 , team2):
    score1 = randint(0,4)
    score2 = randint(0,4)
    return {'team1':team1 , 'team2':team2 , 'score1':str(score1) , 'score2':str(score2)}

def create_game_knock(team1 , team2 , day):
    score1 , score2 = 0 , 0
    while(score1 == score2):
        score1 = randint(0,4)
        score2 = randint(0,4)
    return {'match':day,'team1':team1 , 'team2':team2 , 'score1':str(score1) , 'score2':str(score2)}
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
                "winner":'  tie        '
            }
        self.result.append(result)

    def semulate(self):
        for i in range(4):
            for j in range(i+1,4):
                self.game(**create_game(self.teams[i] , self.teams[j]))
    


    def results(self):
        return [self.table , self.result]

    def qualified(self):
        self.table = sorted(self.table, key=itemgetter('score'),reverse=True) 
        return [self.table[0]['team_name'] , self.table[1]['team_name']]



def print_table(table):
    tables=""
    tables+='   team name     |       points         \n'
    tables+='-----------------------------------\n'

    for i in range(4):
        tables+= '     ' + table[i]['team_name'] + '      |' +'     ' + str(table[i]['score']) + '     ' + ('qulified\n' if i < 2 else '             \n')
    tables += '========================================\n'    
    return tables

def print_result(result):
    results = ""
    results+= '    team 1        VS     team 2       |     score     |     winner     \n'
    results+= '----------------------------------------------------------------------\n'

    for i in range(6):
        results+= '     ' + result[i]['team1'] + '      VS' \
            '     ' + str(result[i]['team2']) + '     |'+\
                '     ' + result[i]['score'] + '      |' \
                '     ' + str(result[i]['winner']) + '     \n'
    
    return results
    

class KnockOut:
    def __init__(self,numberOfTeams , teams) -> None:
        self.numberOfTeams = numberOfTeams
        self.teams = teams
        self.games = []
        self.winners = []
    
    def create_matches(self):
        for i in range(int(self.numberOfTeams/2)):
            self.games.append(create_game_knock(self.teams[i],self.teams[self.numberOfTeams-i-1],i+1))
        return self.games
    
    def qualified(self):
        for game in self.games:
            if game['score1'] > game['score2']:
                self.winners.append(game['team1'])
                game['winner'] = game['team1']
            else :
                self.winners.append(game['team2'])
                game['winner'] = game['team2']

        return self.winners
    
    def print_games(self):
        results = ""
        results+= '    match    |     team 1       |     team 2      |         score          |     winner   \n'
        results+= '------------------------------------------------------------------------------------------\n'

        for game in self.games:
            results+= '       ' + str(game['match'])      + '        |'  \
                      '    ' + str(game['team1'])      + '     VS' \
                      '    ' + str(game['team2'])      + '     |'+\
                      '       ' + str(game['score1'])+' - '+str(game['score2'])       + '      |' \
                      '    ' + str(game['winner'])      + '     \n'
            results+= '--------------------------------------------------------------------------------------\n'


        return results
        

