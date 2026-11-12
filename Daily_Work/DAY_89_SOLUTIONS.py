
import heapq

def lastStoneWeight(stones: list[int]) -> int:
        
        max_heap = []

        for num in stones:

            heapq.heappush(max_heap,-num)

        first = heapq.heappop(max_heap)
        second = heapq.heappop(max_heap)

        diff = first - second

        heapq.heappush(max_heap,diff)

        
        print(max_heap)


lastStoneWeight([2,7,4,1,8,1])