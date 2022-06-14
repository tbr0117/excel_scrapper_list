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
    SourceFieldMeta(SourceFieldName="Date", AliasName="Date", Required=False, DataType=datetime.date, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedLevel=1, GroupedAndHeaderAsForm=False, ShouldBe=True ),
    SourceFieldMeta(SourceFieldName="Num", AliasName="Num", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedLevel=1, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Name", AliasName="Name", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedLevel=1, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Memo/Description", AliasName="Memo/Description", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False ),
    SourceFieldMeta(SourceFieldName="Account #", AliasName="Account #", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, ShouldBe=True),
    SourceFieldMeta(SourceFieldName="Account", AliasName="Account", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Debit", AliasName="Debit", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Credit", AliasName="Credit", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
]

# C://Users//BhargavaTanguturi//Downloads//Audit Application Test Data For General Journal.xlsx

oMyExcelReader = MyExcelReader("test_data/GL_format_2.xlsx", aFieldStr=aSourceFields)
aData = oMyExcelReader.get_sheet_data(aFieldStr=aSourceFields)
print(aData)