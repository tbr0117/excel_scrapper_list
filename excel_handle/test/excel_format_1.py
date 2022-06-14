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
    SourceFieldMeta(SourceFieldName="Control", AliasName="Control", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedLevel=1, GroupedAndHeaderAsForm=False, ShouldBe=True ),
    SourceFieldMeta(SourceFieldName="Batch", AliasName="Batch",  Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedLevel=1, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Period", AliasName="Period", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedLevel=1, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Date", AliasName="Date", Required=False, DataType=datetime.date, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedLevel=1, GroupedAndHeaderAsForm=False, ShouldBe=True ),
    SourceFieldMeta(SourceFieldName="Book", AliasName="Book", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedLevel=1, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Property", AliasName="Property", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Account", AliasName="Account", Required=True, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False, ShouldBe=True ),
    SourceFieldMeta(SourceFieldName="Debit", AliasName="Debit", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Credit", AliasName="Credit", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Reference", AliasName="Reference", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Source", AliasName="Source", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
    SourceFieldMeta(SourceFieldName="Description", AliasName="Description", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, GroupedAndHeaderAsForm=False ),
]

# C://Users//BhargavaTanguturi//Downloads//Audit Application Test Data For General Journal.xlsx

oMyExcelReader = MyExcelReader("test_data/GL_format_1.xlsx", aFieldStr=aSourceFields)
aData = oMyExcelReader.get_sheet_data(aFieldStr=aSourceFields)
print(aData)