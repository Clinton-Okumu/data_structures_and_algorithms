def closestNumber(n, m):
    q = n // m

    case1 = m * q
    case2 = m * (q + 1)
    case3 = m * (q - 1)

    cases = [case1, case2, case3]

    closest = min(cases, key=lambda x: (abs(n - x), -abs(x)))
    return closest
