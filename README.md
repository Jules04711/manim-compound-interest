# manim-compound-interest
An educational animation created with Manim to explain the concept of compound interest through clear visualizations and step-by-step calculations.

## Overview

This project uses the Manim animation library to create an engaging educational video that explains compound interest. The animation demonstrates how compound interest works, compares it with simple interest, and breaks down the mathematical formula in an accessible way.

The video includes:
- Clear definition of compound interest
- Visual explanation of the formula
- Graphical comparison between simple and compound interest
- Year-by-year calculation breakdown
- Final mathematical proof

## Demo

When run, the animation will show:
1. Introduction to compound interest concept
2. The mathematical formula explained
3. A graph comparing $1,000 invested at 10% interest for 5 years under both simple and compound interest
4. Year-by-year calculations showing exactly how the compounding works
5. Final formula application and key takeaways

## Requirements

- Python 3.7+
- Manim
- NumPy

## Installation

1. Install Manim following the official documentation: [https://docs.manim.community/en/stable/installation.html](https://docs.manim.community/en/stable/installation.html)

2. Clone this repository:
```
git clone https://github.com/yourusername/compound-interest-manim.git
cd compound-interest-manim
```

3. Install required dependencies:
```
pip install -r requirements.txt
```

## Run app.py
```
manim -pql app.py CompoundInterestExplanation
```

This command will:
- `-p`: Play the animation once it's rendered
- `-ql`: Render in medium quality for faster rendering
- `CompoundInterestExplanation`: Render the specific scene class from app.py

## How This Code Was Generated

This code was generated using Claude 3.7 Sonnet with the following prompt:

```
As a math specialist, write a Manim program that explains the following problem with precision and engaging, easy-to-understand animations. <problem>{compounding interest}</problem> <solution>{Compound interest = total amount of principal and interest in future (or future value) minus principal amount at present (or present value) = [P (1 + i)n] – P
= P [(1 + i)n – 1]
Where:
 P = principal
 i = annual interest rate
 n = number of compounding periods}</solution>
```

The prompt was designed to:
1. Set the context (as a math specialist)
2. Define the output format (Manim program)
3. Specify the mathematical concept to explain (compound interest)
4. Provide the formula and variables to be explained

## Customization

You can modify the example values in the `CompoundInterestExplanation` class:

```python
principal_value = 1000  # Initial investment
interest_rate = 0.1     # 10% interest
years = 5               # Number of years
```

Adjust these values to demonstrate different scenarios.

## Understanding the Code

The animation is built using Manim's Scene class with these key components:

- **Text elements**: Titles, definitions, and labels
- **Mathematical expressions**: Using MathTex for formula display
- **Axes and graphs**: Creating the visual comparison between simple and compound interest
- **Animation sequences**: Carefully timed to build understanding step by step

## Contributing

Contributions to improve the animation or add additional financial concepts are welcome:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- 3Blue1Brown and the Manim Community for creating and maintaining the Manim library
- Anthropic's Claude AI for generating the initial code
