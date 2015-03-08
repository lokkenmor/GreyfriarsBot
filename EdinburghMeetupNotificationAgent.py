#!/usr/bin/python3

class EdinburghMeetupNotificationAgent():
    """Edinburgh Meetup Notification Agent. This class should be called when a
    thread has definitely been determined to be setting up a meetup. This class
    will notify anyone in the subscribers list that a meetup thread has been
    posted and it will provide a link to that thread."""

    SUBSCRIBERS_FILE = 'edinburgh/meetup.sub';
    SUBJECT = "New meetup thread in /r/edinburgh"
    MESSAGE = """
    A new meetup thread has been posted in /r/Edinburgh. A link to the thread
    can be found below:

    {link}

    You received this message because you are subscribed to the GreyfriarsBot
    service of /r/Edinburgh. If you don't want to receive these messages any
    more please send this bot a message with "UNSUBSCRIBE" in the title (case
    sensitive).

    This bot is maintained by /u/lokkenmor.
    """

    def __init__(self, thread):
        __notify_subscribers__(thread);
        return;

    def __notfity_subscribers__(self, thread):
        global praw_user;
        subscribers = open(SUBSCRIBERS_FILE, 'r');
        for subscriber in subscribers:
            praw_user.send_message(
                    subscriber,
                    self.SUBJECT,
                    self.MESSAGE.format(link=thread.url);
