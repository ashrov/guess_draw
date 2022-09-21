"""
Все координаты  передаются в формате (x;y)
"""


def send_position_command(coords: tuple | list) -> str:
    com = f"({coords[0]};{coords[1]})" if len(coords) == 2 else ""
    return com



