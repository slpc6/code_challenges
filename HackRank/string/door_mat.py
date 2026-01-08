"""door mat"""

n, m = map(int, input().split())
LINE = '-'
PALE = '.|.'
CENTER = (m - 3) // 2

for i in range(0, n // 2):
    print(LINE * CENTER + PALE * (2 * i + 1) + LINE * CENTER)
    CENTER -= 3

print(LINE * ((m - 7) // 2) + 'WELCOME' + LINE * ((m - 7) // 2))
CENTER = 3


for i in range((n // 2) - 1, -1, -1):
    print(LINE * CENTER + PALE * (2 * i + 1) + LINE * CENTER)
    CENTER += 3
