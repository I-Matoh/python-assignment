def process_data(data: list) -> list:
    """
    Removes duplicates from a list while preserving order.
    """
    # Initialize a set to track items we've already encountered.
    # Sets provide O(1) average time complexity for lookups.
    seen = set()
    
    # Initialize a list to store the final deduplicated items.
    # Lists preserve the insertion order of elements.
    result = []
    
    for item in data:
        # Check if the current item is new (not seen before).
        # the 'not in' operator checks the 'seen' set.
        if item not in seen:
            # Add the new item to our result list.
            # The 'append' method adds the item to the end of the list.
            result.append(item)
            
            # Mark the item as seen so future duplicates are ignored.
            # The 'add' method inserts the item into the set.
            # NOTE: This was the bug! The line `seen.add(item)` was originally missing.
            seen.add(item)
            
    return result
