from Adafruit_TSL2561 import Adafruit_TSL2561
import temperature
import LDR as ldr
import PIR as pir

import httplib2
import json
import time
import datetime
import plotly.plotly as py
import plotly.graph_objs as go

if __name__ == '__main__':

    #Initialize luminosity sensor
    LuxSensor = Adafruit_TSL2561()
    LuxSensor.enable_auto_gain(True)
    
    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"

    #add separate URL or each sensor type, same with route on the server.
    url_temp = "http://192.168.0.3:5000/homecontrol/api/v1.0/temperature"
    url_ambientlight = "http://192.168.0.3:5000/homecontrol/api/v1.0/ambientlight"
    url_occupancy = "http://192.168.0.3:5000/homecontrol/api/v1.0/occupancy"
    
    headers = {'Content-Type': content_type_header}

    with open ('./config.json') as config_file:
        plotly_user_config = json.load(config_file)
        py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])


    token1 = plotly_user_config['streaming_tokens'][0]
    token2 = plotly_user_config['streaming_tokens'][1]

    stream_id1 = dict(token=token1, maxpoints=100)
    stream_id2 = dict(token=token2, maxpoints=100)

    trace1 = go.Scatter(x=[], y=[], stream=stream_id1, name='luminosity')
    trace2 = go.Scatter(x=[], y=[], stream=stream_id2, yaxis='y2', name='temperature', marker=dict(color='rgb(148,103,189'))

    data = [trace1, trace2]
    layout = go.Layout(title='Dashboard for room x',
                       yaxis=dict(title='luminusity in lux'), yaxis2=dict(title='temperature in C',
                        titlefont=dict(color='rgb(148, 103, 189)'),
                        tickfont=dict(color='rgb(148, 103, 189)'),
                       overlaying='y',
                       side='right'))

    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='dashboard for room x')
                    
    s1 = py.Stream(stream_id=token1)
    s2 = py.Stream(stream_id=token2)
    s1.open()
    s2.open()


    #url_temp = py.plot([{'x': [], 'y': [], 'type': 'scatter','stream': {
     #   'token': plotly_user_config['streaming_tokens'][0],
     #   'maxpoints': 200
     #   }, 'legendgroup':'Temperature', 'name': 'Temperature in C',
     #                    'mode':'lines', 'line':{'color':'rgb(164,194,244)'},
     #                    'showlegend':True
     #}], filename='Dashboard for room one')

    #print ("View your streaming graph here: ", url_temp)


    #stream1 = py.Stream(plotly_user_config['streaming_tokens'][0])
    #stream1.open()

    
    while True:

        try:
            temp = temperature.read_temp()[0]
            LDRvalue = ldr.read_LDR()
            lux = LuxSensor.calculate_lux()
        except OverflowError as err:
            print(err)
        else:
            lux_data = { 'timestamp': datetime.datetime.now().isoformat(),
                         'lux': "%.2f" %lux,
                         'ldrValue': LDRvalue,
                         'room': 'myRoom'
                        }

            temp_data = {'timestamp': datetime.datetime.now().isoformat(),
                         'temperature': temp,
                         'sensorID': '100',
                         'room': 'myRoom'
                        }

        #occupancy_state = pir.detect_motion()

        
        #print(occupancy_state)

        #if pir.detect_motion():
         #   occupancy_data['occupancy'] = True
            
            #response, content = http.request(url_occupancy, 'POST',
             #            json.dumps(occupancy_data),
              #           headers=headers)
       # else:
        #    pass

        #elif not pir.detect_motion:
        #occupancy_data = {'timestamp': datetime.datetime.utcnow().isoformat(),
         #                         'occupancy': False,
          #                        'sensorID':'300',
           #                       'room':'myRoom'
            #                  }
        #else:
           # pass
            
            
       # else:
        #    occupancy_data = {'timestamp': datetime.datetime.utcnow().isoformat(),
         #                         'occupancy': False,
          #                        'sensorID':'300',
           #                       'room':'myRoom'
            #                      }
            #print("here")
                
        
        #for nested value every minute. this way u can get 1 doc/hour containing
        #1 subdoc/min in temperature field. change "temp" above to empty dict to work.
        #for i in range(0,60,1):
            #data["temperature"].update({i : temperature.read_temp()[0]})
            #print(data["temperature"][i])
            #time.sleep(60)
        
        print ("Posting %s" % temp_data)
        print("posting %s" %lux_data)
        #print("posting %s" %occupancy_data)
        
        #response_o, content_o = http.request(url_occupancy, 'POST',
         #                                   json.dumps(occupancy_data),
          #                                  headers=headers)
                                            
        
        #response_t, content_t = http.request(url_temp, 'POST',
                                         #    json.dumps(temp_data),
                                          #   headers=headers)
        
        #response_l, content_l = http.request(url_ambientlight, 'POST',
                                           #  json.dumps(lux_data),
                                            # headers=headers)

        s1.write(dict(x=lux_data["timestamp"], y=lux_data["lux"]))
        s2.write(dict(x=lux_data["timestamp"], y=temp_data["temperature"]))              
        


        #print (response_t)
        #print (content_t)
        #print(response_l)
        #print(content_l)
        time.sleep(5)
        

        


