from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
# Required for cryptographically signing session cookies
app.secret_key = "super-secret-key-change-in-production"

# Hardcoded demo credentials
DEMO_USER = "admin"
DEMO_PASS = "secret123"


@app.route("/")
def index():
    # If the user is already authenticated, send them straight to dashboard
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("dashboard"))

    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == DEMO_USER and password == DEMO_PASS:
            # Store authentication state in the session
            session["username"] = username
            # Redirect to /dashboard on success
            return redirect(url_for("dashboard"))
        else:
            error = "Access denied. Please check your credentials."

    return render_template("login.html", error=error)


@app.route("/dashboard", methods=["GET"])
def dashboard():
    # Only accessible if session has a logged-in user; otherwise redirect to /
    if "username" not in session:
        return redirect(url_for("index"))

    return render_template("dashboard.html", username=session["username"])


@app.route("/logout")
def logout():
    # Clear the session data and bounce back to /
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
