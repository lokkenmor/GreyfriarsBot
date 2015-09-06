#!/usr/bin/python3

import re;

class EdinburghMeetupAgent():
    """Edinburgh Meetup Agent. Scans /r/Edinburgh of thread containing the
    [MEETUP] tag in the title, or with the word meetup or any derivations
    thereof. Does some administrative actions from there - those actions
    tdb."""

    regexps = [r"\[meetup\]", r"meetup", r"meet-up", r"meet up"];
    threads = None;

    def __init__(self, threads):
        self.threads = threads;
        self.process_threads();
        return;

    def process_threads(self):
        # Need to take a copy of self.threads because iterating over lists
        # apparently alters the list. (They're treated more as a queue...)
        threads = self.threads;

        for thread in threads:
            for regexp in regexps:
                res = re.search(regexp, thread.title, re.IGNORECASE);
                if res == None or res == '':
                    continue;

                # There's clearly something here, now we just need to knwo what
                res = res.lower();
                actions = {
                        r"\[meetup\]"   : definite_meetup,
                        r"meetup"       : possible_meetup,
                        r"meet-up"      : possible_meetup,
                        r"meet up"      : possible_meetup,
                        }
                self.actions[regexp](thread);

        return;

    def definite_meetup(thread):
        # This is definitely a meetup thread. Someone is setting up a meetup,
        # or trying to, so what we'll do now is notify anyone who is subcribed
        # to the bot to come and check out the thread.
        EdinburghMeetupNotificationAgent(thread);
