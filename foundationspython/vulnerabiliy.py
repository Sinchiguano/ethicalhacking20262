# Model a Vulnerability with title, owasp_category, and severity, plus a summary() method.


class Vulnerability:        
    def __init__(self, title, owasp_category, severity):
        self.title = title
        self.owasp_category = owasp_category
        self.severity = severity

    def summary(self):
        return f"Vulnerability: {self.title}, Category: {self.owasp_category}, Severity: {self.severity}"   




vuln1 = Vulnerability("SQL Injection", "Injection", "High")
vuln2 = Vulnerability("Cross-Site Scripting (XSS)", "Cross-Site Scripting", "Medium")
vuln3 = Vulnerability("Insecure Direct Object References", "Broken Access Control", "High")

print('****************************')
print('Vulnerability Summaries:')


print(vuln1.summary())
print(vuln2.summary())
print(vuln3.summary())  