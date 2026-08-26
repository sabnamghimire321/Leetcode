import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        
        users = self.following[userId] | {userId}
        
        for u in users:
            if u in self.tweets:
                idx = len(self.tweets[u]) - 1
                time, tweet_id = self.tweets[u][idx]
                heapq.heappush(heap, (time, tweet_id, u, idx))
                
        while heap and len(feed) < 10:
            time, tweet_id, u, idx = heapq.heappop(heap)
            feed.append(tweet_id)
            if idx > 0:
                next_idx = idx - 1
                next_time, next_tweet_id = self.tweets[u][next_idx]
                heapq.heappush(heap, (next_time, next_tweet_id, u, next_idx))
                
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
