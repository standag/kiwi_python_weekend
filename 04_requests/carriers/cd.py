from datetime import date, datetime
from typing import List

from requests_html import HTMLSession

session = HTMLSession()
BASE_URL = "https://m.cd.cz"


def get_station_code(station: str) -> str:
    url = "https://m.cd.cz/spojeni/ogres/AJAX/SearchTimetableObjects"
    params = {
        "timestamp": int(datetime.now().timestamp() * 1000),
        "prefixText": station,
        "count": 1,
    }
    return session.get(url, params=params).json()[0]["Value"]


def get_price(link: str, session: HTMLSession) -> str:
    # get to eshop
    detail_response = session.get(f"{BASE_URL}{link}")
    eshop_link = next(
        link for link in detail_response.html.links if link.startswith("/eshop/start")
    )
    # select second class
    response = session.get(f"{BASE_URL}{eshop_link}")
    form_data = {"DocTypeClass": 2, "DocType": 1, "cmdContinue": "Pokračovat"}
    response = session.post(response.url, data=form_data)
    # select one-way ticket
    no_return_link = next(
        link for link in response.html.links if link.startswith("/eshop/startnoback")
    )
    response = session.get(f"{BASE_URL}{no_return_link}")
    # select one regular passenger
    form_data = {
        "psgcount1": 1,
        "psgagecat1": "dospělý (26-64 let)",
        "psgid1": 600,
        "psgcard1": "(žádný)",
        "isBack": "true",
        "cmdContinue": "Pokračovat",
    }
    response = session.post(response.url, data=form_data)
    # price to select?
    prices = response.html.find(".ticket-desc-price", first=True)
    if prices:
        return prices.text
    return response.html.find("form p.green", first=True).text


def get_connections(source: str, destination: str, departure_date: date) -> List:
    source_code = get_station_code(source)
    destination_code = get_station_code(destination)
    url = f"{BASE_URL}/spojeni/"
    session.get(url)  # try to get cookies
    data = {
        "FROM_0t": source,
        "FROM_0h": f"{source}%{source_code}",
        "TO_0t": destination,
        "TO_0h": f"{destination}%{destination_code}",
        "VIA_0h": "",
        "VIA_1h": "",
        "VIA_2h": "",
        "form-time": "00:00",
        "form-date": departure_date.strftime("%Y-%m-%d"),
        "deparr": True,
        "cmdSearch": "Hledat",
    }
    response = session.post(url, data=data).html
    results = iter(response.find("a.results"))
    connections = []
    for result in results:
        departure_time, arrival_time, _ = (
            time_span.text for time_span in result.find("span span")
        )
        departure_time = datetime.strptime(departure_time, "%H:%M").time()
        arrival_time = datetime.strptime(arrival_time, "%H:%M").time()
        source_, destination_ = (
            strong_span.text for strong_span in result.find("span strong")
        )
        link = result.attrs["href"]
        price = get_price(link, session)
        connections.append(
            {
                "source": source_,
                "departure_datetime": datetime.combine(departure_date, departure_time),
                "destination": destination_,
                "arrival_datetime": datetime.combine(departure_date, arrival_time),
                "price": price,
                "type": "train",
                "carrier": "CD",
            }
        )
    return connections

