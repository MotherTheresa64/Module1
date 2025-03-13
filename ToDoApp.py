# todo.py

def add_task(task_list):
    """Adds a new task to the list"""
    try:
        task = input("Enter the task you want to add: ")
        if task.strip() == "":
            raise ValueError("Task cannot be empty.")
        task_list.append(task)
        print(f"Task '{task}' added successfully!")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks(task_list):
    """Displays all tasks in the list"""
    if not task_list:
        print("No tasks to display!")
    else:
        print("Your tasks:")
        for idx, task in enumerate(task_list, 1):
            print(f"{idx}. {task}")


def delete_task(task_list):
    """Deletes a task from the list"""
    try:
        if not task_list:
            raise ValueError("No tasks available to delete.")
        
        # Try to convert the input to an integer
        task_num = input("Enter the task number to delete: ")
        task_num = int(task_num)  # Attempt to convert to an integer
        
        if task_num < 1 or task_num > len(task_list):
            raise IndexError("Task number out of range.")
        
        removed_task = task_list.pop(task_num - 1)
        print(f"Task '{removed_task}' has been deleted.")
        
    except ValueError:
        print("Error: Please enter a valid number for the task number.")
    except IndexError as ie:
        print(f"Error: {ie}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def main_menu():
    """Displays the main menu and handles user input"""
    task_list = []
    while True:
        print("\n=== To-Do List ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_task(task_list)
            elif choice == 2:
                view_tasks(task_list)
            elif choice == 3:
                delete_task(task_list)
            elif choice == 4:
                print("Exiting the To-Do List Application. Goodbye!")
                break
            else:
                raise ValueError("Invalid option. Please choose a valid menu option.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main_menu()
