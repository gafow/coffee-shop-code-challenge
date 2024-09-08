# Coffee Shop Code Challenge

This project simulates a coffee shop domain with three main models: `Coffee`, `Customer`, and `Order`. The relationships between these models are as follows:

- A `Coffee` has many `Order`s
- A `Customer` has many `Order`s
- An `Order` belongs to a `Customer` and to a `Coffee`
- `Coffee` - `Customer` is a many-to-many relationship

## Setup

1. Ensure you have `pipenv` installed.
2. Run `pipenv install` in the project directory.
3. Run `pipenv shell` to activate the virtual environment.


## Project Structure

The project is divided into three main classes:

### Customer

- Initialized with a name
- Has properties and methods related to orders and coffees

### Coffee

- Initialized with a name
- Has properties and methods related to orders and customers

### Order

- Initialized with a customer, coffee, and price
- Links customers and coffees

## Key Features

- Object relationship methods
- Aggregate and association methods
- Data validation for properties

## Development Guidelines

- Focus on writing functional code first
- Test your code regularly using the provided tools
- Refactor and optimize your code if time allows

Remember to draw your domain model before starting to code, and identify a single source of truth for your data.

Good luck with your coffee shop code challenge!
