from ..schema import MappingStr, SourceFieldMeta
from typing import List
import datetime
from ..ExcelReader import MyExcelReader

aFieldMapping: List[MappingStr] = []
aSourceFields: List[SourceFieldMeta] = []

# aFieldMapping = [
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="Control", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
#     MappingStr(TargetField="TxnId", Required=False, DataType=str, TargetDataFormat="", DataConvertRequired=False, SourceField="", SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
# ]

aSourceFields = [
    SourceFieldMeta(SourceFieldName="Date", AliasName="Date", Required=True, DataType=datetime.date, IsGrouped=True, GroupedLevel=1, ShouldBe=True ),
    SourceFieldMeta(SourceFieldName="Num", AliasName="Num", DataType=str, IsGrouped=True, GroupedLevel=1 ),
    SourceFieldMeta(SourceFieldName="Name", AliasName="Name", DataType=str, IsGrouped=True, GroupedLevel=1 ),
    SourceFieldMeta(SourceFieldName="Memo/Description", AliasName="Memo/Description", DataType=str ),
    SourceFieldMeta(SourceFieldName="Account #", AliasName="Account #", Required=True, DataType=str, ShouldBe=True),
    SourceFieldMeta(SourceFieldName="Account", AliasName="Account", DataType=str ),
    SourceFieldMeta(SourceFieldName="Debit", AliasName="Debit", DataType=str ),
    SourceFieldMeta(SourceFieldName="Credit", AliasName="Credit", DataType=str ),
]

# C://Users//BhargavaTanguturi//Downloads//Audit Application Test Data For General Journal.xlsx

oMyExcelReader = MyExcelReader("test_data/GL_format_2.xlsx", aFieldStr=aSourceFields)
aData = oMyExcelReader.get_sheet_data(aFieldStr=aSourceFields)
print(aData)