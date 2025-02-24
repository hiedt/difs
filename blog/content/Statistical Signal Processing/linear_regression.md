# Linear Regression

## Introduction

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. It is widely used for predictive analysis and understanding the strength of relationships between variables.

## Simple Linear Regression

Simple linear regression involves a single independent variable. The relationship between the dependent variable (Y) and the independent variable (X) is modeled by a linear equation:

$$
Y = \beta_0 + \beta_1X + \epsilon
$$

Where:

- `Y` is the dependent variable.
- `X` is the independent variable.
- `\beta_0` is the y-intercept.
- `\beta_1` is the slope of the line.
- `\epsilon` is the error term.

## Multiple Linear Regression

Multiple linear regression involves two or more independent variables. The relationship is modeled by the following equation:

$$
Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + \ldots + \beta_nX_n + \epsilon
$$

Where:

- `Y` is the dependent variable.
- `X_1, X_2, \ldots, X_n` are the independent variables.
- `\beta_0` is the y-intercept.
- `\beta_1, \beta_2, \ldots, \beta_n` are the coefficients of the independent variables.
- `\epsilon` is the error term.

## Assumptions of Linear Regression

Linear regression relies on several key assumptions:

1. **Linearity**: The relationship between the dependent and independent variables is linear.
2. **Independence**: Observations are independent of each other.
3. **Homoscedasticity**: The residuals (errors) have constant variance.
4. **Normality**: The residuals are normally distributed.

## Applications

Linear regression is used in various fields, including:

- **Economics**: To predict consumer spending based on income.
- **Medicine**: To model the relationship between dosage and response.
- **Engineering**: To estimate the impact of temperature on material strength.

## Example Python Code Using scikit-learn

Here's an example of how to perform linear regression using scikit-learn in Python:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate some example data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Plot the results
plt.scatter(X_test, y_test, color='black', label='Actual data')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Predicted line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.legend()
plt.show()
