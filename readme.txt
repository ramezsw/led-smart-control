This directory contains 3 important folders: 

-DataCollectionServer: the python server that runs as background daemon in the central linux server,  should always run on port 5000.

-SensorNode: contains the code that must be included in each newly installed sensor node. the server address must be manually changed. 

LEDControlDimmer: contains the Java fuzzy logic code and the FCL code for the dimming controller. this is written in Java and can be imported as JAR file in the existing java server.

Each directory contains a readme.txt on how to operate.

