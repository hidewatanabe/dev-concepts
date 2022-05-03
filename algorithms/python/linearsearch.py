# LINEAR SEARCH
## It's a search based in a sequential search of elements in a vector or a list.
## Complexity: O(n)

def linear_search(list, element):
    for i in range(len(list)):
        if list[i] == element:
            print(f"Element found: {element}")
            return True
    print(f"Element not found")
    return False


if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9,10]
    element = 7
    result = linear_search(list, element)
    print(str(result))