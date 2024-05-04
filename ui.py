from file_operations import FileEncoder, FileDecoder

class UserInterface:
    @staticmethod
    def run():
        while True:
            print("1. Encode file")
            print("2. Decode file")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                input_filename = input("Enter the name of the file to encode: ")
                output_filename = input("Enter the name of the output file: ")
                FileEncoder.encode(input_filename, output_filename)
                print("File encoded successfully.")

            elif choice == "2":
                input_filename = input("Enter the name of the file to decode: ")
                output_filename = input("Enter the name of the output file: ")
                FileDecoder.decode(input_filename, output_filename)
                print("File decoded successfully.")

            elif choice == "3":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    UserInterface.run()