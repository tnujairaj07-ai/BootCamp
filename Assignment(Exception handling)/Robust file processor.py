import csv


def process_csv(filepath):
    file = None

    try:
        file = open(filepath, "r", newline="")
        reader = csv.reader(file)

        rows = list(reader)

        if not rows:
            print("CSV file is empty.")
            return

        num_cols = len(rows[0])

        averages = []

        for col in range(num_cols):
            values = []

            for row in rows:
                values.append(float(row[col]))

            avg = sum(values) / len(values)
            averages.append(avg)

        print("Column Averages:")
        for i, avg in enumerate(averages, start=1):
            print(f"Column {i}: {avg:.2f}")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except csv.Error:
        print("Error: Malformed CSV file.")

    except ValueError:
        print("Error: Non-numeric data found.")

    finally:
        if file:
            file.close()
            print("File closed.")


# Test
process_csv("data.csv")