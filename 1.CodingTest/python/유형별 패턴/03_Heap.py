"""
Heap (힙) 패턴 정리
- 최솟값/최댓값을 O(log n)에 추출
- 파이썬 heapq는 최소 힙(min-heap)
- 활용: 우선순위 큐, Top-K, 중앙값, 다익스트라
"""
import heapq


# ============================================================
# 1. 기본 힙 연산
# ============================================================
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

smallest = heapq.heappop(heap)   # 1 (최솟값 추출)
peek = heap[0]                    # 힙의 최솟값 확인 (pop 안 함)

# 리스트를 힙으로 변환 O(n)
arr = [5, 3, 1, 4, 2]
heapq.heapify(arr)  # arr이 제자리에서 힙으로 변환


# ============================================================
# 2. 최대 힙 (Max Heap) - 부호 반전 트릭
# ============================================================
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -2)

largest = -heapq.heappop(max_heap)  # 3 (최댓값 추출)


# ============================================================
# 3. Top-K 요소 찾기
# ============================================================
def top_k_smallest(nums, k):
    """K번째로 작은 수"""
    return heapq.nsmallest(k, nums)[-1]

def top_k_largest(nums, k):
    """K번째로 큰 수"""
    return heapq.nlargest(k, nums)[-1]

# 힙으로 직접 구현 (효율적)
def kth_largest(nums, k):
    """크기 k인 최소힙 유지 → 힙 top이 k번째 큰 수"""
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)  # pop + push 한번에
    return heap[0]


# ============================================================
# 4. 튜플 힙 (우선순위 + 데이터)
# ============================================================
task_heap = []
heapq.heappush(task_heap, (1, "low priority"))
heapq.heappush(task_heap, (3, "high priority"))
heapq.heappush(task_heap, (2, "medium priority"))

priority, task = heapq.heappop(task_heap)  # (1, "low priority")
# 첫 번째 원소로 정렬, 같으면 두 번째 원소로 비교


# ============================================================
# 5. 다익스트라 알고리즘 (최단 경로)
# ============================================================
def dijkstra(graph, start, n):
    """graph[node] = [(neighbor, weight), ...]"""
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (거리, 노드)

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:  # 이미 더 짧은 경로 발견됨
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist


# ============================================================
# 6. 중앙값 찾기 (두 개의 힙)
# ============================================================
class MedianFinder:
    def __init__(self):
        self.small = []  # 최대 힙 (부호 반전)
        self.large = []  # 최소 힙

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        # small의 최대값을 large로 이동
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # 크기 균형 유지 (small >= large)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2


# ============================================================
# 7. K개 정렬 리스트 병합
# ============================================================
def merge_k_sorted(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (값, 리스트idx, 원소idx)

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    return result


# ============================================================
# 핵심 정리
# ============================================================
# - heapq는 최소 힙만 지원 → 최대 힙은 -부호로 해결
# - heappush/heappop: O(log n), heapify: O(n)
# - heapreplace(heap, val): pop + push를 한번에 (더 효율적)
# - nsmallest/nlargest: k가 작을 때 유용, 큰 경우 정렬이 나음
# - 튜플 사용 시 첫 번째 원소 기준 정렬
# - 다익스트라: 힙 + 거리 배열 조합
