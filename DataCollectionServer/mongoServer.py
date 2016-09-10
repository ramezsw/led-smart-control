from flask import Flask, request, json
from pymongo import MongoClient
import datetime
import plotly.plotly as py  
import plotly.tools as tls   
import plotly.graph_objs as go

app = Flask(__name__)
mongo_client = MongoClient()

#tls.set_credentials_file(username='ramez93', api_key='zeghmdm5yb')
#stream_ids = tls.get_credentials_file()#['stream_ids']
#print (stream_ids)

@app.route("/homecontrol/api/v1.0/temperature", methods=['POST'])
def api_temperature():
	#stream_id = stream_ids[0]
	#stream_1 = go.Stream(token=stream_id, maxpoints=80)
	#stream_1 = dict(token=stream_id, maxpoints=60)
	
	if request.headers['Content-Type'] == 'text/plain':
		print (request.data)
		return 'OK', 200
        #insert new value in mongo every 1 minute. 1 doc/min/sensor.
	elif request.headers['Content-Type'] == 'application/json':   
		isoDate = datetime.datetime.strptime(request.json["timestamp"],"%Y-%m-%dT%H:%M:%S.%f")
		mongo_client['Sensors']['temperature'].insert({"timestamp": isoDate, "temperature": request.json["temperature"],"sensorID":request.json["sensorID"], "room": request.json["room"]}) 
		
		#s=py.Stream(stream_id)
		#s.open()
		#x= isoDate
		#y=request.json["temperature"]
		#s.write(dict(x=x,y=y))
		#s.close()
		#print(isoDate)
		#print(request.json["timestamp"])
        #print (mongo_client['Sensors']['temperature'].count())
		return "OK", 200
	else:
		return "Unsupported Media Type", 415
        
@app.route("/homecontrol/api/v1.0/ambientlight", methods=['POST'])
def api_ambientlight():
	if request.headers['Content-Type'] == 'text/plain':
		print(request.data)
		return 'OK', 200
		
	elif request.headers['Content-Type'] == 'application/json':
		isoDate = datetime.datetime.strptime(request.json["timestamp"],"%Y-%m-%dT%H:%M:%S.%f")
		mongo_client['Sensors']['ambientlight'].insert({"timestamp":isoDate, "lux": request.json["lux"], "ldrValue": request.json["ldrValue"], "room": request.json["room"]})
		return 'OK', 200
	else:
		return 'Unsupported Media', 415
		
@app.route("/homecontrol/api/v1.0/occupancy", methods=['POST'])
def api_occupancy():
	if request.headers['Content-Type'] == 'text/plain':
		print(request.data)
		return 'OK', 200
	elif request.headers['Content-Type'] == 'application/json':
		start_isoDate = datetime.datetime.strptime(request.json["timestamp"],"%Y-%m-%dT%H:%M:%S.%f")
		#end_isoDate = datetime.datetime.strptime(request.json["end"],"%Y-%m-%dT%H:%M:%S.%f")
		
		print(request.json['occupancy'])
		mongo_client['Sensors']['occupancy'].insert({"timestamp": start_isoDate, "occupancy": request.json["occupancy"],"sensorID":request.json["sensorID"],"room":request.json["room"]})
		return 'OK', 200
	else:
		return 'Unsupported Media', 415

if __name__ == '__main__':
    app.run(host ='0.0.0.0')

