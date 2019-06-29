from datetime import date, datetime

import fire

from carriers.eurolines import get_connections as get_eurolines_connections
from carriers.cd import get_connections as get_cd_connections


def get_connections(source: str, destination: str, departure_date: str):
    departure_date = datetime.strptime(departure_date, "%Y-%m-%d").date()
    results = []
    results.extend(get_eurolines_connections(source, destination, departure_date))
    results.extend(get_cd_connections(source, destination, departure_date))
    return results


if __name__ == "__main__":
    fire.Fire(get_connections)

# print(get_eurolines_connections("Praha", "Brno", date(2019, 7, 2)))
# print(get_cd_connections("Praha hl.n.", "Brno dolní nádraží", date(2019, 7, 29)))
