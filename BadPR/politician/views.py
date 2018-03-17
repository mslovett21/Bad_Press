from django.shortcuts import render

import numpy as np
import nvd3
# Create your views here.

def index(request):
    return render(
        request,
        'index.html',)
    """
    View function for home page of site.
    """

'''

#nvd3.ipynb.initialize_javascript(use_remote=True)
    np.random.seed(100)

    chart_type = 'discreteBarChart'
    chart = nvd3.discreteBarChart(name=chart_type, height=500, width=500)

    ydata = [float(x) for x in np.random.randn(10)]
    xdata = [int(x) for x in np.arange(10)]

    chart.add_serie(y=ydata, x=xdata)
    chart.buildhtml()
    #chart_html = chart.htmlcontent
    print(chart)

    color_list = ['orange', 'yellow', '#C5E946',
                  '#95b43f', 'red', '#FF2259',
                  '#F6A641', '#95b43f', '#FF2259', 'yellow']
    extra_serie = {"color_list": color_list}
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata, 'extra': extra_serie}
    charttype = "pieChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',context={'chart':chart},
'''
