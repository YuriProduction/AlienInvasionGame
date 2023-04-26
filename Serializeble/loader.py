def load_data() -> list:
    points = []
    try:
        with open('points.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                point = line.split(" ")[1]
                time = line.split(" ")[0]
                points.append((time, int(point)))
        return points
    except:
        return []
