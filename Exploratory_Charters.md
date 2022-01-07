# YPChallenge

Exploratory charters were aligned according to the priority that I considered following the core/main business of the application (money management app where you can add expenses by category and tack spendings). For the issues found, I put together the description and steps to reproduce the issues/bugs, this way I can save time and space.
> Note: I always separate the description from the test steps as it's cleaner and readable.

## Exploratory Testing
**Agenda**
- [Exploratory Charters](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#exploratory-charters)
  - [Charter #1: Expenses/Incomes management (CRUD)](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#charter-1-expensesincomes-management-crud)
  - [Charter #2: Expenses/Incomes filters](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#charter-2-expensesincomes-filters)
  - [Charter #3: Transfer management (CRUD)](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#charter-3-transfer-management-crud)
  - [Charter #4: Settings main functionalities as a free account (Currency, languages)](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#charter-4-settings-main-functionalities-as-a-free-account-currency-languages)
  - [Charter #5: Search by categories](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#charter-5-search-by-categories)
- [Findings From Charters](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#findings-from-charters)
  - [Issue #1](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-1)
  - [Issue #2](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-2)
  - [Issue #3](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-3)
  - [Issue #4](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-4)
  - [Issue #5](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-5)
  - [Issue #6](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-6)
  - [Issue #7](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-7)
  - [Issue #8](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-8)
  - [Issue #9](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-9)
  - [Issue #10](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-10)
  - [Issue #11](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#issue-11)
- [Charters Prioritization & Planned spend time per charter](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#charters-prioritization--planned-spend-time-per-charter)
- [Risks](https://github.com/erickcajasmonier/YPChallenge/blob/main?Exploratory_Charters.md#risks)

## Exploratory Charters

### Charter #1: Expenses/Incomes management (CRUD)
**Target:** Explore the different categories and check how moneyfy CRUD actions behaves regarding expenses and incomes management.

**Resources:**
- OS: Android 12 
- Device: Pixel 6 Pro
- Proxy Tool: Charles Proxy.

**Test Notes:**
- Focusing on the main app screen.
  - Add a new income using the “Income” button.
  - Add a new expense using “Expense” button.
  - Add a new expense from random expense icons in main screen.
  - Add/Edit cents in the amounts.
  - Update the dates of the expenses/incomes
  - Open balance detailed summary to check expenses & incomes
  - Modify an expense/income.
  - Delete an expense/income.
  - Adding/Updating notes for expenses and incomes.
  - Calculating an addition or deletion.
  - Select or change the category for expenses/incomes.
  - Select or change the payment method (cash/payment card).
  - Confirm the changes.
  - Canceling changes with "back" icon button.
  
### Charter #2: Expenses/Incomes filters
**Target:** Explore the different filters of the expenses and incomes in the main screen (by day, week, month, year, all, interval, choosing date, carry over).

**Resources:**
- OS: Android 12 
- Device: Pixel 6 Pro
- Proxy Tool: Charles Proxy.

**Test Notes:**
- Focusing on the main app screen.
  - Filter the report by day with and without carry over.
  - Filter the report by week with and without carry over.
  - Filter the report by moth with and without carry over.
  - Filter the report by year with and without carry over
  - Filter the report by all with and without carry over.
  - Filter the report by interval with and without carry over.
  - Filter the report by choosing date with and without carry over.
  - Edit/Change a value/amount of an expense or income with the filtered view.
  - Carry over should show the negative balance in the next date.
  - Add new income or expense with the filtered view.
  
### Charter #3: Transfer management (CRUD)
**Target:** Explore how moneyfy manages the transfers having in mind the CRUD actions, check how it behaves.

**Resources:**
- OS: Android 12 
- Device: Pixel 6 Pro
- Proxy Tool: Charles Proxy.

**Test Notes:**
- Focusing on the main app screen.
  - Add a new transfer using the “transfer” icon button from payment card to cash.
  - Add a new transfer using the “transfer” icon button from cash to payment card.
  - Add a new transfer using the “transfer” icon button from same services (cash to cash, payment card to payment card).
  - Add/Edit cents in the amounts.
  - Update the dates of the transfers.
  - Open balance detailed summary to check transfers.
  - Modify a transfer
  - Delete a transfer.
  - Adding/Updating notes for transfers.
  - Calculating an addition or deletion.
  - Select or change the transfer types.
  - Confirm the changes.
  - Canceling changes with "back" icon button.
  
### Charter #4: Settings main functionalities as a free account (Currency, languages)
**Target:** Explore the main settings functionalities as a free account, changing the currency and languages.

**Resources:**
- OS: Android 12 
- Device: Pixel 6 Pro
- Proxy Tool: Charles Proxy.

**Test Notes:**
- Review the different languages that the application supports (list).
- Review the different currencies that the application supports (list).
- Change to different languages.
- Change to different currencies.

### Charter #5: Search by categories
**Target:** Explore the searching of categories using the search icon button.

**Resources:**
- OS: Android 12 
- Device: Pixel 6 Pro
- Proxy Tool: Charles Proxy.

**Test Notes:**
- Search by categories without expenses.
- Search by categories with expenses.
- Change/Update amounts.
- Change/Update dates.


## Findings From Charters
### Issue #1
**Title:** Automatic saved changes after editing expenses/incomes.
**Desc w/ steps:** When the user tap on an expense/income, then change/edit the value/amount and tap on the back icon button.
**Actual Result:** The app is saving changes automatically.
**Expected Result:** The app should have a “confirm” button to save changes as users can make mistakes and there is no way to get the previous amount/value.

### Issue #2
**Title:** Minus operator button is taking the amount to 0 in the backend.
**Desc w/ steps:** When the user add/edit an expense or income, then tap in the minus operator button.
**Actual Result:** The backend of the application is updating the amount to 0.
**Expected Result:** (Not sure about the correct behavior about this) The app should not take the amount to 0.

### Issue #3
**Title:** Income/Expense amount/value is not updating after tapping the operator buttons.
**Desc w/ steps:** When the user add/edit an expense or income, then tap in the plus/divide/multiplication/minus icon, finally write another amount to perform the operator action.
**Actual Result:** The amount text is not getting updated, it gets updated after you tap in the back icon button.
**Expected Result:** The user should see the amount text updated according to the selected operator and the amount wrote.

### Issue #4
**Title:** Operators are performing action with the actual amount of the expense/income.
**Desc w/ steps:** When the user add/edit an expense or income, then tap in the plus/divide/multiplication/minus icon.
**Actual Result:** The backend is performing plus/divide/multiplication/minus actions having in mind the current amount. For example: If the current amount is 25, when I tap in the plus icon is performing 25+25, having a result of 50).
**Expected Result:** (Not sure about the correct behavior about this) The app should suggest to add a value after the operator to don’t use the current amount by default.

### Issue #5
**Title:** If the amount has cents, the user can’t edit the non-cents amount without deleting the cents first.
**Desc w/ steps:** When the user add/edit an expense or income, then add cents in the value/amount, finally try to tap in the non cent section of the amount.
**Actual Result:** The app is not allowing you to change the non cents amount.
**Expected Result:** The app should allow you to edit just the non cent amount in case the user needs to.

### Issue #6
**Title:** Categories position randomly moves to other places when there is an expense percentage.
**Desc w/ steps:** When the user adds expenses for any category and apply the changes, the category icon position is moving randomly in the main page of the application.
**Actual Result:** The app is moving positions of the categories with expense percentage randomly.
**Expected Result:** In case the category icon needs to be moved, the application can sort it by descendant or just keep the icons in the same position.

### Issue #7
**Title:** The “Choose date” filter is not working as expected for the current date.
**Desc w/ steps:** When the user is in the “All” filter from the menu, then selects “Choose date”, finally select the current date and apply changes.
**Actual Result:** The application is still showing the “All” filter view.
**Expected Result:** The application should show the current date filter view.

### Issue #8
**Title:** Users with a filtered view besides “All” that change/update an amount in a different date from the current one using the balance summary option is going to be kicked to the default (first) date after applying changes.
**Desc w/ steps:** When the user is in a filtered view besides “All”, then opens the balance summary detailed screen, make changes/updates in the amount of an expense/income, finally apply changes.
**Actual Result:** The application is scrolling automatically to the default (first) date.
**Expected Result:** The application should keep in the same date that I applied the changes without auto scrolling.

### Issue #9
**Title:** Searching by “Food” is showing Transfer records.
**Desc w/ steps:** When the user taps in the search icon button, then search by “Food” and finally apply changes.
**Actual Result:** The app is showing the Transfer records.
**Expected Result:** The app should show the Food records if there are any.

### Issue #10
**Title:** Some currencies like Colombian Pesos have big amounts that the app doesn’t support.
**Desc w/ steps:** When the user change to a currency that supports big amounts of money, like Colombian Pesos, the app is limiting the amount to a maximum.
**Actual Result:** The app is limiting the amount to a maximum of 999,999,999.99.
**Expected Result:** Some Colombian users may have more money as savings, the app should add support for those cases with some currencies.

### Issue #11
**Title:** Supported languages are missing some translations.
**Desc w/ steps:** When the user change to another language using the settings options from the three dots menu icon at the upper right screen.
**Actual Result:** The app is not translating some of the texts/labels.
**Expected Result:** The app should translate all the texts/labels to the corresponding language.

## Charters Prioritization & Planned spend time per charter
- The first area to explore is the expense/income management (CRUD) because it’s the main/core business functionality of the company/software.
- I expected to spend no more than 45 minutes per charter (some charters were faster than others).

## Risks
- Some risks that I can find are:
  - As Android has many brands (Samsung, OnePlus, Pixel, LG, others), it’s a risk to have few Android devices to test due to screen sizes, OS version, device hardware, many others.
  - In case the app has notifications, there are differences between Android versions > 7 and < 6 regarding the notifications displays and icons.
  - Memory leaks that can be inserted by mistake in the application.
  - The app should be up to date, at least testers with the Beta OS next version to cover future issues/blockers with the incoming updates. (iOS & Android)
  - As it’s a paid application (to use full features), it’s into the considerations a risk on the payments by random not valid credit cards.
  - As it’s a subscription application, it’s good to consider that after the user unsubscribe from the Pro feature, the user will not be charges in the future billing.
  - The app should consider features that covers accessibility.
