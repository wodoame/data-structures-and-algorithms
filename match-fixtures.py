import random 

default_results = {'points':0, 'wins': 0, 'draws':0, 'losses': 0, 'GF': 0, 'GA':0, 'GD': 0}
league_table = {
'Manchester City': default_results.copy(),
'Manchester United':default_results.copy(), 
'Liverpool': default_results.copy(), 
'Chelsea': default_results.copy(), 
'Tottenham': default_results.copy(), 
'Arsenal':default_results.copy(), 
'Westham': default_results.copy(), 
'Luton Town': default_results.copy(), 
'Aston Villa': default_results.copy(),
'Burnley': default_results.copy(), 
'Sheffield': default_results.copy(), 
'Bournemouth': default_results.copy(), 
'Newcastle': default_results.copy(),
'Brighton': default_results.copy(), 
'Brentford': default_results.copy(), 
'Wolves': default_results.copy(), 
'Everton': default_results.copy(), 
'Crystal Palace': default_results.copy(), 
'Fulham': default_results.copy(), 
'Nottingham Forest':default_results.copy(),
}

individual_results = {'goals': 0}

players = {
    'Manchester City':{
        'E. Haaland':individual_results.copy(),
        'P. Foden':individual_results.copy(),
        'J. Alvarez':individual_results.copy(),
        'Rodri':individual_results.copy(),
        'De Bruyne':individual_results.copy(),
        'J. Grealish':individual_results.copy()
    },
    
    'Manchester United': {
        'Garnacho':individual_results.copy(),
        'M. Rashford':individual_results.copy(),
        'B.Fernandes':individual_results.copy(),
        'Hojlund':individual_results.copy(),
        'Mctominay':individual_results.copy(),
        'Dalot':individual_results.copy()
    },
    
    'Everton': {
     'D. Calvert-Lewin':individual_results.copy(),
     'A. Doucoure':individual_results.copy(),
     'D. Mcneil':individual_results.copy(),
     'Andre Gomes':individual_results.copy(),
     'V. Mykolenko':individual_results.copy()
     }, 
    
    'Chelsea': {
     'R. Sterling':individual_results.copy(),
     'N. Jackson':individual_results.copy(),
     'Broja':individual_results.copy(),
     'Mudryk':individual_results.copy(),
     'Enzo Fernandes':individual_results.copy(),
     'C. Palmer':individual_results.copy()
     }, 
    
    'Arsenal': {
     'B. Saka':individual_results.copy(),
     'Kai Havertz':individual_results.copy(),
     'Martinelli':individual_results.copy(),
     'Odegaard':individual_results.copy(),
     'Gabriel Jesus':individual_results.copy(),
     'Zinchenko':individual_results.copy()
     }, 
    
    'Luton Town': {
     'E. Adebayo':individual_results.copy(),
     'A. Doughty':individual_results.copy(),
     'C. Woodrow':individual_results.copy(),
     'C. Ogbene':individual_results.copy(),
     'C. Morris':individual_results.copy(),
     'J. Clark':individual_results.copy(), 
     'R. Barkley':individual_results.copy()
     }, 
    
    'Tottenham': {
     'Son':individual_results.copy(),
     'James Maddison':individual_results.copy(),
     'Johnson':individual_results.copy(),
     'Kulusevski':individual_results.copy(),
     'Hojberg':individual_results.copy()
     },
    
    'Westham': {
     'Mo Kudus':individual_results.copy(),
     'Paqueta':individual_results.copy(),
     'Benrahma':individual_results.copy(),
     'J. Bowen':individual_results.copy(),
     'Antonio':individual_results.copy()
     },
    
    'Newcastle': {'A. Gordon':individual_results.copy(), 'A. Isak':individual_results.copy(), 'C. Wilson':individual_results.copy(), 'M. Almiron':individual_results.copy(), 'Miley':individual_results.copy(), 'Bruno G.':individual_results.copy()},
    'Wolves': {'Hwang Hee Chan':individual_results.copy(), 'Cunha':individual_results.copy(), 'Sarabia':individual_results.copy(), 'Lemina':individual_results.copy(), 'Nelson Semedo':individual_results.copy()}, 
    
    'Liverpool': {
     'Mo Salah':individual_results.copy(),
     'Darwin':individual_results.copy(),
     'C. Gakpo':individual_results.copy(),
     'Luis Diaz':individual_results.copy(),
     'Gravenberch':individual_results.copy(),
     'Szoboszlai':individual_results.copy(),
     'H. Elliot':individual_results.copy(),
     'Curtis Jones':individual_results.copy()
     },
    
    'Burnley': {
    'M. Tresor':individual_results.copy(),
     'L. Foster':individual_results.copy(),
     'J. Gudmundsson':individual_results.copy(),
     'Jay Rodriguez':individual_results.copy(), 'A. Zaroury':individual_results.copy(), 'J. Bruun Larson':individual_results.copy(), 'Z. Amdouni':individual_results.copy()},
    'Aston Villa': {'M. Diaby':individual_results.copy(), 'M. Cash':individual_results.copy(), 'O. Watkins':individual_results.copy(), 'J. McGinn':individual_results.copy()},
    
    'Nottingham Forest': {
     'O. Aina':individual_results.copy(),
     'A. Elanga':individual_results.copy(),
     'T. Awoniyi':individual_results.copy(), 
     'C. Wood':individual_results.copy(),
     'C. Hudson-Odoi':individual_results.copy(),
     'D. Origi':individual_results.copy(),
      }, 
    
    'Sheffield': {
    'O. McBurnie':individual_results.copy(),
     'C. Archer':individual_results.copy(),
     'W. Osula':individual_results.copy(),
     'D.Jebbison':individual_results.copy(),
     'R. Brewster':individual_results.copy()
     }, 
    
    'Fulham': {'Adama Traore':individual_results.copy(), 'R. Jimenez':individual_results.copy(), 'Decordova-Reid':individual_results.copy(), 'Willian':individual_results.copy(), 'C. Vinicius':individual_results.copy(), 'A. Iwobi':individual_results.copy(), 'R. Muniz':individual_results.copy()}, 
    'Brentford': {'N. Maupay':individual_results.copy(), 'K. Schade':individual_results.copy(), 'S. Ghoddos':individual_results.copy(), 'B. Mbeumo':individual_results.copy(), 'Y. Wissa':individual_results.copy(), 'K. Lewis-Potter':individual_results.copy(), 'I. Toney':individual_results.copy()}, 
    'Crystal Palace': {'J. Ayew':individual_results.copy(), 'O. Edouard':individual_results.copy(), 'Mateta':individual_results.copy(), 'Eberechi Eze':individual_results.copy(), 'M. Olise':individual_results.copy()}, 
    'Brighton':{'Ansu Fati':individual_results.copy(), 'E. Ferguson':individual_results.copy(), 'D. Welbeck':individual_results.copy(), 'S. Adingra':individual_results.copy(), 'Joao Pedro':individual_results.copy(), 'Kaoru Mitoma':individual_results.copy()}, 
    'Bournemouth': {'D. Solanke':individual_results.copy(), 'L. Sinisterra':individual_results.copy(), 'K. Moore':individual_results.copy(), 'A. Semenyo':individual_results.copy(), 'J. Kluivert':individual_results.copy(), 'P. Billing':individual_results.copy()}
}

