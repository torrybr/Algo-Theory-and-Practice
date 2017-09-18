import re


def fun(s):
    result = re.match(r'[a-zA-z0-9\-_]+@[a-zA-Z0-9]+\..{1,3}$', s)
    return True if result else False


def filter_mail(emails):
    return filter(fun, emails)


if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    print emails
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
