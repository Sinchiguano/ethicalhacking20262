#  Sort a list of vulnerability dictionaries by a numeric `severity` field, highest first, using `sorted()`.

vulnerabilities = [
    {'name': 'sql-injection', 'severity': 3},
    {'name':'xss', 'severity': 2},
    {'name': 'csrf', 'severity': 4}
]
sorted_vulnerabilities = sorted(vulnerabilities, key=lambda x: x['severity'], reverse=True)
print(sorted_vulnerabilities)


a