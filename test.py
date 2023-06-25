# định nghĩa 1 function
def sum_of_odd_numbers(n):
    sum = 0
    for num in range(n):
        if num % 2 != 0:
            sum = sum + num

    return sum

if __name__ == "__main__":
    print (sum_of_odd_numbers(1000)) 