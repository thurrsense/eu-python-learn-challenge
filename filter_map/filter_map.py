from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = [func(el)[1] for el in input_array if func(el)[0] is not False]
        return result
