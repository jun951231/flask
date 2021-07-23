def str_to_list(payload: str) -> []:
    return [i for i in payload()]

def reverse_str_list(ls: []) -> []:
    return []


def list_to_str(ls: []) -> str:
    return ''


if __name__ == '__main__':
    ls = str_to_list(input("Input"))
    revere_ls = reverse_str_list(ls)
    print(list_to_str(revere_ls))