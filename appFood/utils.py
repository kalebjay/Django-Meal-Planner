#Utils - extra space for functions

# This function sorts the query into a list that can
# be fed into the pie data for visual representation.
# Pie charts are only effective if there are no more
# than 6 categories so this function sorts the 12 used
# in the model into the 6 used for the pie chart.
def sortPieData(queryList):
    data = []
    americaCount = 0
    italianCount = 0
    mexicanCount = 0
    asianCount = 0
    dessertCount = 0
    otherCount = 0
    for c in queryList:
        if c.get('category_name') == 1:
            americaCount += c.get('count')
        elif c.get('category_name') == 2:
            americaCount += c.get('count')
        elif c.get('category_name') == 3:
            otherCount += c.get('count')
        elif c.get('category_name') == 4:
            otherCount += c.get('count')
        elif c.get('category_name') == 5:
            americaCount += c.get('count')
        elif c.get('category_name') == 6:
            italianCount += c.get('count')
        elif c.get('category_name') == 7:
            mexicanCount += c.get('count')
        elif c.get('category_name') == 8:
            asianCount += c.get('count')
        elif c.get('category_name') == 9:
            otherCount += c.get('count')
        elif c.get('category_name') == 10:
            otherCount += c.get('count')
        elif c.get('category_name') == 11:
            dessertCount += c.get('count')
        elif c.get('category_name') == 12:
            otherCount += c.get('count')

    data = [americaCount, italianCount, mexicanCount, asianCount, dessertCount, otherCount]
    return data
