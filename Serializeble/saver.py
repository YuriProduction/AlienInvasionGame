from datetime import date


def save_data(points: int):
    with open('points.txt', 'a') as f:
        current_date = date.today()
        f.write(str(current_date) + " " + str(points) + "\n")
