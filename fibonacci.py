def fibonacci_sequence():
    number = int(input('Enter number of terms in sequence: '))
    count = 0
    first_term = 0
    second_term = 1

    while count < number:
        if count <= 1:
            Next = count
        else:
            Next = first_term + second_term
            first_term = second_term
            second_term = Next
        print(Next)
        count += 1


fibonacci_sequence()
