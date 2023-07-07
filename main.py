import Jira_connector
import Milestone
import Puml_Tools
import Puml_Creator

# 1 Get Milestones
milestones = Milestone.map_issues_to_milestones(Jira_connector.get_Jira_Milestones())

# 2 Sort by date
milestones = sorted(milestones, key=lambda x: x.target_start)

# 3 Create PlantUml timeline
plantUml = Puml_Creator.create_timeline(milestones)

Puml_Tools.render_puml_file(plantUml)