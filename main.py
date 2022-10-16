# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import pandas as pd
import numpy as np
# from urllib2 import Request, urlopen

import requests
import pickle
import itertools
import json
from itertools import chain
from io import StringIO
import ast
import datetime

# from tqdm.notebook import tqdm, trange
from tqdm import tqdm
import time

# from flask import Flask

st.title('TRCWIHP 2022/2023')

from pandas.io.json import json_normalize

with st.spinner("Please wait, loading updated stats - should not take more than 30 seconds - all stats are live"):
    BrettTeam = pd.DataFrame(np.array(
        [['Steven Stamkos', 'Tampa Bay Lightning', '141', "F"],
         ['Nikita Kucherov', 'Tampa Bay Lightning', '113', "F"],
         ['Brayden Point', 'Tampa Bay Lightning', '73', "F"],
         ['Alex DeBrincat', 'Ottawa Senators', '57', "F"],
         ['William Nylander', 'Toronto Maple Leafs', '37', "F"],
         ['Matthew Tkachuk', 'Florida Panthers', '49', "F"],
         ['Victor Hedman', 'Tampa Bay Lightning', '137', "D"],
         ['Noah Hanifin', 'Calgary Flames', '32', "D"],
         ['Jaccob Slavin', 'Carolina Hurricanes', '51', "D"],
         ['Noah Dobson', 'New York Islanders', '33', "D"],
         ['Jacob Markstrom', 'Calgary Flames', '110', "G"],
         ['Frederik Andersen', 'Carolina Hurricanes', '70', "G"]]))

    BrettTeam.columns = ["Player", "Team", "Bid", "Position"]
    BrettTeam['Competitor'] = "Brett"
    BrettTeam['SpecialTeam'] = 'Tampa Bay Lightning'

    ColinTeam = pd.DataFrame(np.array(
        [['Nathan MacKinnon', 'Colorado Avalanche', '167', "F"],
         ['Chris Kreider', 'New York Rangers', '147', "F"],
         ['Aleksander Barkov', 'Florida Panthers', '149', "F"],
         ['J.T. Miller', 'Vancouver Canucks', '88', "F"],
         ['Sam Reinhart', 'Florida Panthers', '78', "F"],
         ['David Pastrnak', 'Boston Bruins', '48', "F"],
         ['Tyson Barrie', 'Edmonton Oilers', '36', "D"],
         ['Devon Toews', 'Colorado Avalanche', '49', "D"],
         ['Shea Theodore', 'Vegas Golden Knights', '1', "D"],
         ['Gustav Forsling', 'Florida Panthers', '1', "D"],
         ['Sergei Bobrovsky', 'Florida Panthers', '119', "G"],
         ['Andrei Vasilevskiy', 'Tampa Bay Lightning', '117', "G"]]))

    ColinTeam.columns = ["Player", "Team", "Bid", "Position"]
    ColinTeam['Competitor'] = "Colin"
    ColinTeam['SpecialTeam'] = 'Florida Panthers'

    HarveyTeam = pd.DataFrame(np.array(
        [['Connor McDavid', 'Edmonton Oilers', 221, "F"],
         ['Johnny Gaudreau', 'Columbus Blue Jackets', 201, "F"],
         ['Elias Lindholm', 'Calgary Flames', '189', "F"],
         ['Kyle Connor', 'Winnipeg Jets', '159', "F"],
         ['Joe Pavelski', 'Dallas Stars', '11', "F"],
         ['Robert Thomas', 'St. Louis Blues', '1', "F"],
         ['Zach Werensky', 'Columbus Blue Jackets', '1', "D"],
         ['Nate Schmidt', 'Winnipeg Jets', '1', "D"],
         ['Justin Faulk', 'St. Louis Blues', '1', "D"],
         ['Colton Pareyko', 'St. Louis Blues', '1', "D"],
         ['Igor Shesterkin', 'New York Rangers', '212', "G"],
         ['Juuse Saros', 'Nashville Predators', '1', "G"]]))

    HarveyTeam.columns = ["Player", "Team", "Bid", "Position"]
    HarveyTeam['Competitor'] = "Harvey"
    HarveyTeam['SpecialTeam'] = 'St. Louis Blues'

    MalcolmTeam = pd.DataFrame(np.array(
        [['Auston Matthews', 'Toronto Maple Leafs', '191', 'F'],
         ['Mitchell Marner', 'Toronto Maple Leafs', '172', 'F'],
         ['Artemi Panarin', 'New York Rangers', '141', 'F'],
         ['Elias Pettersson', 'Vancouver Canucks', '79', 'F'],
         ['Sidney Crosby', 'Pittsburgh Penguins', '73', 'F'],
         ['John Tavares', 'Toronto Maple Leafs', '40', 'F'],
         ['Shayne Gostisbehere', 'Arizona Coyotes', '59', 'D'],
         ['Aaron Ekblad', 'Florida Panthers', '82', 'D'],
         ['Morgan Rielly', 'Toronto Maple Leafs', '79', 'D'],
         ['Cam Fowler', 'Anaheim Ducks', '22', 'D'],
         ['Alexander Nedeljkovic', 'Detroit Red Wings', '50', 'G'],
         ['Connor Hellebuyck', 'Winnipeg Jets', '12', 'G']]))

    MalcolmTeam.columns = ["Player", "Team", "Bid", "Position"]
    MalcolmTeam['Competitor'] = "Malcolm"
    MalcolmTeam['SpecialTeam'] = 'New York Rangers'

    MattTeam = pd.DataFrame(np.array(
        [['Leon Draisaitl', 'Edmonton Oilers', '200', 'F'],
         ['Alex Ovechkin', 'Washington Capitals', '153', 'F'],
         ['Mika Zibanejad', 'New York Rangers', '101', 'F'],
         ['Filip Forsberg', 'Nashville Predators', '34', 'F'],
         ['Jason Robertson', 'Dallas Stars', '31', 'F'],
         ['Matt Duchene', 'Nashville Predators', '15', 'F'],
         ['Adam Fox', 'New York Rangers', '150', 'D'],
         ['Kris Letang', 'Pittsburgh Penguins', '10', 'D'],
         ['Jared Spurgeon', 'Minnesota Wild', '13', 'D'],
         ['Quinn Hughes', 'Vancouver Canucks', '9', 'D'],
         ['Darcy Kuemper', 'Washington Capitals', '127', 'G'],
         ['Jack Campbell', 'Edmonton Oilers', '157', 'G']]))

    MattTeam.columns = ["Player", "Team", "Bid", "Position"]
    MattTeam['Competitor'] = "Matt"
    MattTeam['SpecialTeam'] = 'Edmonton Oilers'

    NormTeam = pd.DataFrame(np.array(
        [['Jonathan Huberdeau', 'Calgary Flames', '120', 'F'],
         ['Kirill Kaprizov', 'Minnesota Wild', '160', 'F'],
         ['Sebastian Aho', 'Carolina Hurricanes', '13', 'F'],
         ['Mark Scheifele', 'Winnipeg Jets', '21', 'F'],
         ['Jack Hughes', 'New Jersey Devils', '13', 'F'],
         ['Patrick Kane', 'Chicago Blackhawks', '10', 'F'],
         ['Cale Makar', 'Colorado Avalanche', '190', 'D'],
         ['Roman Josi', 'Nashville Predators', '163', 'D'],
         ['Rasmus Andersson', 'Calgary Flames', '111', 'D'],
         ['John Carlson', 'Washington Capitals', '128', 'D'],
         ['Ilya Sorokin', 'New York Islanders', '13', 'G'],
         ['Thatcher Demko', 'Vancouver Canucks', '10', 'G']]))

    NormTeam.columns = ["Player", "Team", "Bid", "Position"]
    NormTeam['Competitor'] = "Norm"
    NormTeam['SpecialTeam'] = 'Calgary Flames'

    Pool = pd.concat([BrettTeam, ColinTeam, HarveyTeam, MalcolmTeam, MattTeam, NormTeam])
    SkaterPool = Pool[Pool['Position'].isin(['F', 'D'])]
    GoaliePool = Pool[Pool['Position'].isin(['G'])]

    ## Collect Information about Each Team

    Teams = requests.get(url='https://statsapi.web.nhl.com/api/v1/teams')
    Teams = Teams.json()
    Teams = pd.concat([pd.DataFrame(Teams['teams'])['id'],
                       pd.DataFrame(Teams['teams'])['locationName'],
                       pd.DataFrame(Teams['teams'])['teamName'],
                       pd.DataFrame(Teams['teams'])['name'],
                       pd.DataFrame(Teams['teams'])['abbreviation'],
                       pd.DataFrame(Teams['teams'])['link'],
                       ], axis=1)

    FullRoster = pd.DataFrame()

    intCounter = 0
    for teamLink in tqdm(Teams['link']):
        SourceData = pd.DataFrame.from_dict(requests.get(url='https://statsapi.web.nhl.com' + teamLink + '/roster').json())[
            'roster'].to_dict()
        for Player in SourceData:
            Person = SourceData[Player]['person']
            Position = SourceData[Player]['position']

            CurrentPlayer = StringIO("""ID;FullName;Link;PosCode;PosName;PosType;PosAbbreviation;Team
            """ +
                                     str(Person['id']) + ";" +
                                     Person['fullName'] + ";" +
                                     Person['link'] + ";" +
                                     Position['code'] + ";" +
                                     Position['name'] + ";" +
                                     Position['type'] + ";" +
                                     Position['abbreviation'] + ";" +
                                     Teams['name'][intCounter])
            CurrentPlayer = pd.read_csv(CurrentPlayer, sep=";")
            FullRoster = pd.concat([FullRoster, CurrentPlayer], ignore_index=True)
        intCounter += 1

    PoolRoster = FullRoster[FullRoster['FullName'].isin(Pool['Player'])]
    PoolRoster = PoolRoster.reset_index(drop=True)

    PlayerDetails = pd.DataFrame()

    intCounter = 0
    for playerLink in tqdm(PoolRoster['Link']):
        SourceData = \
            pd.DataFrame.from_dict(requests.get(url='https://statsapi.web.nhl.com' + playerLink).json()).to_dict()[
                'people'][0]

        try:
            primaryNumber = str(SourceData['primaryNumber'])
        except:
            primaryNumber = "0"
        try:
            birthStateProvince = SourceData['birthStateProvince']
        except:
            birthStateProvince = "NA"
        try:
            birthCity = str(SourceData['birthCity'])
        except:
            birthCity = "NA"
        try:
            birthCountry = str(SourceData['birthCounty'])
        except:
            birthCountry = "NA"
        try:
            weight = str(SourceData['weight'])
        except:
            weight = "NA"
        try:
            height = str(SourceData['height'])
        except:
            height = "NA"
        try:
            birthCountry = str(SourceData['birthCounty'])
        except:
            birthCountry = "NA"
        try:
            shootsCatches = str(SourceData['shootsCatches'])
        except:
            shootsCatches = "NA"

        CurrentPlayer = StringIO("""ID;Position;FullName;Link;FirstName;LastName;PrimaryNumber;BirthDate;CurrentAge;BirthCity;BirthProvState;BirthCountry;Nationality;Height;Weight;Active;AlternateCaptain;Captain;Rookie;ShootsCatches;RosterStatus
        """ +
                                 str(SourceData['id']) + ";" +
                                 PoolRoster['PosAbbreviation'][intCounter] + ";" +
                                 SourceData['fullName'] + ";" +
                                 SourceData['link'] + ";" +
                                 SourceData['firstName'] + ";" +
                                 SourceData['lastName'] + ";" +
                                 primaryNumber + ";" +
                                 SourceData['birthDate'] + ";" +
                                 str(SourceData['currentAge']) + ";" +
                                 birthCity + ";" +
                                 birthStateProvince + ";" +
                                 birthCountry + ";" +
                                 SourceData['nationality'] + ";" +
                                 height + ";" +
                                 weight + ";" +
                                 str(SourceData['active']) + ";" +
                                 str(SourceData['alternateCaptain']) + ";" +
                                 str(SourceData['captain']) + ";" +
                                 str(SourceData['rookie']) + ";" +
                                 shootsCatches + ";" +
                                 SourceData['rosterStatus'])

        CurrentPlayer = pd.read_csv(CurrentPlayer, sep=";")
        PlayerDetails = pd.concat([PlayerDetails, CurrentPlayer], ignore_index=True)

        intCounter += 1

        GoalieDetails = PlayerDetails.loc[PlayerDetails['Position'] == 'G']
        SkaterDetails = PlayerDetails.loc[PlayerDetails['Position'] != 'G']

        GoalieDetails = GoalieDetails.reset_index()
        SkaterDetails = SkaterDetails.reset_index()

        GoalieRoster = PoolRoster.loc[PoolRoster['PosAbbreviation'] == 'G']
        SkaterRoster = PoolRoster.loc[PoolRoster['PosAbbreviation'] != 'G']

        SkaterRoster = SkaterRoster.reset_index()
        GoalieRoster = GoalieRoster.reset_index()

    Season = str(20222023)

    SkaterStatistics = pd.DataFrame()

    intCounter = 0
    for PlayerLink in tqdm(SkaterDetails['Link']):
        SourceData = pd.DataFrame.from_dict(requests.get(
            url="https://statsapi.web.nhl.com" + PlayerLink + "/stats?stats=statsSingleSeason&season=" + Season).json()).to_dict()[
            'stats'][0]['splits']
        try:
            SD = pd.DataFrame.from_dict(SourceData)['stat']
            SD = SD.to_dict()[0]
            CurrentPlayer = StringIO("""ID;Position;FullName;Team;TOI;A;G;P;PIM;Shots;Games;Hits;PPG;PPP;PPTOI;EVTOI;PIM2;FaceOffPCT;ShtPercent;GWG;OTG;SHG;SHP;SHTOI;Blocks;PlusMinus;Pts;Shifts;TOIperGame;EVTOIperGame;SHTOIperGame;PPTOIperGame
            """ +
                                     str(SkaterRoster['ID'][intCounter]) + ";" +
                                     SkaterRoster['PosAbbreviation'][intCounter] + ";" +
                                     SkaterRoster['FullName'][intCounter] + ";" +
                                     SkaterRoster['Team'][intCounter] + ";" +
                                     str(SD['timeOnIce']) + ";" +
                                     str(SD['assists']) + ";" +
                                     str(SD['goals']) + ";" +
                                     str(SD['points']) + ";" +
                                     str(SD['pim']) + ";" +
                                     str(SD['shots']) + ";" +
                                     str(SD['games']) + ";" +
                                     str(SD['hits']) + ";" +
                                     str(SD['powerPlayGoals']) + ";" +
                                     str(SD['powerPlayPoints']) + ";" +
                                     str(SD['powerPlayTimeOnIce']) + ";" +
                                     str(SD['evenTimeOnIce']) + ";" +
                                     str(SD['penaltyMinutes']) + ";" +
                                     str(SD['faceOffPct']) + ";" +
                                     str(SD['shotPct']) + ";" +
                                     str(SD['gameWinningGoals']) + ";" +
                                     str(SD['overTimeGoals']) + ";" +
                                     str(SD['shortHandedGoals']) + ";" +
                                     str(SD['shortHandedPoints']) + ";" +
                                     str(SD['shortHandedTimeOnIce']) + ";" +
                                     str(SD['blocked']) + ";" +
                                     str(SD['plusMinus']) + ";" +
                                     str(SD['points']) + ";" +
                                     str(SD['shifts']) + ";" +
                                     str(SD['timeOnIcePerGame']) + ";" +
                                     str(SD['evenTimeOnIcePerGame']) + ";" +
                                     str(SD['shortHandedTimeOnIcePerGame']) + ";" +
                                     str(SD['powerPlayTimeOnIcePerGame']))

            CurrentPlayer = pd.read_csv(CurrentPlayer, sep=";")
            SkaterStatistics = pd.concat([SkaterStatistics, CurrentPlayer], ignore_index=True)
            intCounter += 1
        except:
            print("Missing Stats for Player " + PlayerLink + " " + SkaterRoster['FullName'][intCounter])
            intCounter += 1

    Season = str(20222023)

    GoalieStatistics = pd.DataFrame()

    intCounter = 0
    for PlayerLink in tqdm(GoalieDetails['Link']):
        SourceData = pd.DataFrame.from_dict(
            requests.get(
                url="https://statsapi.web.nhl.com" + PlayerLink + "/stats?stats=statsSingleSeason").json()).to_dict()[
            'stats'][0]['splits']
        try:
            SD = pd.DataFrame.from_dict(SourceData)['stat']
            SD = SD.to_dict()[0]
            CurrentPlayer = StringIO("""ID;Position;FullName;Team;TOI;OT;SO;T;W;L;Saves;PPSaves;SHSaves;EVSaves;SHShots;EVShots;PPShots;SvPct;GAA;G;GS;ShotsAgainst;GoalsAgainst;TOIperGame;PPSvPct;SHSvPct;EVSvPct
            """ +
                                     str(GoalieRoster['ID'][intCounter]) + ";" +
                                     GoalieRoster['PosAbbreviation'][intCounter] + ";" +
                                     GoalieRoster['FullName'][intCounter] + ";" +
                                     GoalieRoster['Team'][intCounter] + ";" +
                                     str(SD['timeOnIce']) + ";" +
                                     str(SD['ot']) + ";" +
                                     str(SD['shutouts']) + ";" +
                                     str(SD['ties']) + ";" +
                                     str(SD['wins']) + ";" +
                                     str(SD['losses']) + ";" +
                                     str(SD['saves']) + ";" +
                                     str(SD['powerPlaySaves']) + ";" +
                                     str(SD['shortHandedSaves']) + ";" +
                                     str(SD['evenSaves']) + ";" +
                                     str(SD['shortHandedShots']) + ";" +
                                     str(SD['evenShots']) + ";" +
                                     str(SD['powerPlayShots']) + ";" +
                                     str(SD['savePercentage']) + ";" +
                                     str(SD['goalAgainstAverage']) + ";" +
                                     str(SD['games']) + ";" +
                                     str(SD['gamesStarted']) + ";" +
                                     str(SD['shotsAgainst']) + ";" +
                                     str(SD['goalsAgainst']) + ";" +
                                     str(SD['timeOnIcePerGame']) + ";" +
                                     str(SD['powerPlaySavePercentage']) + ";" +
                                     # str(SD['shortHandedSavePercentage']) + ";" +
                                     str(SD['evenStrengthSavePercentage']))

            CurrentPlayer = pd.read_csv(CurrentPlayer, sep=";")

            GoalieStatistics = pd.concat([GoalieStatistics, CurrentPlayer], ignore_index=True)
            intCounter += 1
        except:
            print("Missing Stats for Player " + PlayerLink + " " + GoalieRoster['FullName'][intCounter])
            intCounter += 1

    # print(GoalieStatistics)

    SkaterStatistics['TRCWIHP'] = SkaterStatistics['A'] * 8 + SkaterStatistics['G'] * 15 + SkaterStatistics['PIM'] * -10 + \
                                  SkaterStatistics['PPP'] * 4 + SkaterStatistics['GWG'] * 10 + SkaterStatistics[
                                      'SHP'] * 16 + SkaterStatistics['PlusMinus'] * 2
    GoalieStatistics['TRCWIHP'] = GoalieStatistics['W'] * 6 + GoalieStatistics['Saves'] * 0.2 + GoalieStatistics[
        'SO'] * 80 - GoalieStatistics['L'] * 8

    Skatering = pd.merge(SkaterPool, SkaterStatistics, left_on=['Player', 'Team'], right_on=['FullName', 'Team'])
    Skatering['T2022'] = Skatering['TRCWIHP'].where(Skatering['Team'] != Skatering['SpecialTeam'],
                                                    Skatering['TRCWIHP'] * 1.1)

    Goalieing = pd.merge(GoaliePool, GoalieStatistics, left_on=['Player', 'Team'], right_on=['FullName', 'Team'])
    Goalieing['T2022'] = Goalieing['TRCWIHP'].where(Goalieing['Team'] != Goalieing['SpecialTeam'],
                                                    Goalieing['TRCWIHP'] * 1.1)

    PoolSummary = pd.concat([
        Skatering[['Competitor', 'Player', 'Team', 'Position_x', 'Bid', 'T2022']],
        Goalieing[['Competitor', 'Player', 'Team', 'Position_x', 'Bid', 'T2022']]
    ])

    PoolSummary.columns = ['Competitor', 'Player', 'Team', 'Position', 'Bid', 'Points']

    pd.set_option('display.max_rows', 1000)

    PoolSummary = PoolSummary.sort_values(by=['Competitor', 'Position'], ascending=True)

    Points = PoolSummary.groupby('Competitor').sum()
    Points = Points.sort_values(by='Points', ascending=False)

    print(Points)
    print(PoolSummary)

st.dataframe(Points)
st.dataframe(PoolSummary)