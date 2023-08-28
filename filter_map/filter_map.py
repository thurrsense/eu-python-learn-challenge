from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []
        for el in input_array:
            tmp = func(el)
            if tmp[0] is not False:
                result.append(tmp[1])
        return result
