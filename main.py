tasks = []
while True:
  print("\n--- TO-DO LIST ----")
  print("1.Add Task")
  print("2.View Tasks")
  print("3.Delete Task")
  print("4.Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")
  elif choice == "3":
    if len(tasks) == 0:
      print("No tasks to delete.")
    else:
      for i, task in enumerate(taks,start=1):
        print(i,task)
      num = int(input("Enter task number to delete: "))
      if 1<=num<=len(tasks):
        removed = tasks.poop(num-1)
        print("removed,"deleted successfully!")
      else:
          print("Invalid task number")
  elif choice == "4":
      print("Thnak you for usig To-DO List App!")
  else:
      print("Invalid choice. Try again.")
  
      
    
