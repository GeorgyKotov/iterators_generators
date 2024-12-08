import types


def flat_generator(list_of_lists):
    main_list_pointer = 0
    nested_list_pointer = 0
    while main_list_pointer < len(list_of_lists):
        yield list_of_lists[main_list_pointer][nested_list_pointer]
        nested_list_pointer += 1
        if nested_list_pointer >= len(list_of_lists[main_list_pointer]):
            main_list_pointer += 1
            nested_list_pointer = 0


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()