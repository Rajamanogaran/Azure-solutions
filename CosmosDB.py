from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
table_service = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=Stock;AccountKey=V1K6c7Fj7QIdN8N856ecx0CWR1NiFgjIBZtP57l48gzQd1ElWy99rukhWttEbGsSeHmdkMaEthXG8Gj3XDMSBA==;TableEndpoint=(dbname and remove brakets).documents.azure.com:443;)
task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description' : 'Take out the trash', 'priority' : 200}
table_service.insert_entity('Amazn', task)