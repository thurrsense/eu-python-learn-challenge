from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []
        for el in input_array:
            flag, item = func(el)
            if flag is not False:
                result.append(item)
        return result
