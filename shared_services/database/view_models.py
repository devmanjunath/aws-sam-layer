from schema.documents import Dispatch, Experiment, Project


class DispatchViewModel:
    def __init__(self, Dispatch: Dispatch):
        self.id = Dispatch.id
        self.title = Dispatch.title
        self.totalElectrons = Dispatch.totalElectrons
        self.completedElectrons = Dispatch.completedElectrons
        self.status = Dispatch.status
        self.startTime = Dispatch.startTime
        self.lastUpdated = Dispatch.lastUpdated
        self.statusValue = Dispatch.statusValue
        self.parentId = str(Dispatch.parent)
        self.type = "Dispatch"
        self.isPinned = Dispatch.isPinned
        self.statusValue = Dispatch.statusValue
        self.tags = Dispatch.tags
        self.runTime = Dispatch.runTime
        self.titleSearch = Dispatch.titleSearch


class ExperimentViewModel:
    def __init__(self, Experiment: Experiment):
        self.id = Experiment.id
        self.title = Experiment.title
        self.totalElectrons = Experiment.totalElectrons
        self.count = Experiment.totalCount
        self.completedElectrons = Experiment.completedElectrons
        self.status = Experiment.status
        self.startTime = Experiment.startTime
        self.statusValue = Experiment.statusValue
        self.lastUpdated = Experiment.lastUpdated
        self.parentId = str(Experiment.parent)
        self.type = "Experiment"
        self.tags = Experiment.tags
        self.runTime = Experiment.runTime
        self.titleSearch = Experiment.titleSearch


class PinDispatchViewModel:
    def __init__(self, Dispatch: Dispatch):
        self.id = Dispatch.id
        self.title = Dispatch.title
        self.totalElectrons = Dispatch.totalElectrons
        self.completedElectrons = Dispatch.completedElectrons
        self.status = Dispatch.status
        self.startTime = Dispatch.startTime
        self.lastUpdated = Dispatch.lastUpdated
        self.parentId = str(Dispatch.parent)
        self.isPinned = Dispatch.isPinned
        self.tags = Dispatch.tags
        self.runTime = Dispatch.runTime
        self.master = None



class ProjectViewModel:
    def __init__(self, Project: Project):
        self.id = Project.id
        self.title = Project.title
        self.count = Project.totalCount
        self.lastUpdated = Project.lastUpdated
        self.type = "Project"