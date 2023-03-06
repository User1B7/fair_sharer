def fair_sharer(values, num_iterations, share=0.1):
    values_new = values.copy()
    
    for i in range(num_iterations):
        max_index = values_new.index(max(values_new))
        max_value = values_new[max_index]
        left_index = (max_index - 1) % len(values_new)
        right_index = (max_index + 1) % len(values_new)
        shared_value = max_value * share
        values_new[max_index] -= 2 * shared_value
        values_new[left_index] += shared_value
        values_new[right_index] += shared_value
    return values_new
  
if __name__ == "__main__":
    values = [0, 1000, 800, 0]
    print(fair_sharer(values, 1))
