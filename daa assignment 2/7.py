import math

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def closest_pair(points):
    "Return (min_distance, (p1, p2)). Points is list of (x,y)."
    pts = sorted(points, key=lambda p: p[0])
    def recur(px):
        n = len(px)
        if n <= 3:
            best = float('inf')
            pair = (None, None)
            for i in range(n):
                for j in range(i+1, n):
                    d = dist(px[i], px[j])
                    if d < best:
                        best = d
                        pair = (px[i], px[j])
            return best, pair
        mid = n // 2
        midx = px[mid][0]
        dl, pairl = recur(px[:mid])
        dr, pairr = recur(px[mid:])
        best, pair = (dl, pairl) if dl < dr else (dr, pairr)
        strip = [p for p in px if abs(p[0] - midx) < best]
        strip.sort(key=lambda p: p[1])  
        for i in range(len(strip)):
            j = i+1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < best:
                d = dist(strip[i], strip[j])
                if d < best:
                    best = d
                    pair = (strip[i], strip[j])
                j += 1
        return best, pair
    return recur(pts)

# Example:
points = [(2.1,3.2),(3,4),(5,1),(1,2),(6,3),(2.2,3.1)]
print("Closest pair:", closest_pair(points))