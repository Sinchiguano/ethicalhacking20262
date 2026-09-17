# Given a list of vulnerability dictionaries, count how many belong to each owasp_category. Use a dictionary of counts, no libraries.


vulnerabilities = [
    {"title": "SQL Injection", "owasp_category": "Injection", "severity": "High"},
    {"title": "Cross-Site Scripting (XSS)", "owasp_category": "Cross-Site Scripting", "severity": "Medium"},
    {"title": "Insecure Direct Object References", "owasp_category": "Broken Access Control", "severity": "High"},
    {"title": "Security Misconfiguration", "owasp_category": "Security Misconfiguration", "severity": "Medium"},
    {"title": "Sensitive Data Exposure", "owasp_category": "Sensitive Data Exposure", "severity": "High"},
    {"title": "Cross-Site Request Forgery (CSRF)", "owasp_category": "Cross-Site Request Forgery", "severity": "Medium"},   
]


def count_by_category(vulnerabilities_list):
    counts = {}
    for vuln in vulnerabilities_list:
        category = vuln["owasp_category"]
        counts[category] = counts.get(category, 0) + 1
    return counts

print(count_by_category(vulnerabilities))