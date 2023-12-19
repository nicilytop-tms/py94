from requests import get
from hw_18_requests.user import User
from hw_18_requests.country import Country

url = 'http://185.225.232.111:8000/user/'

users = get(url).json()
user_ids = [u['id'] for u in users]


users_instances = []
for user_id in user_ids:
    user_json = get(f'{url}{user_id}/').json()
    users_instances.append(
        User(**user_json)
    )


for user in users_instances:
    countries_json = get(f'{url}{user._id}/country/').json()

    countries = []
    for country_json in countries_json:
        country = Country(id=country_json["id"], name=country_json["name"])
        countries.append(country)

    countries = [Country(**params) for params in countries_json]
    user.countries = countries