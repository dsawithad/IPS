def canteen_queue(capacity, is_national):
    if capacity >= 50:
        print("Open more counters")
    if is_national:
        if capacity >= 80:
            print("Send to any counter")
        else:
            print("Send to National counter")
    else:
        print("Send to International counter")
# Main Execution
capacity = int(input("Enter canteen capacity (%): "))
is_national = input("Is the student National? (yes/no): ").strip().lower() == "yes"
canteen_queue(capacity, is_national)
