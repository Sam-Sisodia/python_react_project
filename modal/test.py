# # Q1: 
# # Assume we have the following tables:

# #     users
# #         user_id (INT, Primary Key)
# #         username (VARCHAR)
# #         email (VARCHAR)

# #     orders
# #         order_id (INT, Primary Key)
# #         user_id (INT, Foreign Key referencing users)
# #         order_date (DATETIME)

# #     order_items
# #         order_item_id (INT, Primary Key)
# #         order_id (INT, Foreign Key referencing orders)
# #         product_id (INT)
# #         quantity (INT)

# #     products
# #         product_id (INT, Primary Key)
# #         product_name (VARCHAR)
# #         price (DECIMAL)

# # You have to write a query to get the top 5 users with the highest total spending in the last 30 days. The output should include the user’s username, email, and their total spending amount.


# select user.username  user.email Max(total)  where today date < last 30 days  limit 5 ;



# # Q2: Print the following output
# # *****
# # ***
# # *

# for  i in range(5,0,-2):
#     for j in range(i):
#         print("*",end="")
#     print("\n")
    
        
      
# # Q3: Create a class functions to find the square root & exponential value and through command line it ask for
# # square root or exponential and then number, Once inputting the number it will give desired result.


# class Findrootex:
    
#     def find(self,number):
#         sq = number ** 0.5   
#         print(sq)  
#         l = []
#         for n in range(number):
#             l.append(number)

#         n =1
#         for i in l :
#             n *=i
        
#         print(n)


# obj = Findrootex()

# obj.find(3)


 
