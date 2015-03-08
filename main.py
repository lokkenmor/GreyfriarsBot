#!/usr/bin/python3

# Author:  lokkenmor <lokkenmor@live.co.uk>
# Name:    GreyfriarsBot
# Purpose: A bot to periodically poll the /r/Edinburgh subreddit to scan for
#          threads setting up or requesting a meetup. The intention is provide
#          a subscribe-publish service, using reddit's PM system, to notify
#          interested parties when meetup threads are posted, without
#          cluttering up the main part of the /r/Edinburgh board.

import argparse;
import configparser;
import sys;

from CLIParsedOutput import CLIParsedOutput

# Global variables
config = None;
praw_user = None;


def parse_cli(argv):
    cli_p = argparse.ArgumentParser(description=
    """
    GreyfriarsBot.
    A bot to periodically poll /r/edinburgh and determine whether any new threads
    posted since the last execution are trying to organise, or illict, a mettup
    within the community.
    If so, the bot will notify the poster about /r/edinburgh_meetups and may cross
    post the thread there.
    The bot will also operate a publish-subscribe mechanism to notify anyone who is
    register for aleart a direct notifiaction of when meetups are planned.
    """);

    parsed_output = CLIParsedOutput();

    cli_p.add_argument('--configfile',
            type=argparse.FileType('r'),
            help='Configuration file to load',
            required=True,
            metavar='file');

    cli_p.parse_args(argv, namespace=parsed_output);

    return parsed_output;


def parse_config(config_f):
    # The config_f is the file handler which already open for read operations.
    # Which is why we use read_file, not plain old read.
    conf = configparser.ConfigParser();
    conf.read_file(config_f);

    # Check that we have the minimum configuration required to execute this bot
    # Minimums are:
    #   We know when we were last run
    #   The bot's username
    #   The bot's password
    #   The subreddit the bot is scraping
    #
    # We're not so concerned about what Classes the bot is using to search the
    # scraped space for because we could execute to completion happily without
    # them.
    assert(conf['general']['last_run'] is not None);
    assert(conf['praw']['username'] is not None);
    assert(conf['praw']['password'] is not None);
    assert(conf['praw']['subreddit'] is not None);

    return conf;


def connect_to_subreddit(config):
    global praw_user;

    # Connect and login to Reddit using the given config
    # TODO: Login failure handling
    praw_h = praw.Reddit(user_agent = config['praw']['agent_user']);
    praw_h.login(config['praw']['username'], config['praw']['password']);

    # Assert that we have a working connection and that it didn't break
    assert(praw_h is not None);

    # Export the uname to the global space so it can be picked up later
    # Connect to the subreddit given by the configuration info.
    praw_user = praw_h.user;
    subreddit = praw_h.get_subreddit(config['praw']['subreddit']);

    return subreddit;


def execute_on_subreddit(subreddit):
    global config;

    # If there's no agent configuration in the config file then break and
    # return
    if config[config['praw']['subreddit']]['agent'] is None:
        return;

    # Otherwise, execute the specified Agnet (singular - no support for
    # multiple agents).
    controller = config[config['praw']['subreddit']]['agent'](subreddit,
            config);




def main():
    global config;
    # Parse the CLI to somethign sane.
    # Need to drop the first argument, which is the script name, from the list
    # of CLI args to process
    parsed_cli = parse_cli(sys.argv[1:]);

    # Parse the config file given by the CLI inputs.
    config = parse_config(parsed_cli.configfile);

    # Establish connection to reddit via praw, using the settings from the
    # config file
    subreddit = connect_to_subreddit(config);

    execute_on_subreddit(subreddit);


main();