# league_table = {
#     'Manchester City': default_results.copy(), 
#     'Manchester United': default_results.copy(), 
#     'Chelsea': default_results.copy(), 
#     'PSG': default_results.copy(), 
#     'Dortmund': default_results.copy(), 
#     'Bayern Munich': default_results.copy(), 
#     'Liverpool': default_results.copy(),
#     'Barcelona': default_results.copy(), 
#     'Real Madrid': default_results.copy(), 
#     'Atletico Madrid': default_results.copy(), 
#     'Arsenal': default_results.copy(), 
#     'Inter Milan': default_results.copy(), 
#     'AC Milan': default_results.copy(), 
#     'Tottenham': default_results.copy(), 
#     'Sevilla': default_results.copy(), 
#     'Leipzig': default_results.copy(), 
#     'Napoli': default_results.copy(), 
#     'Girona': default_results.copy(), 
#     'Real Sociedad': default_results.copy(), 
#     'Newcastle': default_results.copy(),
# }

teams = list(league_table.keys())
fixture_details = []
# From ChatGpt 

def getScorers(team, goals):
    if goals == 0: 
        return  team + ': No scorers'
    team_players = players.get(team)
    scorers = random.choices(list(team_players.keys()), k=goals)
    for i, scorer in enumerate(scorers): 
        stats = team_players.get(scorer)
        # print(stats, scorer)
        prev_goals = stats.get('goals')
        stats.update({'goals': prev_goals + 1})
        if i > 0:
            result_str = f'{result_str}, {scorer}' 
        else: 
            result_str = f'{team}: {scorer}'
    return result_str 

