# int_1 = int(input())
# int_2 = int(input())
# int_3 = int(input())
#
# result = int_1 + int_2 + int_3
#
# print(result)

#################


#Lottery Game

winning_ticket = 77
lottery_process = True
#lottery_process = False

while lottery_process:
    lucky_number = int(input('Enter the number:'))
    if winning_ticket == lucky_number:
        print('You won the lottery')

    else:
        print('Unfortunately you lose')

else:
    print('lottery process in not available')