class Milestone:
    def __init__(self, target_start, target_end, name, label, team):
        self._target_start = target_start
        self._target_end = target_end
        self._name = name
        self._label = label
        self.team = team

    # target_start getter and setter
    @property
    def target_start(self):
        return self._target_start

    @target_start.setter
    def target_start(self, value):
        self._target_start = value

    # target_end getter and setter
    @property
    def target_end(self):
        return self._target_end

    @target_end.setter
    def target_end(self, value):
        self._target_end = value

    # name getter and setter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # label getter and setter
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value

    # team getter and setter
    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

def map_issues_to_milestones(issues):
    milestones = []
    for issue in issues:
        target_start = issue.fields.customfield_10027
        target_end = issue.fields.customfield_10028
        name = issue.fields.summary
        label = issue.fields.labels
        if (issue.fields.customfield_10001 is not None):
            team = issue.fields.customfield_10001.name
        milestone = Milestone(target_start, target_end, name, label, team)
        if ((milestone is not None) & (milestone.target_start is not None)):
            milestones.append(milestone)
    return milestones