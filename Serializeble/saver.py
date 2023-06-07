def save_data(points: int, username):
    with open('points.txt', 'a') as f:
        f.write(username + " " + str(points) + "\n")
