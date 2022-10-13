from flask import Flask

app = Flask(__name__)

#Creating Home Page
@app.route("/")
def home():
  return "Smart Fashion Recommender System"

if __name__ == "__main__":
  app.run(debug=True)
