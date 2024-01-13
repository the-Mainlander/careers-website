from flask import Flask, render_template, jsonify

app=Flask(__name__)

JOBS=[
  {
    "id":1,
    "title":"Data Analyst",
    "location":"Hybrid",
    "salary":"Rs. 10,00,000"
  },
  {
    "id":2,
    "title":"Data Scientist",
    "location":"Bengaluru",
    "salary":"Rs. 12,00,000"
  },
  {
    "id":3,
    "title":"Frontend Engineer",
    "location":"Remote",
    "salary":"Rs. 13,00,000"
  },
  {
    "id":4,
    "title":"Backend Engineer",
    "location":"Bengaluru",
    "salary":"Rs. 17,00,000"
  },
  {
    "id":5,
    "title":"Embedded Systems Engineer",
    "location":"Bengaluru",
    "salary":"Rs. 25,00,000"
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,
                        company_name='Deus')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)