def load_data() -> list:
    points = {}
    try:
        with open('points.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                username = line.split(" ")[0]
                point = int(line.split(" ")[1])
                if username not in points:
                    points[username] = point
                else:
                    if point > points[username]:
                        points[username] = point
        return list(points.items())
    except:
        return []
