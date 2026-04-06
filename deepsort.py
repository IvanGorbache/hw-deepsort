import collections

#t
def deep_sorted(x: any) -> str:
    if isinstance(x, dict):
        sorted_items = []
        for key in sorted(x.keys()):
            sorted_items.append("\"" + key + "\": " + deep_sorted(x[key]))
        return "{" + ", ".join(sorted_items) + "}"
    elif isinstance(x, (list, tuple, set)):
        container = {list: "[]", tuple: "()", set: "{}"}
        return container[type(x)][0] + ", ".join(sorted([deep_sorted(y) for y in x])) + container[type(x)][1]
    return str(x)


if __name__ == '__main__':
    # x=eval(input())
    # print(deep_sorted(x))
    import doctest

    print(doctest.testmod())
