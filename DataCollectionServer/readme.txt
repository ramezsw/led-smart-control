This is the python data collection server. all sensor nodes must be connected to this server.

this server runs as a background process in the actual linux server where data is constantly recieved and stored in mongo DB over the HTTP rest API. 

Data is recieved in JSON format which is then sent to the mongo database to be stored as BSON format.

it can run over python 2 or python 3, though a few dependencies are required for this to execute.

look at requirements.txt for the dependencies.
