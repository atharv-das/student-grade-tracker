from datetime import datetime


def add_new_expense(expense_list, amount, category, note):
    # Auto-increment simple numeric ID
    new_id = len(expense_list) + 1
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    item = {
        "id": new_id,
        "date": current_time,
        "amount": round(amount, 2),
        "category": category.strip().title(),
        "note": note.strip()
    }
    expense_list.append(item)
    return expense_list


def get_summary(expense_list):
    total = sum(item["amount"] for item in expense_list)

    category_totals = {}
    for item in expense_list:
        cat = item["category"]
        if cat in category_totals:
            category_totals[cat] += item["amount"]
        else:
            category_totals[cat] = item["amount"]

    return total, category_totals
