# leetcode-solutions/leetcode-solutions/README.md

# LeetCode Solutions

This project contains solutions to various LeetCode problems, organized by categories such as arrays, strings, linked lists, trees, and dynamic programming. Each problem is implemented in its respective directory, with accompanying test cases to ensure correctness.

## Project Structure

```
leetcode-solutions
├── src
│   ├── arrays
│   │   └── two_sum.py
│   ├── strings
│   ├── linked_lists  
│   ├── trees
│   ├── dynamic_programming
│   └── utils
│       └── test_utils.py
├── tests
│   └── test_two_sum.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd leetcode-solutions
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests**:
   You can run the tests using:
   ```bash
   pytest tests/
   ```

## Example Usage

### Two Sum

To use the `two_sum` function, you can import it as follows:

```python
from src.arrays.two_sum import two_sum

result = two_sum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.