import re


def is_valid_hooks(line: str) -> bool:
    hooks = {'{': '}', "(": ')', "[": ']'}
    find_hooks: list[str] = re.findall('[\[\]{}()]', line)
    if find_hooks and len(find_hooks) % 2 == 0:
        start = 0
        end = len(find_hooks) - 1
        while start < end:
            if find_hooks[start] in hooks:
                if hooks[find_hooks[start]] != find_hooks[end]:
                    return False
                start += 1
                end -= 1
            else:
                return False
    else:
        return False
    return True


if __name__ == '__main__':
    assert is_valid_hooks('[ ]') is True
    assert is_valid_hooks('{ ( { ) } }') is False
    assert is_valid_hooks('[{((()))}]') is True
    assert is_valid_hooks('[{((()))}}') is False
    assert is_valid_hooks('[A, B, {C:[1, 2]}]') is True
    assert is_valid_hooks('[A, B, {C:[1, 2}]') is False
