
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["file_management"]
collection = db["files"]

print("MongoDB Connected Successfully!")
import os

def create_file(filename):
    try:
        with open(filename, 'x') as file:
            print(f"file name{filename}: Created successfully")
    except FileExistsError:
        print(f"file name{filename}: Already exists")
    
    except Exception as e:
        print(f"file name {filename}: error occurred:{e}")

def view_all_files():
    files=os.listdir()
    if not files:
        print('no file found')
    else:
        print('files in directory:')
        for file in files:
            print(f" - {file}")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file name {filename}: Deleted successfully")
    except FileNotFoundError:
        print(f"file name {filename}: Not found")
    except Exception as e:
        print(f"file name {filename}: error occurred:{e}")

def read_file(filename):
    try:
        with open('sample.txt','r') as  file:
            content=f .read()
            print(f"content of'{filename}':\n{content}")

    except FileNotFoundError: 
        print(f"file name {filename}: Not found")
    except Exception as e:
        print(f"file name {filename}: error occurred:{e}")            

def edit_file(filename):
    try:
        with open(filename, 'a') as file:
            content = input("Enter content to append: ")
            file.write(content)
            print(f"file name {filename}: Edited successfully")
    except FileNotFoundError:
        print(f"file name {filename}: Not found")
    except Exception as e:
        print(f"file name {filename}: error occurred:{e}")

def main():
    while True:
        print("\nFile Management System")
        print("1. Create a file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Read a file")
        print("5. Edit a file")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the filename to create: ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the filename to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the filename to read: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the filename to edit: ")
            edit_file(filename)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("program started")          
    main()
