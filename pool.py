import json

POOL_FILE = "cards_pool.json"


def load_pool():

    with open(POOL_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_card_by_id_set(card_id, card_set):

    pool = load_pool()

    for card in pool["cards"]:
        if card["id"] == card_id and card["set"] == card_set:
            return card