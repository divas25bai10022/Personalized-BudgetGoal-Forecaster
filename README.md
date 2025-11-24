# Personalized BudgetGoal Forecaster
VITYARTHI PROJECT

The Personalized Budget/Goal Forecaster is a unique Python project designed to solve the real-world problem of financial uncertainty and goal planning by providing data-driven projections and scenario modeling.

Key Functionality
1. Baseline Forecasting 
The primary function of the tool is to calculate the estimated time (in months and years) it will take a user to reach a specific financial goal (e.g., saving for a down payment, a large purchase, or an emergency fund) based on their current financial standing.

Inputs: Current Savings, Monthly Income, Fixed Expenses, and Variable Expenses.

Calculation: It first calculates the Monthly Surplus (Income - Total Expenses) and then uses this surplus to determine the number of months required to cover the remaining amount needed for the goal.

2. Scenario Modeling 
This is the project's most unique and powerful feature. It allows the user to test a "what-if" scenario by inputting a proposed change to their monthly savings amount (e.g., saving $100 more, or $50 less).

Impact Assessment: The script calculates a new monthly surplus based on the proposed change.

New Projection: It then runs a second forecast using this new surplus, showing the user the faster or slower timeline to reach the same goal.

3. Comparison and Reporting 
The program concludes by comparing the baseline forecast (current habits) with the scenario forecast (new habits).

Result: It clearly reports the difference in time, telling the user precisely how many months or years they could accelerate or delay their goal by making the proposed change. This quantification makes the financial decision-making tangible and motivating.