import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    #Will read one column of a tab-delimited file.
    #Returns (list of valid numbers, total number of values in the column).
    
    numbers = []
    total_values = 0
    line_number = 0 
    
    try:
        with open(filepath, 'r') as infile:
            for line in infile:
                line_number += 1
                line = line.strip()     #Remove the newline at the end
                if line == "":
                    continue            #This will skip blank lines
                
                #Get the value in the requested column (column starts at 0)
                
                try:
                    value = line.split("\t")[column]
                except IndexError:
                    print(f"Exiting: There is no valid 'list index' in column {column}"
                          f"in line {line_number} in file: {filepath}")
                    sys.exit(1)
                    
                total_values += 1
                   
                try:
                    num = float(value)
                except ValueError:
                    continue
                   
                if math.isnan(num):
                    continue
                   
                numbers.append(num)
                
    except FileNotFoundError:
        print(f"Exiting: File not found: {filepath}")
        sys.exit(1)
    
    #The PDFL if the column shows no numbers, this will show an appropriate message
    if len(numbers) == 0:
        print(f"Error: There were no valid number(s) in column {column} in file: {filepath}")
        sys.exit(1)
    
    return numbers, total_values
        
    
def calculate_average(numbers: list) -> float:
    # average = sum of values / n
    total = 0.0
    for num in numbers:
        total += num
    return total / len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
# Start with the first value, then compare value to the current max and min
    max_val = numbers [0]
    min_val = numbers [0]
    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val
    

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    #Sample variance = sum of (x - average)^2 / (n -1)
    n = len(numbers)
    if n < 2:
        return 0.0
    average = calculate_average(numbers)
    squared_diffs = 0.0
    for num in numbers:
        squared_diffs += (num - average) ** 2
    return squared_diffs / (n -1)
   

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    return math.sqrt(calculate_variance(numbers))

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    sorted_nums = sorted(number)
    n = len(sorted_nums)
    middle = n // 2
    if n % 2 == 1:
        return float(sorted_nums[middle]) #odd: middle value
    return (sorted_nums[middle - 1] + sorted_nums[middle]) / 2 #even: average of two middle values

def print_stats(filepath: str, column: int) -> None:
    """
    Display the summary statistics in the required output format.
    """
    print(filepath)
    print(f"Column: {column}\n")
    
    numbers, total_values = load_data(filepath, column)
    max_val, min_val = get_max_and_min(numbers)
    
    print(f"    Count = {total_values:.3f}")
    print(f"    ValidNum = {len(numbers):.3f}")
    print(f"    Average = {calculate_average(numbers):.3f}")
    print(f"    Maximum = {max_val:.3f}")
    print(f"    Minimum = {min_val:.3f}")
    print(f"    Variance = {calculate_variance(numbers):.3f}")
    print(f"    Std Dev = {calculate_std_dev(numbers):.3f}")
    print(f"    Median = {calculate_median(numbers):.3f}")

def main() -> None:
    # Ask the iser for file and the column
    filepath = input("Enter the file path: ").strip()
    column_text = input("Enter the column number (starting at 0): ").strip()
    
   
    # The column must be a whole number
    try:
        column = int(column_text)
    except ValueError:
        print(f"Exiting: '{column_text}' is not a valid column number")
        sys.exit(1)
        
    if column < 0:
        print("Exiting: the column number cannot be negative")
        sys.exit(1)
        
    print_stats(filepath, column)    

if __name__ == "__main__":
    main()