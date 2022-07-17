from itertools import count
from os import link, waitstatus_to_exitcode
from re import sub
from time import time
from flask import Flask, jsonify
from flask_cors import CORS
import praw

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def default():

    return jsonify({"status" : "200", "message" : "Hey there, happy hacking..."})

@app.route("/mreddit", methods=(['GET']))
def mReddit():
    mReddit = praw.Reddit(
        client_id="xVrGKhWt5Cz8M1U9ZS_6eQ",
        client_secret="clALfvI6H260htZAg-L_4secQLvXMw",
        password="donotgiveuponGod@2022",
        user_agent="testscript by u/holy0spirit",
        username="holy0spirit",
        )


    # subreddit to post to
    subreddits = ['TheYouShow', 'casualiama', 'IAmA']

    # title and link to post to subreddit
    title = "Osun poll: Aregbesola deletes post on Adeleke’s victory"
    links = "Check out this link for more information: https://punchng.com/osun-poll-aregbesola-deletes-post-on-adelekes-victory/"

    count = 0
    
    for subreddit in subreddits:
        count += 1
        mReddit.subreddit(subreddit).submit(title, selftext=links, send_replies=False)
        print("Successfully posted to ", subreddit, count, " of ", len(subreddits), "subreddits")

    return jsonify({"status" : "200", "message" : "Hey there, happy hacking..."})