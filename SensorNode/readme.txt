This directory contains the code required by each sensor node. before running, change the server address in mongoClient.py and occupancyClient.py to the Local area address in which the data collection server is executing.

Ever sensor node installed must contain this folder keeping in mind that the specified address must manually be changed according to the server's address.

to run, simply click myclient.sh which is a bash script that run mongoClient.py and occupancyClient.py as background processes. or type ./mysclient.sh in terminal

the Client uses:
	Adafruit_I2C.py
	Adafruit_TSL2561.py
	LDR.py
	PIR.py
	temperature.py
	
MongoClient contains the API for sending data over to the Plot.ly visualisation server, and to the data collection server.

look at readme.txt for server to see the dependencies required.

mongoClient.py contains a lot of commented code for different formats to store the data stream in mongoDB.

must be in the same local area network as the data collection server to work. However the database itself can be in a remote location, which is handled by the server.

Both the sensor client and the central data collection server are written entirely in python 3.
