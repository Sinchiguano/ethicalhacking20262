# Sort a list of vulnerability dictionaries by a numeric severity field, highest first, using sorted().
vulnerabilities = [
    {"title": "SQL Injection", "owasp_category": "Injection", "severity": 3},
    {"title": "Cross-Site Scripting (XSS)", "owasp_category": "Cross-Site Scripting", "severity": 2},
    {"title": "Insecure Direct Object References", "owasp_category": "Broken Access Control", "severity": 3},
    {"title": "Security Misconfiguration", "owasp_category": "Security Misconfiguration", "severity": 2},
    {"title": "Sensitive Data Exposure", "owasp_category": "Sensitive Data Exposure", "severity": 3},
    {"title": "Cross-Site Request Forgery (CSRF)", "owasp_category": "Cross-Site Request Forgery", "severity": 2}
]

sorted_vulnerabilities = sorted(vulnerabilities, key=lambda x: x["severity"], reverse=True)
print(sorted_vulnerabilities)
