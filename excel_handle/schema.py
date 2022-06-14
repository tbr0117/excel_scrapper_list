from typing import Any, Optional, List
from pydantic import BaseModel

class MappingStr(BaseModel):
    TargetField:str
    Required:bool
    DataType:str
    DataConvertRequired:bool
    TargetDataFormat: str

    SourceField:str
    SourceDataFormat:str
    IsGrouped:bool
    GroupedAndHeaderAsForm:bool

class SourceFieldMeta(BaseModel):
    SourceFieldName:str
    AliasName:str
    SourceDataFormat:Optional[str] = ""
    DataType:Optional[Any] = str
    Required:Optional[bool] = False
    IsGrouped:Optional[bool] = False
    GroupedLevel:Optional[int] = 0
    GroupedAndHeaderAsForm:Optional[bool] = False
    DataConvertRequired:Optional[bool]
    FieldNameIndex:Optional[int] = 0
    FieldValueIndex: Optional[int] = 0
    MergedColumns:Optional[int] = 0
    ShouldBe:Optional[bool] = False
    IsFormStart: Optional[bool] = False
    IsFormEnd: Optional[bool] = False

class GroupLevel(BaseModel):
    Level:int
    Fields:List[SourceFieldMeta]
    MustBeField:Optional[SourceFieldMeta]
    FirstField:Optional[SourceFieldMeta]
    LastField:Optional[SourceFieldMeta]
    