import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Якщо номер починається з '+', перевіряємо код країни
    if cleaned_number.startswith('+'):
        if not cleaned_number.startswith('+38'):  # Якщо номер не з кодом України
            return cleaned_number
    else:
        # Якщо номер без '+', перевіряємо на наявність українського коду
        if cleaned_number.startswith('380'):
            return f'+{cleaned_number}'
        else:
            # Додаємо код України
            return f'+38{cleaned_number}'
    
    return cleaned_number
