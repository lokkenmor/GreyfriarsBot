#!/usr/bin/python3

# Author:  lokkenmor <lokkenmor@live.co.uk>
# Name:    GreyfriarsBot
# Purpose: A bot to periodically poll the /r/Edinburgh subreddit to scan for
#          threads setting up or requesting a meetup. The intention is provide
#          a subscribe-publish service, using reddit's PM system, to notify
#          interested parties when meetup threads are posted, without
#          cluttering up the main part of the /r/Edinburgh board.

import argparse;
import sys;

from CLIParsedOutput import CLIParsedOutput


def parse_cli(argv):
    cli_p = argparse.ArgumentParser(description="""
    GreyfriarsBot.
    A bot to periodically poll /r/edinburgh and determine whether any new threads
    posted since the last execution are trying to organise, or illict, a mettup
    within the community.
    If so, the bot will notify the poster about /r/edinburgh_meetups and may cross
    post the thread there.
    The bot will also operate a publish-subscribe mechanism to notify anyone who is
    register for aleart a direct notifiaction of when meetups are planned.""");

    parsed_output = CLIParsedOutput();

    cli_p.add_argument('--config', 
            type=argparse.FileType('r'),
            help='Configuration file to load',
            required=True,
            metavar='file');

    cli_p.parse_args(argv, namespace=parsed_output);

    return parsed_output;


def main():
    # Need to drop the first argument, which is the script name, from the list
    # of CLI args to process
    parsed_output = parse_cli(sys.argv[1:]);

main();
