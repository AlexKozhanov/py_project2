def upper_str(user_str):
    user_str = user_str.upper()
    return user_str


def main():
    print("Введите строку")
    user_input = input()
    user_input = upper_str(user_input)
    print(f"Строка: {user_input}")

if __name__ == '__main__':
    main()
