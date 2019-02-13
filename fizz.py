def fizzbuzz(list1, list2):
    total_length = len(list(list1)) + len(list(list2))
    print(int(total_length))
    #conditions
    if total_length % 3 == 0 and total_length % 5 != 0:
        print("fizz")
    if total_length % 5 == 0 and total_length % 3 != 0:
        print("buzz")
    if total_length % 3 == 0 and total_length % 5 == 0:
        print("fizzbuzz")     

fizzbuzz([1, 2, 3, 4, 5], [1,2,3,4,5,6,7,8,9,0])

