def main() -> list[int]:
    num: list[int] = list(map(int, input().split()))
    return num


if __name__ == "__main__":
    result: list[int] = main()
    print(*result)

    