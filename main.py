#main entry point for linkbot
import time
import json
from slackclient import SlackClient


with open("config.json") as fd:
    config = json.load(fd)

print config
sc = SlackClient(config["slack_token"])

if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
