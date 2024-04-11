def upper_str(user_str):
    """
    Возвращает строку сменив все элементы на заглавные
     
    Parameters
    ----------
    user_str : str
        строка
 
    Returns
    -------
    str
        строка с заглавными символами
    """
    
    user_str = user_str.upper()
    return user_str


def main():
# Ход основной программы
    print("Введите строку")
    user_input = input()
    user_input = upper_str(user_input)
    print(f"Строка: {user_input}")

if __name__ == '__main__':
    main()
