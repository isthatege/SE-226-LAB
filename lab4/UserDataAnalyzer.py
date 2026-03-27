def main():
    num_users = int(input("Enter number of users: "))
    
    user_items = {}
    
    for i in range(num_users):
        username = input("Enter username: ")
        num_items = int(input(f"How many items? "))
        
        items = []
        for j in range(num_items):
            item = input(f"Item {j + 1}: ")
            items.append(item)
        
        user_items[username] = items
    
    print("\nUSER DATA:")
    for user, items in user_items.items():
        print(f"{user} -> {items}")
    
    print("\nCOMMON ITEMS:")
    
    all_items = set()
    for items in user_items.values():
        all_items.update(items)
    
    item_counts = {}
    for item in all_items:
        count = 0
        for items in user_items.values():
            if item in items:
                count += 1
        item_counts[item] = count
    
    common_items = [item for item, count in item_counts.items() if count > 1]
    common_items.sort()
    
    for item in common_items:
        print(item)
    
    print("\nUNIQUE ITEMS:")
    
    unique_items = [item for item, count in item_counts.items() if count == 1]
    unique_items.sort()
    
    for item in unique_items:
        print(item)
    
    print("\nMOST POPULAR ITEM:")

    if item_counts:
        max_count = max(item_counts.values())
        most_popular_items = [item for item, count in item_counts.items() if count == max_count]
        most_popular_items.sort()
        for item in most_popular_items:
            print(item)

if __name__ == "__main__":
    main()
