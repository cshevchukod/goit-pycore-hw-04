# Імпортуємо головну функцію пакета
from .cli import get_cats_info

# __all__ показує, що саме буде доступним при імпорті пакета
__all__ = ["get_cats_info"]