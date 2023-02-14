import requests
PUBG_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzYmU1YTc1MC04ZDViLTAxM2ItMDFkMy01NzVjNzBiMzFiMzkiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjc2MjQ0NjYxLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Ii0zODkzZjVkMy04MzRjLTQyOWUtOWJlOC0zNTA3NGQ4NjAzMGQifQ.PdOUZA5qM_Ysa1nD2KWAg6UxIbOKHYbs6dF5iqrgyIs"

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message.startswith("!stat"):
        words = message.split()

        if len(words) < 2:
            return "Please provide a player name"

        player_name = words[1]

        headers = { "Authorization": "Bearer " + PUBG_API_KEY, "Accept": "application/vnd.api+json" }
        response = requests.get(f"https://api.pubg.com/shards/pc-na/players?filter[playerNames]={player_name}", headers=headers)
        print(response.text)
        data = response.json()

        if "erros" in data:
            return "Could not find player data"

        player = data["data"][0]
        name = player["attributes"]["name"]
        kills = player["attributes"]["stats"]["kills"]
        win_rate = player["attributes"]["stats"]["winPercent"]

        return str(f"{name} has {kills} kills and a win rate of {win_rate}%")

    else:
        return

    return 'I didn\'t understand what you wrote.  Try typing "!help".'