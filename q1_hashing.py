import time


class Medicine:
    # One medicine record (the value we store in the hash table).

    def __init__(self, code, name, price, quantity):
        self.code = code          # key, e.g. "M001"
        self.name = name
        self.price = price
        self.quantity = quantity


class HashTable:
    # Hash table with linear probing.
    # Idea: turn a key into an index, then walk forward if that slot is taken

    def __init__(self, size=11):
        self.size = size
        # Each slot is either None (empty) or a Medicine object
        self.table = [None] * size

    def _hash(self, key):
        # Convert a string key into an index from 0 to size-1.
        # sum of character codes, then mod size so it fits in the table
        return sum(ord(c) for c in key) % self.size

    def insert(self, medicine):
        # Put a medicine into the table. If the code already exists, update it.
        i = self._hash(medicine.code)
        start = i

        # Keep probing until we find an empty slot or a matching code
        while self.table[i] is not None:
            # Same code -> update the existing record
            if self.table[i].code == medicine.code:
                self.table[i] = medicine
                return

            # Collision: try the next slot (wrap around with %)
            i = (i + 1) % self.size

            # Back to start means the table is full
            if i == start:
                print("Table is full.")
                return

        # Found an empty slot -> insert here
        self.table[i] = medicine

    def search(self, code):
        """Find a medicine by code. Return the Medicine, or None if not found."""
        i = self._hash(code)
        start = i

        while self.table[i] is not None:
            if self.table[i].code == code:
                return self.table[i]

            # Keep probing (same idea as insert)
            i = (i + 1) % self.size
            if i == start:
                break  # checked the whole table

        return None

    def display(self):
        """Print every slot so you can see how items are placed."""
        print("\nMedicine slots:")
        for i, item in enumerate(self.table):
            if item is None:
                print(f"Slot {i}: EMPTY")
            else:
                print(
                    f"Slot {i}: {item.code} | {item.name} | "
                    f"RM{item.price} | Qty:{item.quantity}"
                )


def show_medicine(med):
    """Print one medicine nicely (or 'Not found')."""
    if med is None:
        print("Not found.")
    else:
        print("")
        print(f"Code: {med.code}")
        print(f"Name: {med.name}")
        print(f"Price: {med.price}")
        print(f"Quantity: {med.quantity}")


def linear_search(medicines_arr, code):
    for medicine in medicines_arr:
        if medicine.code == code:
            return medicine

    return None

def main():
    ht = HashTable(11)
    arr = []  # plain list, used only to compare search speed

    # Same sample data that goes into BOTH the hash table and the array
    sample = [
        Medicine("M001", "Paracetamol", 5.50, 100),
        Medicine("M002", "Ibuprofen", 8.00, 50),
        Medicine("M003", "Amoxicillin", 12.90, 40),
        Medicine("M004", "Vitamin C", 15.00, 80),
        Medicine("M005", "Cough Syrup", 9.50, 60),
    ]

    for med in sample:
        ht.insert(med)
        arr.append(med)

    print("Sample medicines loaded.\n")

    while True:
        print("===== Pharmacy Inventory =====")
        print("1. Insert medicine")
        print("2. Search medicine")
        print("3. Compare search speed (hash vs array)")
        print("4. Display all medicines")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                code = input("Code: ")
                name = input("Name: ")
                price = float(input("Price: "))
                qty = int(input("Quantity: "))
                med = Medicine(code, name, price, qty)
                ht.insert(med)

                for i, existing in enumerate(arr):
                    if existing.code == med.code:
                        arr[i] = med
                        break
                else:
                    arr.append(med)
                print("Inserted.\n")

            except ValueError:
                print("Invalid input. Please enter a valid code, name, price, and quantity.\n")

        elif choice == "2":
            code = input("Enter code to search: ")
            show_medicine(ht.search(code))
            print()

        elif choice == "3":
            code = input("Enter code to search for timing: ")

            # Hash table search time
            t1 = time.perf_counter_ns()
            result_ht = ht.search(code)
            t2 = time.perf_counter_ns()
            hash_time = t2 - t1

            # Array linear search time (check one by one)
            t3 = time.perf_counter_ns()
            result_ls = linear_search(arr, code)
            t4 = time.perf_counter_ns()
            array_time = t4 - t3

            if (result_ls is not None and result_ht is not None):
                print("\n--- Search Result (Hash Table)---")
                print(f"Medicine Code: {result_ht.code}")
                print(f"Medicine Name: {result_ht.name}")
                print(f"Medicine Price: {result_ht.price}")
                print(f"Medicine Quantity: {result_ht.quantity}\n")

                print("\n--- Search Result (Linear Search)---")
                print(f"Medicine Code: {result_ls.code}")
                print(f"Medicine Name: {result_ls.name}")
                print(f"Medicine Price: {result_ls.price}")
                print(f"Medicine Quantity: {result_ls.quantity}\n")

            elif result_ht is None and result_ls is None:
                print("Medicine not found in either data structure.")

            elif result_ht is None:
                print("No existing medicine found in the hash table.")

            else:
                print("No existing medicine found in the array.")
           
            print("\n--- Timing (nanoseconds) ---")
            print(f"Hash table: {hash_time} ns")
            print(f"Array     : {array_time} ns")
         
        elif choice == "4":
            ht.display()
            print()

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
