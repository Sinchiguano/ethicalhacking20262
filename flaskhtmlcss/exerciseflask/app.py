from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# No database engine: every vulnerability submitted lives in this list
# (it is emptied every time the server restarts).
vulnerabilities = []

OWASP_CATEGORIES = [
    "A01:2021 - Broken Access Control",
    "A02:2021 - Cryptographic Failures",
    "A03:2021 - Injection",
    "A04:2021 - Insecure Design",
    "A05:2021 - Security Misconfiguration",
    "A06:2021 - Vulnerable and Outdated Components",
    "A07:2021 - Identification and Authentication Failures",
    "A08:2021 - Software and Data Integrity Failures",
    "A09:2021 - Security Logging and Monitoring Failures",
    "A10:2021 - Server-Side Request Forgery (SSRF)",
]

SEVERITIES = ["Low", "Medium", "High", "Critical"]


"Page 1: the form where i type the vulnerability data."
"GET shows the form, POST saves the data in the list and sends me to the report."
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vulnerability = {
            "title": request.form["title"],
            "category": request.form["category"],
            "severity": request.form["severity"],
        }
        vulnerabilities.append(vulnerability)
        return redirect(url_for("report"))

    return render_template(
        "index.html",
        categoriesHtml=OWASP_CATEGORIES,
        severitiesHtml=SEVERITIES,
    )


"Page 2: the report, it loops through the list with jinja and shows everything."
@app.route("/report")
def report():
    return render_template("report.html", vulnerabilitiesHtml=vulnerabilities)


if __name__ == "__main__":
    app.run(debug=True)
