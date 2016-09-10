import PIR as pir

import httplib2
import json
import time
import datetime

if __name__ == '__main__':
	
    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"
    
    url_occupancy = "http://192.168.0.3:5000/homecontrol/api/v1.0/occupancy"

    headers = {'Content-Type': content_type_header}
    
    while True:

        if pir.detect_motion():
            occupancy_data = {'timestamp': datetime.datetime.utcnow().isoformat(),
                          'occupancy': True,
                          'sensorID':'300',
                          'room':'myRoom'
                          }

        response_o, content_o = http.request(url_occupancy, 'POST', json.dumps(occupancy_data),headers=headers)
        
        print(response_o)
        print(content_o)

