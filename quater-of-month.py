# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4

## in Javascript

# const quarterOf = (month) => {
#   // Your code here
#   if (month >= 1 && month <= 3) {
#     return 1;
#   } else if (month >= 4 && month <= 6) {
#     return 2;
#   } else if (month >= 7 && month <= 9) {
#     return 3;
#   } else {
#     return 4;
#   }
# }