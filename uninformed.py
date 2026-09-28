from collections import deque
import heapq


def _neighbors(map_data, city):
    """Return a city's adjacent cities as (name, distance) pairs."""
    return sorted(map_data.get("graph", {}).get(city, {}).items())


def _has_locations(map_data, start, goal):
    locations = map_data.get("locations", {})
    return start in locations and goal in locations


def _not_found_result():
    return {"path": None, "expanded": [], "distance": 0.0}


def bfs(map_data, start, goal):
    """
    Breadth-First Search (BFS)
    Returns: {"path": list, "expanded": list, "distance": float}
    """
    if not _has_locations(map_data, start, goal):
        return _not_found_result()

    if start == goal:
        return {"path": [start], "expanded": [start], "distance": 0.0}
    
    queue = deque([(start, [start], 0.0)])
    visited = {start}
    expanded = []
    
    while queue:
        node, path, dist = queue.popleft()
        expanded.append(node)
        
        if node == goal:
            return {"path": path, "expanded": expanded, "distance": round(dist, 2)}
            
        # Sort neighbors alphabetically for deterministic tie-breaking
        for n_name, n_dist in _neighbors(map_data, node):
            if n_name not in visited:
                visited.add(n_name)
                queue.append((n_name, path + [n_name], dist + n_dist))
                
    return {"path": None, "expanded": expanded, "distance": 0.0}

def dfs(map_data, start, goal):
    """
    Depth-First Search (DFS)
    Returns: {"path": list, "expanded": list, "distance": float}
    """
    if not _has_locations(map_data, start, goal):
        return _not_found_result()

    if start == goal:
        return {"path": [start], "expanded": [start], "distance": 0.0}
    
    stack = [(start, [start], 0.0)]
    visited = set()
    expanded = []
    
    while stack:
        node, path, dist = stack.pop()
        
        if node in visited:
            continue
            
        visited.add(node)
        expanded.append(node)
        
        if node == goal:
            return {"path": path, "expanded": expanded, "distance": round(dist, 2)}
            
        # Reverse sort neighbors so they are popped in alphabetical order
        for n_name, n_dist in reversed(_neighbors(map_data, node)):
            if n_name not in visited:
                stack.append((n_name, path + [n_name], dist + n_dist))
                
    return {"path": None, "expanded": expanded, "distance": 0.0}

def ucs(map_data, start, goal):
    """
    Uniform-Cost Search (UCS)
    Returns: {"path": list, "expanded": list, "distance": float}
    """
    if not _has_locations(map_data, start, goal):
        return _not_found_result()

    pq = []
    # Entry: (cost, counter, node, path) to avoid comparisons on path list
    counter = 0
    heapq.heappush(pq, (0.0, counter, start, [start]))
    visited = set()
    expanded = []
    
    while pq:
        cost, _, node, path = heapq.heappop(pq)
        
        if node in visited:
            continue
            
        visited.add(node)
        expanded.append(node)
        
        if node == goal:
            return {"path": path, "expanded": expanded, "distance": round(cost, 2)}
            
        for n_name, n_dist in _neighbors(map_data, node):
            if n_name not in visited:
                counter += 1
                heapq.heappush(pq, (cost + n_dist, counter, n_name, path + [n_name]))
                
    return {"path": None, "expanded": expanded, "distance": 0.0}

def ids(map_data, start, goal):
    """
    Iterative Deepening Search (IDS)
    Returns: {"path": list, "expanded": list, "distance": float}
    """
    if not _has_locations(map_data, start, goal):
        return _not_found_result()

    if start == goal:
        return {"path": [start], "expanded": [start], "distance": 0.0}

    expanded = []
    
    def dls(node, path, dist, limit, visited_path):
        expanded.append(node)
        if node == goal:
            return {"path": path, "distance": dist}
        if limit <= 0:
            return None
            
        for n_name, n_dist in _neighbors(map_data, node):
            if n_name not in visited_path:
                res = dls(n_name, path + [n_name], dist + n_dist, limit - 1, visited_path | {n_name})
                if res is not None:
                    return res
        return None

    # Iteratively increase depth limit
    for limit in range(len(map_data.get("locations", {}))):
        visited_path = {start}
        res = dls(start, [start], 0.0, limit, visited_path)
        if res is not None:
            res["expanded"] = expanded
            res["distance"] = round(res["distance"], 2)
            return res
            
    return {"path": None, "expanded": expanded, "distance": 0.0}
