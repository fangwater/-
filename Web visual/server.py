from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
import Model_polar
import Word_cloud
import Recall3D
import Simheat
import Rec_graph
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))
app = Flask(__name__, static_folder="templates")




@app.route("/bug-vis/polar")
def polar():
    c = Model_polar.draw()
    return Markup(c.render_embed())

@app.route("/bug-vis/word-cloud")
def wordcloud():
    c = Word_cloud.draw()
    return Markup(c.render_embed())

@app.route("/bug-vis/sim-heat")
def simheatmap():
    c = Simheat.draw()
    return Markup(c.render_embed())

@app.route("/bug-vis/sample-recall")
def Recall3dbar():
    c = Recall3D.draw()
    return Markup(c.render_embed())

@app.route('/bug-vis/<order>', methods=['GET','POST'])
def recgraph(order):
    c = Rec_graph.draw(order)
    return Markup(c.render_embed())

if __name__ == "__main__":
    app.run()