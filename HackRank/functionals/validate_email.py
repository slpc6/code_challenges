"""Validating email addresses with a filter"""

import re

def fun(s: str) -> bool:
    """Validate a email with a regula expresion"""
    rule = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    if re.fullmatch(rule, s):
        return True
    return False


def filter_mail(emails_raw: list) -> list:
    """"Filter only valid emails"""
    return list(filter(fun, emails_raw))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
