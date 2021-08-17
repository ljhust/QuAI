from influxdb import InfluxDBClient
import datetime

client = InfluxDBClient(database='testdb')

# client.create_database('testdb')

# print(client.get_list_database())
# print(client.query('show measurements'))
# current_time = datetime.datetime.utcnow().isoformat("T")
# body = [
#     {
#         "measurement": "students",
#         "time": current_time,
#         "tags": {
#             "class": 1
#         },
#         "fields": {
#             "name": "Hyc",
#             "age": 3
#         },
#     }
# ]

# res = client.write_points(body, database='testdb')

result = client.query('select * from students;')
print("Result: {0}".format(result))

