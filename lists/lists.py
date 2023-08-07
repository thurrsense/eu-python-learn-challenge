class ListExercise:
    @staticmethod
    def max_val(input_list: list[int]) -> int:
        max = 0
        for el in input_list:
            if max < el:
                max = el
        return max

    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return input_list

        max_input = ListExercise.max_val(input_list)

        for index in range(len(input_list)):
            if input_list[index] > 0:
                input_list[index] = max_input

        return input_list

    @staticmethod
    def binary_search(input_list: list[int], left: int, right: int, query: int) -> int:
        if left <= right:

            mid = (left + right) // 2
            value = input_list[mid]

            if value == query:
                return mid
            elif value > query:
                return ListExercise.binary_search(input_list, left, mid - 1, query)
            else:
                return ListExercise.binary_search(input_list, mid + 1, right, query)

        return -1

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        left = 0
        right = len(input_list) - 1

        return ListExercise.binary_search(input_list, left, right, query)
