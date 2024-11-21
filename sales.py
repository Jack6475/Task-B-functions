import random

def daily_sales(available_items, inventory_records, current_day):
    '''
    This function is responsible for updating the sales for a given day.
    ---------------
    Function Input:
    ---------------
    available_items: (integer) Available T-shirts from the previous day.
    inventory_records: (List) A list of inventory records until the previous day.
                        Each row contains (day, sales, restocked items, available items).
    current_day: (integer) Day number which you want to add as the current day. 

    ----------------
    Function Output:
    ----------------
    available_items:(integer) This function returns this integer which updates 
                               the available items at the current day.

    The function will also update the inventory_records (for sales) for the given current day. 
    '''

    # On non-restocking days, calculate sales
    if current_day % 7 != 0:
        # Randomly generate the number of units sold (up to a maximum of 200)
        sold_units = random.randint(0, min(200, available_items))
        
        # Update the available items after the sales
        available_items -= sold_units
        
        # Append the daily record for sales
        inventory_records.append([current_day, sold_units, 0, available_items])
    else:
        # On restocking days, no sales are recorded
        inventory_records.append([current_day, 0, 0, available_items])

    return available_items