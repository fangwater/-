import math
import random

from pyecharts import options as opts
from pyecharts.charts import Polar

def draw():
    c = (
        Polar()
        .add_schema(
            angleaxis_opts=opts.AngleAxisOpts(data=["Mozilla@1","Mozilla@5","Mozilla@10",
                                                    "Eclipse@1","Eclipse@5","Eclipse@10",
                                                    "FireFox@1","FireFox@5","FireFox@20",], type_="category")
        )
        .add("NextBug", [0.1093,0.2349,0.2908,0.1140,0.2499,0.3176,0,0,0], type_="bar", stack="Baseline")
        .add("Bert+XGboost", [0.301,0.515,0.713,0.283,0.487,0.625,0.293,0.572,0.742], type_="bar", stack="Our")
        .add("Word2vec+TF-IDF", [0.1691,0.3791,0.4867,0.1993,0.4342,0.5373,0.112,0.204,0.301],type_="bar", stack="ISSRE")
        .add("Word2vec+LDA+Deep-learning", [0,0,0,0,0,0,0.254,0.517,0.702], type_="bar", stack="ICSE")
        .set_global_opts(title_opts=opts.TitleOpts(title="模型效果对比-Polar"))
    )
    return c