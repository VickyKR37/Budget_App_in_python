from applications.budget_app.classes import Budget


def test_budget():
    food_example = Budget(100, "food_example")
    assert food_example.amount == 100
    food_example.withdraw(50)
    assert food_example.amount == 50
    food_example.deposit(20)
    assert food_example.amount == 70
    assert str(food_example) == "70"

def test_budget2():
    clothes_example = Budget(1000, "clothes_example")
    assert clothes_example.amount == 1000
    clothes_example.withdraw(300)
    assert clothes_example.amount == 700
    clothes_example.deposit(200)
    assert clothes_example.amount == 900
    assert str(clothes_example) == "900"

def test_budget3():
    entertainment_example = Budget(500, "entertainment_example")
    assert entertainment_example.amount == 500
    entertainment_example.withdraw(200)
    assert entertainment_example.amount == 300
    entertainment_example.deposit(400)
    assert entertainment_example.amount == 700
    assert str(entertainment_example) == "700"


