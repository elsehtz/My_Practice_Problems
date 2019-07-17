#Dealing with Modulo problems
#
#(Like 10^9 + 7)

# A few distributive properties of modulo are as follows:
# 1. ( a + b ) % c = ( ( a % c ) + ( b % c ) ) % c
# 2. ( a * b ) % c = ( ( a % c ) * ( b % c ) ) % c
# 3. ( a – b ) % c = ( ( a % c ) - ( b % c ) ) % c ( see notes at bottom )
# 4. ( a / b ) % c NOT EQUAL TO ( ( a % c ) / ( b % c ) ) % c
# 5. the result of ( a % b ) will always be less than b
# So, modulo is distributive over +, * and - but not / .


# Example for dealing with large numbers:
# There exists an integer with n-digits, where 1 <= n <= 2*10^5 (to emphasize; up to 200 thousand digits!)
# Represented with result % (10^9 + 7)
#
# Note: we'll refer to (10^9 + 7) as M from here
# Note: result = sum of its substrings = sub_1 + sub_2 + ... + sub_n
# Modular arithmetic lets us use rule 1. ((sub_1)+(sub_n)) % (M) == ((sub_1 % M) + (sub_n % M)) % M