def upper_str(user_str):
    """
    Возвращает строку сменив все элементы на заглавные
<<<<<<< HEAD
=======
     
>>>>>>> develop
    Parameters
    ----------
    user_str : str
        строка
<<<<<<< HEAD
=======
 
>>>>>>> develop
    Returns
    -------
    str
        строка с заглавными символами
    """
<<<<<<< HEAD
    user_str = user_str.upper()
    return user_str

def title_str(user_str):
    """
    Возвращает строку сменив первые буквы на заглавные
    Parameters
    ----------
    user_str : str
        строка
    Returns
    -------
    str
        строка с первыми заглавными символами
    """
    user_str = user_str.title()
    return user_str
=======
    
    user_str = user_str.upper()
    return user_str

>>>>>>> develop

def main():
# Ход основной программы
    print("Введите строку")
    user_input = input()
<<<<<<< HEAD
    print(f"Строка1: {upper_str(user_input)}")
    print(f"Строка2: {title_str(user_input)}")

if __name__ == '__main__':
    main()
=======
    user_input = upper_str(user_input)
    print(f"Строка: {user_input}")

if __name__ == '__main__':
    main()
>>>>>>> develop