def generate_fixtures(teams):
    fixtures = []
    # Ensure the number of teams is even
    if len(teams) % 2 != 0:
        teams.append("BYE")

    # Generate fixtures using the round-robin algorithm
    for i in range(len(teams) - 1):
        mid = len(teams) // 2
        round_fixtures = []
        
        for j in range(mid):
            match = [teams[j], teams[len(teams) - j - 1]]
            round_fixtures.append(match)
            
        fixtures.append(round_fixtures)

        # Rotate teams for the next round
        teams = [teams[0]] + [teams[-1]] + teams[1:-1]

    return fixtures

def print_fixtures(fixtures, start):
    BIG_TEAMS = ['Manchester United', 'Manchester City', 'Chelsea', 'Liverpool', 'Arsenal', 'Tottenham', 'Aston Villa']
    for i, round_fixtures in enumerate(fixtures, start=start): 
        for match in round_fixtures:
            if i >= 20:
                match = [match[1], match[0]]
            simulate_match(match, league_table)
    sortable = [[team, results] for team, results in league_table.items()]
    sortable = league_sort(sortable)
    sortable_ranks = []
    for team, team_stats  in players.items(): 
        for player, stats in team_stats.items():
            sortable_ranks.append([team, player, stats])
    
    sortable_ranks = player_sort(sortable_ranks)        

    for i, item in enumerate(sortable, start=1): 
        print(f'{i} {item[0]}: {item[1]}')
        
    print('\n\nPLAYER STATS\n\n')
    
    for i, item in enumerate(sortable_ranks, start=1): 
        print(f'{i} ({item[0]}) {item[1]}: {item[2]}')
    
                
