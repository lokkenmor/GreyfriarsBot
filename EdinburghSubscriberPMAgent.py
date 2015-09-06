#!/usr/bin/python3

class EdinburghSubscriberPMAgent():
    """
    Edinburgh Subscriber PM Agent.

    Agent used to read private messages from a given user's inbox and scan them
    for potential subscribers.
    """

    subscribers = [];

    def __init__(self, reddit):
        """
        Get a list of messages of unread.
        Process that list of unread messages
        Tell reddit these messages have been processed.
        """
        # Get the list of unread messages from reddit
        messages = reddit.get_unread();

        # Fetch the list of subscribers
        self.fetch_subscribers();

        # Process the list
        self.process_pms(messages);


    def fetch_subscribers():
        """
        Fetch the list of subscribers from the list file (as defined by the
        config). Read it into a list of users that we'll manipulate later.
        """
        global config;

        subs = open(config['EdinburghSubscribers']['list'], 'r');
        for sub in subs:
            self.subscribers.append(sub.rstrip());

        subs.close();


    def process_pms(self, messages):
        """
        Process a list of private messages looking for subscribe/unsubscribe
        keywords.
        """
        for msg in messages:
            if(re.search(r"^SUBSCRIBE$", msg.subject)):
                self.add_subscriber(msg);
            elif(re.search(r"^UNSUBSCRIBE$", msg.subject):
                self.rm_subscriber(msg);
            else:
                self.respond_confused(msg);


    def add_subscriber(self, msg):
        """
        Add the username of the sender of the given message to the list
        of subscribed users (write it to the end of the file defined in 
        the config).
        """
        self.subscribers.append(msg.author.name);

        # Quick and easy duplication removal. Doesn't maintain ordering but
        # that's not really that important for this use-case.
        self.subscribers = list(set(self.subscribers));


    def rm_subscriber(self, msg):
        """
        Remove the username of the sender of the given message from the list
        of subscribed users by reading the file to a list
        """
        self.subscribers.remove(msg.author.name);
