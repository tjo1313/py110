# Sort the following list of numbers first in ascending numeric order, then in
# descending numeric order. Do not mutate the list.

# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# print(sorted(lst))
# print(sorted(lst, reverse=True))

# Repeat the previous exercise but this time perform the sort by mutating the
# original list.

# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

# Repeat problem 2, but this time sort the list as string values. Both the list
# passed to the sorting function and the returned list should contain numbers, 
# not strings.

# lst.sort(key=str)
# print(lst)

# lst.sort(key=str, reverse=True)
# print(lst)

# Problem 4: How would you sort the following list of dictionaries based on the
# year of publication of each book, from earliest to most recent?

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {   'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

# Expected output--Pretty printed for clarity
# [
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800'
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869'
#     },
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967'
#     }
# ]

def sort_by_date(dict):
    return int(dict['published'])

books.sort(key=sort_by_date)
print(books)