def check_issn_key(issn_id: str) -> bool:
    """
    :param issn_id:
        The 9th first number of the issn id as a string

    :return bool:
        Whether the issn key is valid.
    """

    issn_id = issn_id.replace('-', '')

    r = sum(
        (int(x) if x.isdigit() else 10) * (c + 2)
        for c, x in enumerate(issn_id[-2::-1])
    ) % 11

    return ("x" if r == 10 else str(r)) == issn_id[-1]


if __name__ == '__main__':
    print(check_issn_key('0000-0000'))
    print(check_issn_key('1234-4321'))
    print(check_issn_key('7185-0456'))
