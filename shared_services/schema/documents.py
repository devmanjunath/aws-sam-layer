import datetime
from enum import Enum
from typing import List, Optional

from beanie import Document, Link, PydanticObjectId
from pydantic import BaseModel, constr


class ItemStatus(Enum):
    COMPLETED = 3
    RUNNING = 2
    FAILED = 1


class GenericObjectProjection(BaseModel):
    _id: PydanticObjectId


class ItemStatus(Enum):
    COMPLETED = 3
    RUNNING = 2
    FAILED = 1


class GenericObjectProjection(BaseModel):
    _id: PydanticObjectId


class ItemStatus(Enum):
    COMPLETED = 4
    RUNNING = 3
    FAILED = 2
    NEW = 1


class Dispatch(Document):
    dispatchId: str
    createdBy: Optional[PydanticObjectId] = None
    title: constr(max_length=50)
    titleSearch: Optional[str] = None
    completedElectrons: int
    totalElectrons: int
    status: str = ""
    statusValue: int
    isArchived: bool = False
    isDeleted: bool = False
    isPinned: bool
    tags: Optional[list[str]] = []
    runTime: float
    createdAt: datetime.datetime
    lastUpdated: datetime.datetime
    startTime: datetime.datetime
    lastViewed: Optional[datetime.datetime]
    parent: Optional[PydanticObjectId] = None
    titleSearch: Optional[str]

    class Settings:
        validate_on_save = True


class Experiment(Document):
    experimentId: str
    createdBy: Optional[PydanticObjectId] = None
    totalCount: Optional[int]
    title: constr(max_length=50)
    titleSearch: Optional[str] = None
    completedElectrons: Optional[int]
    totalElectrons: Optional[int]
    status: Optional[str]
    statusValue: Optional[int]
    isArchived: bool = False
    isDeleted: bool = False
    tags: Optional[list[str]] = []
    runTime: Optional[float]
    createdAt: Optional[datetime.datetime]
    lastUpdated: Optional[datetime.datetime]
    startTime: Optional[datetime.datetime]
    lastViewed: Optional[datetime.datetime]
    dispatches: Optional[List[Link[Dispatch]]]
    parent: Optional[PydanticObjectId]
    titleSearch: Optional[str]

    class Settings:
        validate_on_save = True


class Project(Document):
    projectId: str
    totalCount: Optional[int]
    createdBy: Optional[PydanticObjectId] = None
    title: constr(max_length=50)
    titleSearch: Optional[str] = None
    isArchived: bool = False
    isDeleted: bool = False
    createdAt: Optional[datetime.datetime]
    startTime: Optional[datetime.datetime]
    runTime: Optional[float]
    status: Optional[str]
    statusValue: Optional[int]
    lastUpdated: Optional[datetime.datetime]
    dispatches: Optional[List[Link[Dispatch]]]
    experiments: Optional[List[Link[Experiment]]]

    class Settings:
        validate_on_save = True


class Summary(Document):
    itemId: PydanticObjectId
    title: constr(max_length=50)
    titleSearch: Optional[str] = None
    itemType: str
    status: str
    statusValue: int
    lastUpdated: Optional[datetime.datetime]
    lastUpdatedSearch: Optional[str]
    startTimeSearch: Optional[str]
    itemOwnedBy: Optional[PydanticObjectId] = None
    runTime: Optional[float]
    startTime: Optional[datetime.datetime]
    isHierarchyView: bool
    isActive: bool

    class Settings:
        validate_on_save = True
