from common.io_utils import read_lines
from .parse import parse_cats

def get_cats_info(path: str) -> list[dict]:
    #Зчитує файл → парсить у словники → повертає список котів.

    lines = read_lines(path)
    if not lines:
        return []
    return parse_cats(lines)
