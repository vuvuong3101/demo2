from flask import *
import mlab
from models.link_item import LinkItem
from models.button_item import ButtonItem
from random import randint
app = Flask(__name__)

mlab.connect()

@app.route('/')
def home():
    return redirect('/main')

link_item = []
index_button = ['music','movie','book','clip','special']
button = {}

def add_data():
    count_link = -1
    count_index_button = -1

    myfile = open("link_item.txt",'r', encoding='utf-16')

    while True:
        theline = myfile.readline()

        if len(theline) == 0:
            break
        if theline[0] == '-':
            count_index_button += 1
            button[index_button[count_index_button]] = []
        else:
            count_link += 1
            button[index_button[count_index_button]].append(count_link)
            link_item.append(theline)

    myfile.close()
#
# add_data()
#
# link = LinkItem()
# link.item = link_item
# link.save()
#
# button_ = ButtonItem()
# button_.music = button['music']
# button_.movie = button['movie']
# button_.book = button['book']
# button_.clip = button['clip']
# button_.special = button['special']
# button_.save()

@app.route('/home')
def main():
    # print(LinkItem.objects()[0].item)
    # print(ButtonItem.objects()[0].to_dict())
    index_site_random = randint(0, len(LinkItem.objects()[0].item) - 1)
    site_random_all = link_item = LinkItem.objects()[0].item[index_site_random]
    return render_template('main.html', link_item=LinkItem.objects()[0].item, button=ButtonItem.objects()[0].to_dict(),
                           first_time=True, site_random_all=site_random_all)

@app.route('/main')
def main2():
    return  render_template('index.html')
if __name__ == '__main__':
    app.run()