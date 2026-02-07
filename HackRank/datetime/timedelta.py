"""Time Delta"""

from datetime import datetime


def time_delta(time1: str, time2: str) -> str:
    """"Calculate the time delta
    
    """
    date = datetime.strptime(time1, '%a %d %b %Y %H:%M:%S %z')
    date2 = datetime.strptime(time2, '%a %d %b %Y %H:%M:%S %z')
    return f"{abs(date - date2).total_seconds():.0f}"


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta + '\n')
