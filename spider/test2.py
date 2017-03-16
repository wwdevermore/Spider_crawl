from matplotlib import pyplot


def drawBox(heights):

    pyplot.boxplot([heights], labels=['Heights'])
    pyplot.title('Heights Of Male Students')
    pyplot.show()
heights=(1.75,1.55,2,1.8,1.66,1.55,1.77,1.85)
drawBox(heights)
