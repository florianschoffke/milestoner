import datetime
import Milestone
from plantweb.render import render_file

def get_date_range(milestones: list[Milestone.Milestone]):
    mindate = None
    maxdate = None

    for milestone in milestones:
        milestone_start_date = datetime.datetime.strptime(milestone._target_start, "%Y-%m-%d")
        milestone_end_date = datetime.datetime.strptime(milestone._target_end, "%Y-%m-%d")

        if (mindate is None):
            mindate = milestone_start_date
            maxdate = milestone_end_date
        else:
            if (milestone_start_date < mindate):
                mindate = milestone_start_date
            elif (milestone_end_date > maxdate):
                maxdate = milestone_end_date

    return [mindate, maxdate]
        
def get_all_teams(milestones):
    teams = []
    for milestone in milestones:
        if milestone.team not in teams:
            teams.append(milestone.label)
    return teams

def sort_by_team(milestones):
    milestones_by_team = {}
    for milestone in milestones:
        if milestone.team in milestones_by_team:
            milestones_by_team[milestone.team].append(milestone)
        else:
            milestones_by_team[milestone.team] = [milestone]
    return milestones_by_team

def render_puml_file(puml_string):
    infile = 'milestones.png'
    with open(infile, 'wb') as fd:
        fd.write(puml_string.encode('utf-8'))

    print('==> INPUT FILE:')
    print(infile)

    outfile = render_file(
        infile,
        renderopts={
            'engine': 'graphviz',
            'format': 'png'
        },
        cacheopts={
            'use_cache': False
        }
    )

    print('==> OUTPUT FILE:')
    print(outfile)