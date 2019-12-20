import pandas as pd
import matplotlib.pyplot as plt
from yattag import Doc
import datetime

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)


def autolabelh(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(width * 1.05, rect.get_y() + rect.get_height() / 2., '%d' % int(width), ha='left', va='center', fontdict={'size': 10})


def test_create_locust_chart():
    current_datetime = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    data_csv = pd.read_csv("test_result_response_times.csv", sep=',')
    sorted_data = data_csv.sort_values(by=['Median response time'])
    name, median_response_time = sorted_data['Name'], sorted_data['Median response time']
    bar = plt.barh(range(len(median_response_time)), median_response_time, align='edge', alpha=0.7)
    plt.yticks(range(len(name)), name, ha='right', va='bottom', size='small')
    plt.subplots_adjust(left=0.3)
    plt.grid(True)
    autolabelh(bar)
    title = current_datetime + ' Load Test Result'
    plt.suptitle(title, fontsize=12, weight='bold')
    plt.xlabel('Median Response Time(ms)')
    plt.savefig('locust_report.png', bbox_inches='tight')


def test_create_html_report():
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('body', id='img'):
            with tag('p'):
                doc.stag('img', src='locust_report.png')
    output = open("load.html", 'w')
    output.write(doc.getvalue())
    output.close()