from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def home():
    return "Hello flask"

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        message=request.form.get("message")
        return f"Thank you{name} for the message {message} we will be contacting you at{email}"
    return render_template('contact_form.html')

if __name__=='__main__':
    app.run(debug=True)