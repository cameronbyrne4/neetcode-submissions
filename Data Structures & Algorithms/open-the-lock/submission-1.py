from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        BFS
        - 8 directions of moving each digit by 1 space
        - return when we run into fail case
        - increment move count by 1
        '''
        if "0000" in deadends:
            return -1
        q = deque()
        v = set()
        q.append("0000")
        v.add("0000")
        dirs = [-1, 1]
        num_moves = 0
        while q:    # There were things to append
            # Break if target
            # dont go to visited
            # dont go to deadends
            # 9 and 0 are connected
            # mark visited before adding to q
            if target in q:
                return num_moves
            for _ in range(len(q)):
                curnum_base = q.popleft()
                # 8 unique transformations
                for i in range(4):
                    for dr in dirs:
                        curnum = curnum_base
                        curnum = curnum[:i] + str((int(curnum[i]) + dr) % 10) + curnum[i+1:]
                        if curnum not in v and curnum not in deadends:
                            v.add(curnum)
                            q.append(curnum)
            num_moves += 1
        
        # BFS fails to return the number of moves, never hit target
        return -1

