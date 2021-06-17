import sys
import requests
import webbrowser


def wrapper():
    try:
        a = 5 + 'string'
    except Exception:
        e = sys.exc_info()
        #print(e)
        e = str(e[0]).strip('<>').split()[1]
        return e
    else:
        print("No errors found")


search = wrapper()


def search_in_stockapi(search):
    url_uri = 'https://api.stackexchange.com/2.2/search'
    query_param = {'order': 'desc','sort': 'activity','tagged': 'TypeError','site': 'stackoverflow'}
    search_output = requests.get(url_uri,params=query_param)
    return search_output.json()


stock_api_output = search_in_stockapi(search)

link_list = []
for listed_items in stock_api_output['items']:
    if 'is_answered' in listed_items and listed_items['is_answered'] == True:
        link_list.append(listed_items['link'])
        webbrowser.open(listed_items['link'],new=0)
