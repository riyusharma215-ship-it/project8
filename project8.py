import numpy as np

class DataAnalytics:
    """
    DataAnalytics class to encapsulate NumPy functionalities.
    Follows OOP principles: encapsulation, static methods, and private helpers.
    """
    def __init__(self):
        # Encapsulation: Storing the data in a 'protected' attribute
        self._current_array = None

    @staticmethod
    def _safe_input(prompt, type_func=int):
        """Helper to prevent the program from crashing on bad text input."""
        while True:
            try:
                return type_func(input(prompt))
            except ValueError:
                print(f"Invalid input. Please enter a valid {type_func.__name__}.")

    def _display_array(self, label, array):
        """Standardized way to print arrays as seen in Screenshot 2026-05-09 154512.png."""
        print(f"\n{label}:\n{array}")

    def create_array(self):
        """Handles the creation of 1D, 2D, or 3D arrays."""
        print("\n--- Array Creation ---")
        print("1. 1D Array\n2. 2D Array\n3. 3D Array")
        choice = input("Enter choice: ")

        try:
            if choice == '1':
                n = self._safe_input("Enter number of elements: ")
                elements = input(f"Enter {n} elements (space separated): ").split()
                self._current_array = np.array(elements, dtype=float)
            
            elif choice == '2':
                rows = self._safe_input("Enter number of rows: ")
                cols = self._safe_input("Enter number of columns: ")
                elements = input(f"Enter {rows*cols} elements (space separated): ").split()
                self._current_array = np.array(elements, dtype=float).reshape(rows, cols)
            
            elif choice == '3':
                d = self._safe_input("Enter depth: ")
                r = self._safe_input("Enter rows: ")
                c = self._safe_input("Enter columns: ")
                elements = input(f"Enter {d*r*c} elements (space separated): ").split()
                self._current_array = np.array(elements, dtype=float).reshape(d, r, c)
            
            self._display_array("Array created successfully", self._current_array)
        except Exception as e:
            print(f"Error creating array: {e}. Check your dimensions!")

    def perform_mathematical_ops(self):
        """Performs element-wise operations."""
        if self._current_array is None:
            return print("Error: No array exists. Create one first.")

        print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        choice = input("Select operation: ")
        
        # Humanized logic: automatically expects the same shape as the existing array
        print(f"Enter elements for a second {self._current_array.shape} array:")
        elements = input("Elements (space separated): ").split()
        
        try:
            second_arr = np.array(elements, dtype=float).reshape(self._current_array.shape)
            self._display_array("Original Array", self._current_array)
            self._display_array("Second Array", second_arr)

            if choice == '1': self._display_array("Result of Addition", self._current_array + second_arr)
            elif choice == '2': self._display_array("Result of Subtraction", self._current_array - second_arr)
            elif choice == '3': self._display_array("Result of Multiplication", self._current_array * second_arr)
            elif choice == '4': self._display_array("Result of Division", self._current_array / second_arr)
        except Exception as e:
            print(f"Operation failed: {e}")

    def search_sort_filter(self):
        """Logic for finding and organizing data."""
        if self._current_array is None: return
        
        print("\n1. Search Value\n2. Sort Array\n3. Filter (Greater Than)")
        choice = input("Choice: ")

        if choice == '1':
            val = self._safe_input("Value to search: ", float)
            coords = np.where(self._current_array == val)
            print(f"Found at indices: {list(zip(*coords))}")
        elif choice == '2':
            # Sorting row-wise as shown in Screenshot 2026-05-09 154512.png
            self._display_array("Sorted Array", np.sort(self._current_array))
        elif choice == '3':
            limit = self._safe_input("Show values greater than: ", float)
            print("Filtered Results:", self._current_array[self._current_array > limit])

    def compute_stats(self):
        """Computes statistical aggregates."""
        if self._current_array is None: return
        
        print("\n1. Sum\n2. Mean\n3. Median\n4. Std Dev\n5. Variance")
        choice = input("Select statistic: ")
        
        stats = {
            '1': ("Sum", np.sum), '2': ("Mean", np.mean), 
            '3': ("Median", np.median), '4': ("Std Dev", np.std),
            '5': ("Variance", np.var)
        }
        
        if choice in stats:
            label, func = stats[choice]
            print(f"{label}: {func(self._current_array)}")

def main():
    """Main interface loop."""
    analyzer = DataAnalytics()
    
    print("Welcome to the NumPy Analyzer!")
    print("==============================")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Create Array")
        print("2. Math Operations")
        print("3. Search, Sort, or Filter")
        print("4. Statistics")
        print("5. Exit")
        
        user_choice = input("Enter your choice (1-5): ")

        if user_choice == '1': analyzer.create_array()
        elif user_choice == '2': analyzer.perform_mathematical_ops()
        elif user_choice == '3': analyzer.search_sort_filter()
        elif user_choice == '4': analyzer.compute_stats()
        elif user_choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1-5.")

if __name__ == "__main__":
    main()