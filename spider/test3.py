#coding=utf-8
from matplotlib import pyplot

#绘制散点图
def drawScatter(heights, weights):
    #创建散点图
    #第一个参数为点的横坐标
    #第二个参数为点的纵坐标
    pyplot.scatter(heights, weights)
    pyplot.xlabel('Heights')
    pyplot.ylabel('Weights')
    pyplot.title('Heights & Weights Of Male Students')
    pyplot.show()


heights=(1.75,1.55,2,1.8,1.66,1.55,1.77,1.85)
weights=(50,45,75,70,51,40,55,60)
drawScatter(heights, weights)