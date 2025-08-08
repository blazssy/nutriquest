# nutrition_tracker/utils/meal_pairing.py

def find_meal_pairs(food_items, target, margin=50):
    food_items.sort(key=lambda x: x['calories'])
    left, right = 0, len(food_items) - 1
    pairs = []

    while left < right:
        total = food_items[left]['calories'] + food_items[right]['calories']
        if abs(total - target) <= margin:
            pairs.append((food_items[left], food_items[right]))
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1

    return pairs