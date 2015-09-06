#!/usr/bin/python3

class EdinburghController():
    """
    Edinburgh Controller. Controller class for what gets executed on the
    /r/edinburgh subreddit by the Greyfriars bot. Delegates all work to other
    classes that can be added at will.
    """

    pmsg_agents   = ['EdinburghSubscriberPMAgent']
    thread_agents = ['EdinburghMeetupAgent'];
    LIMIT = 50;

    def __init__(self, config, username, reddit, subreddit):
        """
        Automated Controller/Delegator for the GreyfriarsBot.
        Automatically runs the GreyfriarsBot consituent part, namely the PM 
        agent and the thread scraping agent.
        Can be extended to execute the 
        """
        # Get any new private messages we received to our inbox and pass them
        # along to whichever agents we use to handle PMs.
        pms = self.get_private_messages(config);
        self.run_pm_agents(pms);

        # Get the threads (Submissions) that have made to the sub-reddit and
        # pass them along to be processed by whichever agents have been
        # assigned to work on threads.
        threads = self.get_threads(subreddit, config)
        self.run_thread_agents(threads);
        return;


    def get_private_messages(self, config):
        """
        Fetch any new private messages we've got in our inbox
        """
        


    def run_pm_agents(self, priv_msgs):
        """
        Run the PM agents
        """


    def get_threads(self, subreddit, config):
        last_thread = config['EdinburghController']['last_thread'];
        if last_thread == -1 or last_thread == None:
            threads = subreddit.get_new(limit = self.LIMIT);
        else
            threads = subreddit.get_new(limit = self.LIMIT, 
                    place_holder = last_thread);
        return threads;


    def run_thread_agents(self, threads):
        for agent in self.thread_agents:
            running = eval(agent)(threads);
