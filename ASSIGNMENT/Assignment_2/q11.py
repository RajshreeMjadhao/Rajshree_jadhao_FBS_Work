#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = 43530
#notes = [2000,500,200,100,50,20,10]

a_2000= amount//2000
amount=amount%2000

a_500=amount//500
amount=amount%500

a_200=amount//200
amount=amount%200

a_100=amount//100
amount=amount%100

a_50=amount//50
amount=amount%50

a_20=amount//20
amount=amount%20

a_10=amount//10
amount=amount%10


print(f'Numbers of notes ,2000 = {a_2000} , 500 ={a_500}, 200={a_200}, 100={a_100}, 50={a_50}, 20={a_20}, 10={a_10}')