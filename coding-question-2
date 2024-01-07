def total_load_on_support_beams(platform):
    total_load = 0
    rows = len(platform)
    
    for row_idx, row in enumerate(platform):
        for col_idx, cell in enumerate(row):
            if cell == 'O':  # Rounded rock
                total_load += rows - row_idx
    
    return total_load


result = total_load_on_support_beams(platform)
print("Total load on the north support beams:", result)
