def process_data(data: list) -> list:
    """
    Removes duplicates from a list while preserving order.
    """
    # WHAT: Initialize a set to track items we've already encountered.
    # HOW: Sets provide O(1) average time complexity for lookups.
    seen = set()
    
    # WHAT: Initialize a list to store the final deduplicated items.
    # HOW: Lists preserve the insertion order of elements.
    result = []
    
    for item in data:
        # WHAT: Check if the current item is new (not seen before).
        # HOW: The 'not in' operator checks the 'seen' set.
        if item not in seen:
            # WHAT: Add the new item to our result list.
            # HOW: The 'append' method adds the item to the end of the list.
            result.append(item)
            
            # WHAT: Mark the item as seen so future duplicates are ignored.
            # HOW: The 'add' method inserts the item into the set.
            # NOTE: This was the bug! The line `seen.add(item)` was originally missing.
            seen.add(item)
            
    return result
