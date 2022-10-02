class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            start,destination = destination,start
        overall_sum = sum(distance)
        route_sum = sum(distance[start:destination])
        return min(overall_sum-route_sum,route_sum)
