from flask import Flask, render_template, redirect, url_for
from scraper import *
import json
app = Flask(__name__)
app.secret_key = "Secret Key"



#This is the index route where we are going to call the main data fetching function
@app.route('/')
def Index():
    scraper = ProxyScraper()
    scraper.run()
    return render_template('index.html', proxies=scraper.results)



#This route is for making user offline
@app.route('/offline/<id>/', methods = ['GET', 'POST'])
def offline(id):
    url = 'https://iptrade.zendesk.com/api/v2/channels/voice/availabilities/'+id+'.json'
    payload = {"availability":
        {
        "agent_state": "offline"
        }
    }
    headers = {'Authorization': 'Basic bWVlbmFsLnNoYXJtYUBidC5jb206V29uZGVyd29tYW5AMjM=', 'content-type': 'application/json'}
    r = requests.put(url, data=json.dumps(payload), headers=headers)


    #CheckAgentData = -1
    #while CheckAgentData < 0:
     #   confirmation = requests.get(url, headers={'Authorization': 'Basic bWVlbmFsLnNoYXJtYUBidC5jb206V29uZGVyd29tYW5AMjM='})
     #   AgentData = confirmation.text
     #   CheckAgentData = AgentData.find('offline')
      #  print(AgentData)
      #  print(CheckAgentData)
      #  print("Waiting for API to update data...")

    #while True :
        #with open('proxies.csv', 'rt') as f:
        #    reader = csv.reader(f, delimiter=',')
     #   with open('proxies.csv', 'r') as read_obj:
     #       csv_reader = reader(read_obj)
     #       for row in csv_reader:
     #           print(row)
     #           if row[1] == id and row[16] == "offline":  # if the username shall be on column 3 (-> index 2)
     #                   return redirect(url_for('Index'))
     #                   print("Waiting for API to update data...")
     #           else:
     #               scraper = ProxyScraper()
     #               scraper.run()
     #               pass

    return redirect(url_for('Index'))




if __name__ == "__main__":
    app.run(debug=True)