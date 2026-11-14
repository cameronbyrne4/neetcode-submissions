class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        input: tasks for a cpu to do in pairs (start time, task duration)
        output: list order of the tasks based on the original index

        limits:
        -- if idle and no tasks: stays idle
        -- if idle and tasks:
            -- picks shortest duration tasks
            -- if same durations: pick the first available one aka whatever has the smaller i since it's pre sorted

        Two min heaps was my thought..

        IDEA:
        - Sort task list by the first value in the pairs (the time it's ready) --> THIS IS ALREADY DONE
        - Check time, then add any available things to our min heap queue
        '''
        # Before we move stuff around, add the index to the task
        for i, task in enumerate(tasks):
            task.append(i)

        # Sort the initial list by the start time
        tasks.sort(key=lambda x: x[0])

        res = []
        heap = []               # keeps tracks of what is currently on the table
        time = 0
        i = 0           # not sure what this is for
        while heap or i < len(tasks):
            # Some available tasks are left to be added to the heap even tho they are available
            while i < len(tasks) and time >= tasks[i][0]:    # Time has passed
                heapq.heappush(heap, (tasks[i][1],tasks[i][2]))     # Only care about two variables now
                i += 1

            # Now everything available is on the minheap (if shit got added)
            # Case 1 - heap empty --> we take the first element and process it
            if heap:
                processingTime, index = heapq.heappop(heap)
                res.append(index)
                time += processingTime

            else: # Idle
                # time += 1 THIS IS WRONG WE SHOULD JUST GO OT THE NEXT TASK
                #time = tasks[i][0]
                time += 1




        return res