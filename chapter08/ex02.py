
def find(string: str, letter: str) -> int:
    """Возвращает индекс вхождения символа `letter` в строку `string`.

    Возвращает -1, если такого вхождения нет.
   >>> find('abc', 'b')
   1
   >>> find('abc', 'c')
   3
   >>> find('abc', 'd')
   -1
    """
    index = 0
    while index < len(string):
        if string[index] == letter:
            return index
        index = index + 1
    return -1

result = find("rgvrbr","v")
print(result)
import doctest
doctest.testmod()
