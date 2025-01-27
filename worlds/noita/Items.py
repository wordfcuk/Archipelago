import itertools
from collections import Counter
from typing import Dict, List, NamedTuple, Optional, Set

from BaseClasses import Item, ItemClassification, MultiWorld
from .Options import BossesAsChecks, VictoryCondition


class ItemData(NamedTuple):
    code: Optional[int]
    group: str
    classification: ItemClassification = ItemClassification.progression
    required_num: int = 0


class NoitaItem(Item):
    game: str = "Noita"


def create_item(player: int, name: str) -> Item:
    item_data = item_table[name]
    return NoitaItem(name, item_data.classification, item_data.code, player)


def create_fixed_item_pool() -> List[str]:
    required_items: Dict[str, int] = {name: data.required_num for name, data in item_table.items()}
    return list(Counter(required_items).elements())


def create_orb_items(victory_condition: VictoryCondition) -> List[str]:
    orb_count = 0
    if victory_condition == VictoryCondition.option_pure_ending:
        orb_count = 11
    elif victory_condition == VictoryCondition.option_peaceful_ending:
        orb_count = 33
    return ["Orb" for _ in range(orb_count)]


def create_spatial_awareness_item(bosses_as_checks: BossesAsChecks) -> List[str]:
    return ["Spatial Awareness Perk"] if bosses_as_checks.value >= BossesAsChecks.option_all_bosses else []


def create_kantele(victory_condition: VictoryCondition) -> List[str]:
    return ["Kantele"] if victory_condition.value >= VictoryCondition.option_pure_ending else []


def create_random_items(multiworld: MultiWorld, player: int, random_count: int) -> List[str]:
    filler_pool = filler_weights.copy()
    if multiworld.bad_effects[player].value == 0:
        del filler_pool["Trap"]

    return multiworld.random.choices(
        population=list(filler_pool.keys()),
        weights=list(filler_pool.values()),
        k=random_count
    )


def create_all_items(multiworld: MultiWorld, player: int) -> None:
    sum_locations = len(multiworld.get_unfilled_locations(player))

    itempool = (
        create_fixed_item_pool()
        + create_orb_items(multiworld.victory_condition[player])
        + create_spatial_awareness_item(multiworld.bosses_as_checks[player])
        + create_kantele(multiworld.victory_condition[player])
    )

    random_count = sum_locations - len(itempool)
    itempool += create_random_items(multiworld, player, random_count)

    multiworld.itempool += [create_item(player, name) for name in itempool]


# 110000 - 110032
item_table: Dict[str, ItemData] = {
    "Trap":                                 ItemData(110000, "Traps", ItemClassification.trap),
    "Extra Max HP":                         ItemData(110001, "Pickups", ItemClassification.useful),
    "Spell Refresher":                      ItemData(110002, "Pickups", ItemClassification.filler),
    "Potion":                               ItemData(110003, "Items", ItemClassification.filler),
    "Gold (200)":                           ItemData(110004, "Gold", ItemClassification.filler),
    "Gold (1000)":                          ItemData(110005, "Gold", ItemClassification.filler),
    "Wand (Tier 1)":                        ItemData(110006, "Wands", ItemClassification.useful),
    "Wand (Tier 2)":                        ItemData(110007, "Wands", ItemClassification.useful),
    "Wand (Tier 3)":                        ItemData(110008, "Wands", ItemClassification.useful),
    "Wand (Tier 4)":                        ItemData(110009, "Wands", ItemClassification.useful),
    "Wand (Tier 5)":                        ItemData(110010, "Wands", ItemClassification.useful),
    "Wand (Tier 6)":                        ItemData(110011, "Wands", ItemClassification.useful),
    "Kantele":                              ItemData(110012, "Wands", ItemClassification.useful),
    "Fire Immunity Perk":                   ItemData(110013, "Perks", ItemClassification.progression, 1),
    "Toxic Immunity Perk":                  ItemData(110014, "Perks", ItemClassification.progression, 1),
    "Explosion Immunity Perk":              ItemData(110015, "Perks", ItemClassification.progression, 1),
    "Melee Immunity Perk":                  ItemData(110016, "Perks", ItemClassification.progression, 1),
    "Electricity Immunity Perk":            ItemData(110017, "Perks", ItemClassification.progression, 1),
    "Tinker with Wands Everywhere Perk":    ItemData(110018, "Perks", ItemClassification.progression, 1),
    "All-Seeing Eye Perk":                  ItemData(110019, "Perks", ItemClassification.progression, 1),
    "Spatial Awareness Perk":               ItemData(110020, "Perks", ItemClassification.progression),
    "Extra Life Perk":                      ItemData(110021, "Repeatable Perks", ItemClassification.useful),
    "Orb":                                  ItemData(110022, "Orbs", ItemClassification.progression_skip_balancing),
    "Random Potion":                        ItemData(110023, "Items", ItemClassification.filler),
    "Secret Potion":                        ItemData(110024, "Items", ItemClassification.filler),
    "Powder Pouch":                         ItemData(110025, "Items", ItemClassification.filler),
    "Chaos Die":                            ItemData(110026, "Items", ItemClassification.filler),
    "Greed Die":                            ItemData(110027, "Items", ItemClassification.filler),
    "Kammi":                                ItemData(110028, "Items", ItemClassification.filler),
    "Refreshing Gourd":                     ItemData(110029, "Items", ItemClassification.filler),
    "Sädekivi":                             ItemData(110030, "Items", ItemClassification.filler),
    "Broken Wand":                          ItemData(110031, "Items", ItemClassification.filler),

}

filler_weights: Dict[str, int] = {
    "Trap":              15,
    "Extra Max HP":      25,
    "Spell Refresher":   20,
    "Potion":            40,
    "Gold (200)":        15,
    "Gold (1000)":       6,
    "Wand (Tier 1)":     10,
    "Wand (Tier 2)":     8,
    "Wand (Tier 3)":     7,
    "Wand (Tier 4)":     6,
    "Wand (Tier 5)":     5,
    "Wand (Tier 6)":     4,
    "Extra Life Perk":   10,
    "Random Potion":     9,
    "Secret Potion":     10,
    "Powder Pouch":      10,
    "Chaos Die":         4,
    "Greed Die":         4,
    "Kammi":             4,
    "Refreshing Gourd":  4,
    "Sädekivi":          3,
    "Broken Wand":       10,
}


# These helper functions make the comprehensions below more readable
def get_item_group(item_name: str) -> str:
    return item_table[item_name].group


def item_is_filler(item_name: str) -> bool:
    return item_table[item_name].classification == ItemClassification.filler


def item_is_perk(item_name: str) -> bool:
    return item_table[item_name].group == "Perks"


filler_items: List[str] = list(filter(item_is_filler, item_table.keys()))
item_name_to_id: Dict[str, int] = {name: data.code for name, data in item_table.items()}

item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in itertools.groupby(item_table, get_item_group)
}
