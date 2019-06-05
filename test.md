雷达图下的多数集分析
我们采用雷达图更直观的表示不同模型在不同数据集上的效果分析，可以在展示自己模型的具体数值的同时，也可以展示出和其他模型的对比效果。
由于提升的模型的效果相对偏差并非很大，因此雷达图的对比部分是相对于baseline的提升量。
我们的BaseLine是Nextbug的检索效果，

Eclipse
0.1140
0.2499
0.3176

0.1691
0.3791
0.4867

Mozilla
0.1093
0.2349
0.2908

0.1993
0.4342
0.5373

FireFox
0.112
0.204
0.301

0.254
0.517
0.702


[1]可视化测试集的数据分析
我们可视化的对像是MozillaCore的分割出的测试集，在这一测试集中，一共包含了41014个提供测试的样本,为了可视化的效果，我们仅选取其中存在Bug Duplicted的样本，
也就是说在我们的抽样可视化中，我们忽略没有出现重复的样本，因为如果没有出现重复，就无法在可视化关系图当中体现。
经过统计，所有的出现了重复bug report一共4115个，再忽略其中的只有一个重复bug reoport的对象，还剩余的数据一共有1273个。我们将每个bug report所具有的重复数量做出可视化的结果如下:
可以看到，单个bug report的重复数量上下限在[0,120]之间。

[3]分层抽样的样本选取
为了针对我们recall@20，recall@10和recall@5三个模糊指标，我们选择作分层抽样来进行可视化，从以下区间
[2-5],[6-10],[10-15],[15-20],[20-Max]五个区间分别抽取10个bug issue。所有bug在这几个区间的分布如下：
虽然这样的抽样方式并不符合概率，但是为了实现一个较好的可视化结果就按照这样的方法抽样。

[4]样本的单点数据分析

我们对于所有的样本进行编号，针对五个区间，编码方式为A-E，每个区间的编号为1-10，我们使用3D柱状图的方式来展示单点的Recall数据：
在此仅展示一个切面图：
在整个图中，x轴为bug report对应的编码(区间号-序列号)，y轴为recall@k的k值，z轴为recall值
recall的计算在前文已有描述。

大致可以看到，recall大概在合理的区间波动，总体而言，和整体的样本估计相比，的指数明显低于平均的估计，因为从样本的
分布而言可以看出，用求均值的办法，无重复的bug report和有重复的bug report数量为9：1，差距较为悬殊，但由于指数设计的原因，
TP/P中，0重复bugTP=0，并不会导致recall被影响。




