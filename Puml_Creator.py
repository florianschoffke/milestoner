from plantweb import main
import Milestone
import Puml_Tools
import datetime

def create_timeline(milestones: list[Milestone.Milestone]):
    plantUml_Builder = ""
    plantUml_Builder = initiate_plantuml(plantUml_Builder)
    
    project_start = milestones[0].target_start
    plantUml_Builder = add_settings(plantUml_Builder, project_start)
    teams_dict = Puml_Tools.sort_by_team(milestones)

    for team_key in teams_dict:
        plantUml_Builder = plantUml_Builder + "-- " + team_key + " --\n"

        milestone: Milestone.Milestone
        for milestone in teams_dict[team_key]:
            plantUml_Builder = plantUml_Builder + "[" + milestone.name + "] happens at " + milestone.target_start + "\n"
        
        plantUml_Builder = plantUml_Builder + "\n\n"
    
    plantUml_Builder = end_plantuml(plantUml_Builder)

    return plantUml_Builder
    

def initiate_plantuml(plantUml_Builder):
    current_date = datetime.datetime.now()
    current_date_string = current_date.strftime("%d.%m.%Y")

    plantUml_Builder = plantUml_Builder + "@startgantt  Milestone Chart \nprintscale weekly\n\n"
    plantUml_Builder = plantUml_Builder + "title Zeitleiste der Meilensteine des Team Medical \n"
    plantUml_Builder = plantUml_Builder + "footer Erstellt am " + current_date_string + "\n\n"
    return plantUml_Builder

def end_plantuml(plantUml_Builder):
    return plantUml_Builder + "@endgantt"

def add_settings(plantUml_Builder, projectStart):
    plantUml_Builder = plantUml_Builder + "printscale weekly\n\n"
    return plantUml_Builder + "Project starts " + projectStart + "\n\n"


#Project starts 2021-03-29
#[Review 01] happens at 2021-03-29
#[Review 02 - 3 weeks] happens on 3 weeks after [Review 01]'s end
#[Review 02 - 21 days] happens on 21 days after [Review 01]'s end

"""
@startgantt
printscale weekly

Project starts 2023-03-31
[Umsetzung] happens at 2023-03-31
[Titus Umsetzung] starts at 2023-04-01
[Titus Umsetzung] ends at 2023-05-06
[Anforderungsfinalisierung] happens at 2023-06-30
[M2 - TST- TOB-TFeat2 - GoLive] happens at 2023-07-01
@endgantt

"""