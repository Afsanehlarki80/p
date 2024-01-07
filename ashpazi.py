import random

# ایجاد یک لیست از مواد اولیه
ingredients = ["گوشت چرخ کرده", "پیاز", "سیر", "زردچوبه", "نمک و فلفل", "روغن زیتون"]

# انتخاب تصادفی چند مورد از مواد اولیه
selected_ingredients = random.sample(ingredients, k=3)

# چاپ کردن مواد اولیه انتخاب شده
print("مواد اولیه برای پروژه اشپزی:")
for ingredient in selected_ingredients:
    print(ingredient)