from typing import Optional

def get_full_name(first_name: str, last_name:str):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name


print(get_full_name('john', 'doe'))


def get_name_with_age(name:str, age: int):
    name_with_age = name + ' is this old: ' + str(age)
    return name_with_age


print(get_name_with_age('john', 37))


def get_items(
        item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes
):
    return item_a, item_b, item_c, item_d, item_e


print(get_items('string', 123, 1.5, True, bytes(1)))


def process_items(items: list[str]):
    for item in items:
        print(item.title())


process_items(['john', 'doe', 'joana', 'doe'])


def process_items_tuple_set(item_t: tuple[int, int, str], item_s: set[bytes]):
    return item_t, item_s


print(process_items_tuple_set((1, 2, 'john'), {b'foo', b'bar', b'baz'}))


def process_item_dict(prices: dict[str, float]):
    for k, v in prices.items():
        print(k, v)


process_item_dict({'TV': 200, 'Phone': 800})


def process_item_union(item: int | str):
    print(item)


process_item_union(123)
process_item_union('string')


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f'hey {name}')
    else:
        print('hello world')


say_hi('john')
say_hi()


def say_hi_pipe(name: str | None):
    print(f'hey {name}')


say_hi_pipe('joane')
say_hi_pipe(None)


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name

print(get_person_name(Person('sevastopol')))
