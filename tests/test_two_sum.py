from hashing.two_sum import Solution


def test_two_sum():
    solution = Solution()

    assert solution.twoSum([2, 7, 9, 3], 10) == [1, 3]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([1, 2, 3], 7) == []
