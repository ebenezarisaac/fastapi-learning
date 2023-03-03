from typing import List, Tuple, Set, Dict, Optional

def get_full_name(first_name: str, last_name: str):
    full_name = first_name + "" + last_name
    return full_name

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age

def process_items(items: List[str]):
    for item in items:
        print(item)

def process_moreitems(items_t: Tuple[int, int, str], item_s: Set[bytes]):
    return items_t, item_s

def process_dictitems(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print('Hello world')

class Person:
    def __init__(self, name: str) -> None:
        self.name = name
    
def get_person_name(one_person: Person):
    return one_person.name




