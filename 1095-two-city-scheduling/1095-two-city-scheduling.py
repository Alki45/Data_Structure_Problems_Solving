class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        total_cost = 0
        
        # First n go to city A
        for i in range(n):
            total_cost += costs[i][0]
        
        # Remaining n go to city B
        for i in range(n, 2 * n):
            total_cost += costs[i][1]
        
        return total_cost