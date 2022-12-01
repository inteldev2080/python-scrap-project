import re
from requests_html import HTMLSession

# async def hello():
#     print("hello ym")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


def scrapWebsite(url):
    collect_objs = []
    session = HTMLSession()
    data_request = session.get(url)

    required_data = data_request.html.find(".sc-f7a61dda-2")

    required_tbody = required_data[0].find('tbody')

    all_rows = required_tbody[0].find('tr')

    # Note: after 10 rows the website is using javascript functions for loading data on the website
    # which python couldn't scrap. As the user scrolls in the website, the javascript functions populates 
    # the data (which was earlier blank), HINT: try disabling javascript in webpage to spot the 
    # missing data. Thats why im rendering only 10 rows

    for i in range(0, 10): 
        each_row = all_rows[i]
        table_datas = each_row.find('td')

        name = re.sub(r"[$,%]", "", table_datas[2].text)
        price = re.sub(r"[$,%]", "", table_datas[3].text)
        perhour = re.sub(r"[$,%]", "", table_datas[4].text)
        day = re.sub(r"[$,%]", "", table_datas[5].text)
        week = re.sub(r"[$,%]", "", table_datas[6].text)
        marketcap = re.sub(r"[$,%]", "", table_datas[7].text)
        volume = re.sub(r"[$,%]", "", table_datas[8].text)
        cirulating_supply = re.sub(r"[$,%]", "", table_datas[9].text)

        myobj = {
            "name": re.sub(r"[\n]", " ", name),
            "price": price,
            "perhour": perhour,
            "day": day,
            "week": week,
            "marketcap": marketcap.split("B")[1],
            "volume": volume.split("\n")[0],
            "cirulating_supply": cirulating_supply,
        }

        collect_objs.append(myobj)

        # print("\n------------\n")

    # return data_request.status_code
    return collect_objs


# scrapWebsite()
