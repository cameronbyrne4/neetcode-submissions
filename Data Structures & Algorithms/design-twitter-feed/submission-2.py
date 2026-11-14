class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        # pushes into some data structure
        # tweet id could be key?
        # timestamp? for most recent via max heap, or just a stack!
        # maybe each user gets a stack in a dict # user --> tweets
        self.tweets.append((userId, tweetId))
        #print(f"Just pushed: {self.tweets}")
    def getNewsFeed(self, userId: int) -> List[int]:
        # go backwards thru tweets
        count = 0
        feed = []
        for u,t in reversed(self.tweets):
            if u not in self.follows[userId] and u != userId:
                continue
            # add to feed
            feed.append(t)
            #print(feed)
            count += 1
            if count == 10:
                return feed
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
