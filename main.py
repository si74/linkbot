#main entry point for linkbot
import time
import json
from slackclient import SlackClient
import multiprocessing
import urlmarker
import re

#worker checks for https link and prints/adds to db if that's the case
def worker(msgs, sc):
    """thread worker function"""
    if msgs["type"] == "message":
        #check if message contains a link
        print 'Worker:', msgs
        if "subtype" in msgs:
            if msgs["subtype"] == "message_changed":
                return

        #go through regex process to determine if there is a link
        link = re.findall(urlmarker.URL_REGEX, msgs["text"])
        channel = msgs["channel"]

        if len(link) > 0:
            print link
            print channel

            #grab channel info
            

        #grab channel the link appeared in

    return



if __name__ == "__main__":
    with open("config.json") as fd:
        config = json.load(fd)

    sc = SlackClient(config["slack_token"])

    jobs = [] #should i remove the jobs from a queue?
    if sc.rtm_connect():
        while True:
            line = sc.rtm_read()
            if len(line) > 0:
                 p = multiprocessing.Process(target=worker, args=(line, sc))
                 jobs.append(p)
                 p.start()
            time.sleep(1)
    else:
        print "Connection Failed, invalid token?"
