from datetime import date
from requests_html import HTMLSession

session = HTMLSession()


def get_city_id(city: str, type: str) -> int:
    url = f"https://back.eurolines.eu/euroline_api/{type}s"
    params = {"q": city, "favorite": "true"}
    return session.get(url, params=params).json()[0]["id"]


def get_connections(source: str, destination: str, departure_date: date):
    source_id = get_city_id(source, type="origin")
    destination_id = get_city_id(destination, type="destination")
    url = "https://back.eurolines.eu/euroline_api/journeys"
    args = {
        "date": departure_date.strftime("%Y-%m-%d"),
        "flexibility": 0,
        "currency": "CURRENCY.CZK",
        "passengers": "BONUS_SCHEME_GROUP.ADULT,1",
        "promoCode": "",
        "direct": "false",
        "originCity": source_id,
        "destinationCity": destination_id,
    }
    connections = session.get(url, params=args).json()
    breakpoint()
    return [
        {
            "source": connection["legs"][0]["origin"]["name"],
            "departure_datetime": connection["legs"][0]["departure"],
            "destination": connection["legs"][0]["destination"]["name"],
            "arrival_datetime": connection["legs"][0]["arrival"],
            "price": connection["price"],
            "type": "train",
            "carrier": "CD",
        }
        for connection in connections
    ]
