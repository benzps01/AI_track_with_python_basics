## Example of a try-except-finally statement.
while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:  # Specifying a particular exception to be handled
        print("That's not a valid number!")
        """Exceptions can be handled also as a tuple rather than both handled in separate except blocks"""
    except KeyboardInterrupt:
        print("\nNo Input taken")
        break
    finally:
        print("\nAttempted Input\n")
