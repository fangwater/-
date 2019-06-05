import random
from pyecharts import options as opts
from pyecharts.charts import Bar3D, Page
def draw():
    code = []
    for ch in ["A","B","C","D","E"]:
        for i in range(1,11):
            code.append(ch+"-"+str(i))
    k_value = ["recall@1","recall@5","recall@10"]
    recall_value = []
    plot_data = []
    for i in range(len(code)):
        for j in range(len(k_value)):
            plot_data.append((code[i],k_value[j],random.uniform(0,1)))
    c = (
        Bar3D()
        .add(
            "Sample",
            plot_data,
            xaxis3d_opts=opts.Axis3DOpts(code, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(k_value, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=1),
            title_opts=opts.TitleOpts(title="50 Sample Recall"),
        )
    )
    return c