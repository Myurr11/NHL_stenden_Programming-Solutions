# Programming Assignments Repository

This repository contains solutions to various programming exercises and challenges.

## Exercises

### Exercise 1: `id_to_fruit` function
- **Description**: Fixed a bug with set indexing by replacing the set with a list.
- **Code**: See [`Exercise_1/id_to_fruit.py`](Exercise_1/id_to_fruit.py)

### Exercise 2: `swap` function
- **Description**: Fixed the coordinate swap issue using a temporary array.
- **Code**: See [`Exercise_2/swap.py`](Exercise_2/swap.py)

### Exercise 3: `plot_data` function
- **Description**: Fixed CSV loading and axis swapping for the precision-recall plot.
- **Code**: See [`Exercise_3/plot_data.py`](Exercise_3/plot_data.py)

### Exercise 4: `train_gan` function
- **Description**: Fixed structural and cosmetic bugs in a GAN training loop.
- **Code**: See [`Exercise_4/train_gan.py`](Exercise_4/train_gan.py)


## How to Run the Code

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Myurr11/NHL_stenden_Programming-Solutions.git
   ```

2. **Navigate to the appropriate folder** for the exercise you want to run:
   ```bash
   cd Exercise_1  # or Exercise_2, Exercise_3, etc.
   ```

3. **Run the solution using Python**:
   ```bash
   python id_to_fruit.py  # or swap.py, plot_data.py, etc.
   ```

## Requirements

- Python 3.x
- Required Python packages:  
   - `torch`
   - `torchvision`
   - `matplotlib`
   - `numpy`
   - `ipython`

You can install the required packages by running:
```bash
pip install -r requirements.txt
```

## Setting Up the Environment

If you'd like to set up a virtual environment, follow these steps:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
