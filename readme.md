# Eten API Automation Tests

This repository contains automated tests using pytest for the Eten API. The Eten API provides endpoints for food-related information.
https://eten-ui.vercel.app/

## Getting Started

To get started with running the tests locally or setting up the tests in your CI/CD pipeline, follow the instructions below.

### Prerequisites

- Python 3.x installed on your machine
- Pip package manager

### Installation

1. Clone this repository to your local machine:
    ```git clone https://github.com/your_username/eten-api-tests.git```



2. Navigate to the project directory:

cd eten-api-tests


3. Install the required dependencies:
pip install -r requirements.txt



### Running Tests Locally

To run the tests locally, use the following command:

```pytest```



### GitHub Actions

This repository is integrated with GitHub Actions for continuous integration. The workflow is configured to automatically run the tests on every push or pull request to the `main` branch.

The workflow file (`ci.yml`) is located in the `.github/workflows` directory. It consists of the following steps:

1. Checkout code from the repository.
2. Set up Python.
3. Install dependencies.
4. Run pytest to execute the tests.

### Test Structure

The tests are organized into two main files:

- `tests/test_food_list.py`: Contains tests for the `foodList` API endpoint.
- `tests/test_food_info.py`: Contains tests for the `foodInfo` API endpoint.

Each test file includes multiple test cases covering various scenarios, such as successful requests, error responses, and edge cases.