def simulate_match(teams, league_table):
    team1 = teams[0]
    team2  = teams[1]
    team1_gf_now = random.randint(1, 5) 
    team2_gf_now = random.randint(0, 5)
    team1_scorers = getScorers(team1, team1_gf_now)
    team2_scorers = getScorers(team2, team2_gf_now)
    team1_results = league_table.get(team1)
    team2_results = league_table.get(team2)
    team1_ga_previous = team1_results.get('GA')
    team1_gf_previous = team1_results.get('GF')
    team1_gd_previous = team1_results.get('GD')
    team2_ga_previous = team2_results.get('GA')
    team2_gf_previous =  team2_results.get('GF')
    team2_gd_previous = team2_results.get('GD')
    if team1_gf_now > team2_gf_now:
        wins = team1_results.get('wins')
        points = team1_results.get('points')
        losses = team2_results.get('losses')
        team1_results.update({'wins': wins + 1, 'points':points + 3, 'GF': team1_gf_previous + team1_gf_now, 'GA': team1_ga_previous + team2_gf_now, 'GD': team1_gd_previous + (team1_gf_now - team2_gf_now)})
        team2_results.update({'losses': losses + 1, 'GF': team2_gf_previous + team2_gf_now, 'GA':team2_ga_previous + team1_gf_now, 'GD':team2_gd_previous + (team2_gf_now - team1_gf_now)})
        detail = f'{teams[0]} vs {teams[1]}  ({team1_gf_now}:{team2_gf_now})\t({team1_scorers} | {team2_scorers})'
        fixture_details.append(detail)
    elif team1_gf_now == team2_gf_now: 
        goal = team1_gf_now
        team1_draws = team1_results.get('draws')
        team1_points = team1_results.get('points')
        team1_results.update({'draws': team1_draws + 1, 'points': team1_points + 1, 'GF': team1_gf_previous + goal, 'GA': team1_ga_previous + goal})
        
        team2_draws = team2_results.get('draws')
        team2_points = team2_results.get('points')
        team2_results.update({'draws': team2_draws + 1, 'points':team2_points + 1, 'GF': team2_gf_previous + goal, 'GA': team2_ga_previous + goal})
        fixture_details.append(f'{teams[0]} vs {teams[1]}  ({goal}:{goal})\t({team1_scorers} | {team2_scorers})')
    else: 
        wins = team2_results.get('wins')
        points = team2_results.get('points')
        losses = team1_results.get('losses')
        team2_results.update({'wins': wins + 1, 'points':points + 3, 'GF': team2_gf_previous + team2_gf_now, 'GA': team2_ga_previous + team1_gf_now, 'GD': team2_gd_previous + (team2_gf_now - team1_gf_now)})
        team1_results.update({'losses': losses + 1, 'GF': team1_gf_previous + team1_gf_now, 'GA':team1_ga_previous + team2_gf_now, 'GD':team1_gd_previous + (team1_gf_now - team2_gf_now)})
        detail = f'{teams[0]} vs {teams[1]}  ({team1_gf_now}:{team2_gf_now})\t({team1_scorers} | {team2_scorers})'
        fixture_details.append(detail)
    league_table.update({team1:team1_results, team2:team2_results})
        
def league_sort(sortable):
    for i in range(len(sortable)):
        for j in range(len(sortable) - 1): 
            if sortable[j][1].get('points') < sortable[j + 1][1].get('points'): 
                sortable[j], sortable[j + 1] = sortable[j + 1], sortable[j]
            elif sortable[j][1].get('points') ==  sortable[j + 1][1].get('points'): 
                if sortable[j][1].get('GD') < sortable[j + 1][1].get('GD'):
                     sortable[j], sortable[j + 1] = sortable[j + 1], sortable[j]
    return sortable

def player_sort(sortable_ranks):
    for i in range(len(sortable_ranks)): 
        for j in range(len(sortable_ranks) - 1):
            if sortable_ranks[j][2].get('goals') < sortable_ranks[j + 1][2].get('goals'): 
                sortable_ranks[j], sortable_ranks[j + 1] = sortable_ranks[j + 1], sortable_ranks[j]
    return sortable_ranks
    

# Generate and print fixtures
fixtures = generate_fixtures(teams)
print('\n\nTABLE AFTER 19 GAMES\n\n')
print_fixtures(fixtures, 1)

print('\n\nTABLE AFTER 38 GAMES\n\n')
print_fixtures(fixtures, 20)
print('\n\nSEASON DETAILS\n\n')

for i, result in enumerate(fixture_details, start=1): 
    if i % 10 == 0 and i != len(fixture_details): 
        print(f'{result}')
        print(f'\n\nMatch week {(i//10) + 1}')
    elif i == 1: 
        print(f'\n\nMatch week {1}')
        print(f'{result}')
    else: 
        print(f'{result}')

        






