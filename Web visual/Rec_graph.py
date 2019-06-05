import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Graph

def make_edges(i):
    E = pd.read_csv("Graph/e"+str(i)+".csv")
    Data = E.values.tolist()
    edges = []
    for k in Data:
        edge = {}
        edge["From"] = k[0]
        edge["To"] = k[1]
        edges.append(edge)
    return edges
def make_nodes(i):
    N = pd.read_csv("Graph/g"+str(i)+".csv")
    Data = N.values.tolist()
    nodes = []
    for k in Data:
        node = {}
        node["color"] = k[0]
        node["id"] = k[1]
        node["label"] = k[2]
        node["shape"] = k[3]
        node["size"] = k[4]
        node["value"] = k[5]
        nodes.append(node)
    return nodes

def draw(order):
    NN = make_nodes(order)
    EE = make_edges(order)
    nodes = [
        {
            "id": str(node["id"]),
            "symbol":node["shape"],
            "name": "{Compment:"+node["label"]+"},      {"+"Title:"+node["value"]+"}",
            "symbolSize": node["size"],
            "itemStyle": {"normal": {"color": node["color"]}},
            "value":node["id"],
        }
        for node in NN
    ]

    edges = [
        {"source": str(edge["From"]), "target": str(edge["To"])} for edge in EE
    ]
    
    c = (
        Graph(init_opts=opts.InitOpts())
        .add(
            "Bug-Inf",
            nodes=nodes,
            links=edges,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Recommond System Vis"))
    )
    return c


