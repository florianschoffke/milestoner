from jira import JIRA

def get_Jira_Milestones():
    # create a Jira client instance
    jira = JIRA('https://service.gematik.de/', token_auth='NDQ1Mjg5NjQ2NzEyOtTeU334JtMvsc5TDdndjA+vgrKp')

    # search for issues
    search_query = 'issuetype=Milestone AND status!=Cancelled AND "Target end" is not EMPTY'
    issues = jira.search_issues(search_query)

    jira.close()
    return issues