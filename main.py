#main entry point for linkbot
import time
import json
from slackclient import SlackClient
import multiprocessing

#worker checks for https link and prints/adds to db if that's the case
def worker(msgs):
    """thread worker function"""
    if msgs["type"] == "message":
        #check if message contains a link
        print 'Worker:', msgs
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
                 p = multiprocessing.Process(target=worker, args=(line))
                 jobs.append(p)
                 p.start()
            time.sleep(1)
    else:
        print "Connection Failed, invalid token?"
