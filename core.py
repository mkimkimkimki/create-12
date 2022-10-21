from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def core():
    return render_template('index.html') 
     


if __name__ == "__main__":
    app.run()



# from login import login


# login(
#     9010128,
#     "Ram8181bigboss",
#     "BIGSolutions-LIVE1",
#     symbol,
#     option,
#     lots,
#     sl,
#     tp,
#     pip,
#     count,
# )

# login(63213069,"5zlqamlb","MetaQuotes-Demo")