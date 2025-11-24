import math
from datetime import date, timedelta

def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_forecast(start_savings, monthly_surplus, target_amount):
    needed_savings = target_amount - start_savings
    if needed_savings <= 0:
        return 0, date.today()
    months_needed = math.ceil(needed_savings / monthly_surplus)
    days_needed = months_needed * 30.4375
    target_date = date.today() + timedelta(days=days_needed)
    return months_needed, target_date



def run_goal_forecaster():
    print("******************************************")
    print(" Personalized Budget/Goal Forecaster")
    print("******************************************")

    
    current_savings = get_numeric_input("1. Enter your Current Savings : ")
    monthly_income = get_numeric_input("2. Enter your Monthly Net Income : ")
    fixed_expenses = get_numeric_input("3. Enter your Monthly Fixed Expenses : ")
    variable_expenses = get_numeric_input("4. Enter your Monthly Variable Expenses : ")
    goal_target = get_numeric_input("5. Enter your Goal Target Amount : ")

    
    initial_expenses = fixed_expenses + variable_expenses
    initial_surplus = monthly_income - initial_expenses

    print(f"\nCalculated Current Monthly Surplus: {initial_surplus:.2f}")

    if initial_surplus <= 0:
        print("\n Warning: Your expenses meet or exceed your income.")
        print("   Goal forecasting requires a positive monthly surplus.")
        return

    
    initial_months, initial_date = calculate_forecast(current_savings, initial_surplus, goal_target)

    print("\n--- BASELINE FORECAST (Current Habits) ---")
    print(f"Time to reach {goal_target:,.2f}: **{initial_months} months**")
    print(f"Estimated Date: **{initial_date.strftime('%B %Y')}**")

    
    print("\n--- SCENARIO MODELING (What If...) ---")
    scenario_change = get_numeric_input(
        "6. Enter the amount you want to **SAVE EXTRA** each month (+ number) or **LESS** (- number): "
    )

    scenario_surplus = initial_surplus + scenario_change

    if scenario_surplus <= 0:
        print("\n Warning: This scenario results in zero or negative surplus. Goal cannot be reached.")
        return

    scenario_months, scenario_date = calculate_forecast(current_savings, scenario_surplus, goal_target)

    
    print("\n--- SCENARIO RESULTS ---")
    print(f"New Monthly Surplus: {scenario_surplus:.2f}")
    print(f"New Time to reach {goal_target:,.2f}: **{scenario_months} months**")
    print(f"New Estimated Date: **{scenario_date.strftime('%B %Y')}**")

    month_difference = initial_months - scenario_months
    print("\n**********************************")
    print("Comparison Report")
    print("**********************************")

    if month_difference > 0:
        years_saved = month_difference // 12
        months_saved = month_difference % 12
        print(f" **SUCCESS!** You reached your goal **{years_saved} years and {months_saved} months** earlier!")
        print(f"   You cut the timeline by {month_difference} months.")
    elif month_difference < 0:
        years_delayed = abs(month_difference) // 12
        months_delayed = abs(month_difference) % 12
        print(f" **DELAYED!** Your goal is delayed by **{years_delayed} years and {months_delayed} months**.")
        print(f"   You added {-month_difference} months to the timeline.")
    else:
        print("Result: The scenario change did not affect the timeline.")

if __name__ == "__main__":
    run_goal_forecaster()



