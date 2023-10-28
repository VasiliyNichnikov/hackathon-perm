from enum import Enum


class TypeOfGarbage(Enum):
    Wood = 0,
    Glass = 1,
    Plastic = 2,
    Metal = 3,
    Unknown = 4


__garbage_by_type = {
    TypeOfGarbage.Wood: {
        "color": (217, 215, 90),
        "eng": "wood",
        "ru": "дерево"
    },
    TypeOfGarbage.Glass: {
        "color": (97, 97, 83),
        "eng": "glass",
        "ru": "стекло"
    },
    TypeOfGarbage.Plastic: {
        "color": (104, 207, 7),
        "eng": "plastic",
        "ru": "пластик"
    },
    TypeOfGarbage.Metal: {
        "color": (9, 4, 46),
        "eng": "metal",
        "ru": "металл"
    },
    TypeOfGarbage.Unknown: {
        "color": (222, 31, 144),
        "eng": "unknown",
        "ru": "неизвестный"
    }
}


def get_color_by_type(garbage_type: TypeOfGarbage) -> tuple[float]:
    global __garbage_by_type

    return __garbage_by_type[garbage_type]["color"]


def get_eng_class_by_type(garbage_type: TypeOfGarbage) -> str:
    global __garbage_by_type

    return __garbage_by_type[garbage_type]["eng"]


def get_ru_class_by_type(garbage_type: TypeOfGarbage) -> str:
    global __garbage_by_type

    return __garbage_by_type[garbage_type]["ru"]


def get_type_by_int_value(value: int) -> TypeOfGarbage:
    match int(value):
        case 0:
            type_of_garbage = TypeOfGarbage.Wood
        case 1:
            type_of_garbage = TypeOfGarbage.Glass
        case 2:
            type_of_garbage = TypeOfGarbage.Plastic
        case 3:
            type_of_garbage = TypeOfGarbage.Metal
        case _:
            print(f"GarbageSearch.Calculate: not found class with value: {value}")
            type_of_garbage = TypeOfGarbage.Unknown
    return type_of_garbage


def get_all_colors() -> tuple[tuple[float]]:
    global __garbage_by_type

    result = [get_color_by_type(type_of_garbage) for type_of_garbage in TypeOfGarbage]
    return tuple(result)


def get_all_eng_classes() -> tuple[str]:
    global __garbage_by_type

    result = [get_eng_class_by_type(type_of_garbage) for type_of_garbage in TypeOfGarbage]
    return tuple(result)


def get_all_ru_classes() -> tuple[str]:
    global __garbage_by_type

    result = [get_ru_class_by_type(type_of_garbage) for type_of_garbage in TypeOfGarbage]
    return tuple(result)
