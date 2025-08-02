def get_user_input():
    income = float(input("Enter your monthly income: "))
    expenditure = float(input("Enter your monthly expenditure: "))
    savings = float(input("Enter your current savings: "))
    bank_debts = float(input("Enter your total bank debts: "))
    taxes = float(input("Enter your monthly tax paid: "))
    risk_tolerance = input("Your risk tolerance (low / medium / high): ").lower()
    return income, expenditure, savings, bank_debts, taxes, risk_tolerance


def calculate_financials(income, expenditure, savings, bank_debts, taxes):
    net_income = income - taxes
    monthly_surplus = net_income - expenditure
    savings_rate = (monthly_surplus / income) * 100 if income > 0 else 0
    debt_ratio = (bank_debts / income) * 100 if income > 0 else 0
    return monthly_surplus, savings_rate, debt_ratio


def suggest_plan(surplus, savings_rate, debt_ratio, risk_tolerance):
    print("\n--- Financial Health Report ---")
   
    if surplus > 0:
        print(f"✔ You are saving ₹{surplus:.2f} every month.")
    else:
        print("❌ You are overspending. Cut down on non-essential expenses immediately.")

    if savings_rate < 20:
        print("💡 Try to increase your savings rate to at least 20%. Reduce lifestyle expenses.")
    else:
        print("✔ Good savings rate! Keep it up.")

    if debt_ratio > 40:
        print("⚠ High debt-to-income ratio. Consider debt consolidation or refinancing.")
    elif debt_ratio > 20:
        print("🟡 Manageable debts, but prioritize repayment.")
    else:
        print("✔ Healthy debt ratio.")

    print(f"\nYour risk profile is set to '{risk_tolerance}'.")
    if risk_tolerance == "low":
        print("📌 Recommended: Fixed deposits, PPF, low-risk mutual funds.")
    elif risk_tolerance == "medium":
        print("📌 Recommended: Balanced mutual funds, index funds, SIPs.")
    elif risk_tolerance == "high":
        print("📌 Recommended: Equity mutual funds, stocks (with caution), diversified portfolio.")
    else:
        print("❗ Invalid risk tolerance input. Please enter low, medium, or high.")

    print("\n--- Tips to Improve Financial Health ---")
    print("✅ Track your expenses using an app or spreadsheet.")
    print("✅ Set monthly budgets and stick to them.")
    print("✅ Avoid impulsive purchases; buy only what you need.")
    print("✅ Create an emergency fund covering 6 months of expenses.")
    print("✅ Increase your income through side hustles, freelancing, or skill development.")


def main():
    income, expenditure, savings, bank_debts, taxes, risk_tolerance = get_user_input()
    surplus, savings_rate, debt_ratio = calculate_financials(income, expenditure, savings, bank_debts, taxes)
    suggest_plan(surplus, savings_rate, debt_ratio, risk_tolerance)


if name == "main":
    main()