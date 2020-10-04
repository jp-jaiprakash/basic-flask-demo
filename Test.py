from flask import Flask

app = Flask(__name__)
import json
import re


def readJson():
  with open('testme.json') as f:
    data = json.load(f)
  return data

@app.route("/")
def hello():
  list_factor = readJson()
  # adding "n" and placed at the top
  html = "<h1> Values are</h1>" + "\n" + "<ul>"

  pat = re.compile(r"\bcolor:\w*\b")
  f1 = open("html1.txt", "r")
  color1 = f1.readline()
  co1 = (pat.search(color1).group()).split(":")[1]

  f2 = open("html2.txt", "r")
  color2 = f2.readline()
  co2 = (pat.search(color2).group()).split(":")[1]

  i =0
  # make a <li> item for every output (factor)
  for f in list_factor:
    if i%2 == 0:
      html += "<li style='color: "+co1+";'>" + f['name'] + "</li>" + "\n"
    else:
      html += "<li style='color: "+co2+";'>" + f['name'] + "</li>" + "\n"
    i = i+1

  html += "</ul> </body>"  # closes tag at the end
  f1.close()
  f2.close()
  return html


if __name__ == '__main__':
  app.run(host='0.0.0.0')