#!/usr/bin/env python3
"""
Range Checker Script
Проверяет, попадают ли числа в заданные диапазоны.

Использование:
  python3 check_range.py 75 70 80 120 110 130 85 80 90

Формат: value min max value min max ...
(тройки чисел: значение, минимум диапазона, максимум диапазона)
"""

import sys

def check_ranges():
    """Проверяет тройки чисел на попадание в диапазон"""
    
    # Проверяем аргументы командной строки
    args = sys.argv[1:]  # убираем имя скрипта
    
    if len(args) == 0:
        print("❌ Ошибка: нужно указать числа для проверки")
        print("📖 Использование: python3 check_range.py 75 70 80 120 110 130")
        print("📖 Формат: значение мин макс значение мин макс ...")
        return
    
    if len(args) % 3 != 0:
        print("❌ Ошибка: количество чисел должно быть кратно 3")
        print("📖 Каждая тройка: значение минимум максимум")
        return
    
    # Обрабатываем тройки чисел
    print("🔍 Проверка диапазонов:")
    print("=" * 50)
    
    try:
        for i in range(0, len(args), 3):
            value = float(args[i])
            min_val = float(args[i + 1])
            max_val = float(args[i + 2])
            
            # Проверяем диапазон
            is_in_range = min_val <= value <= max_val
            status = "✅ В диапазоне" if is_in_range else "❌ Вне диапазона"
            
            print(f"{value:8.1f} | [{min_val:6.1f} - {max_val:6.1f}] | {status}")
            
    except ValueError:
        print("❌ Ошибка: все аргументы должны быть числами")
        return
    
    print("=" * 50)

if __name__ == "__main__":
    check_ranges() 