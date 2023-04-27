def load_data() -> list:
    points = []
    try:
        with open('points.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                username = line.split(" ")[0]
                point = line.split(" ")[1]
                points.append((username, int(point)))
        return points
    except:
        return []
