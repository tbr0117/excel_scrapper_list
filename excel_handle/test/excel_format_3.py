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
    SourceFieldMeta( SourceFieldName="User", AliasName="User", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedAndHeaderAsForm=True, IsFormStart=True, ShouldBe=True ),
    SourceFieldMeta(SourceFieldName="Date", AliasName="Date", Required=False, DataType=datetime.date, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedAndHeaderAsForm=True, ShouldBe=True ),
    SourceFieldMeta(SourceFieldName="Description", AliasName="Description", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedAndHeaderAsForm=True ),
    SourceFieldMeta(SourceFieldName="Accounting Basis", AliasName="Accounting Basis", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedAndHeaderAsForm=True ),
    SourceFieldMeta(SourceFieldName="Accounting Book", AliasName="Accounting Book", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=True, GroupedAndHeaderAsForm=True, IsFormEnd=True ),
    SourceFieldMeta(SourceFieldName="Property", AliasName="Property", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False,),
    SourceFieldMeta(SourceFieldName="GL Account", AliasName="GL Account", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False, ShouldBe=True),
    SourceFieldMeta(SourceFieldName="Description", AliasName="Item Description", Required=False, DataType=str, DataConvertRequired=False,SourceDataFormat="", IsGrouped=False),
    SourceFieldMeta(SourceFieldName="Debit", AliasName="Debit", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False),
    SourceFieldMeta(SourceFieldName="Credit", AliasName="Credit", Required=False, DataType=str, DataConvertRequired=False, SourceDataFormat="", IsGrouped=False),
]

# C://Users//BhargavaTanguturi//Downloads//Audit Application Test Data For General Journal.xlsx

oMyExcelReader = MyExcelReader("test_data/GL_format_3.xlsx", aFieldStr=aSourceFields)
aData = oMyExcelReader.get_sheet_data(aFieldStr=aSourceFields)
print(aData)