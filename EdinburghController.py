#!/usr/bin/python3

class EdinburghController():
    """Edinburgh Controller. Controller class for what gets executed on the
    /r/edinburgh subreddit by the Greyfriars bot. Delegates all work to other
    classes that can be added at will"""

    agents = ['EdinburghMeetupAgent'];
    LIMIT = 50;

    def __init__(self, subreddit, config):
        threads = self.get_threads(subreddit, config)
        self.run_agents(threads);
        return;

    def get_threads(subreddit, config):
        last_thread = config['EdinburghController']['last_thread'];
        if last_thread == -1 or last_thread == None:
            threads = subreddit.get_new(limit = self.LIMIT);
        else
            threads = subreddit.get_new(limit = self.LIMIT, 
                    place_holder = last_thread);
        return threads;

    def run_agents(self, threads):
        for agent in self.agents:
            running = eval(agent)(threads);
