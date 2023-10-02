
logo="""
NNNNNNNN        NNNNNNNN                                         b::::::b                                                                                                                                                       iiii                                                 
N:::::::N       N::::::N                                         b::::::b                                                                                                                                                      i::::i                                                
N::::::::N      N::::::N                                         b::::::b                                                                                                                                                       iiii                                                 
N:::::::::N     N::::::N                                          b:::::b                                                                                                                                                                                                            
N::::::::::N    N::::::Nuuuuuu    uuuuuu     mmmmmmm    mmmmmmm   b:::::bbbbbbbbb        eeeeeeeeeeee    rrrrr   rrrrrrrrr           ggggggggg   ggggguuuuuu    uuuuuu      eeeeeeeeeeee        ssssssssss       ssssssssss   iiiiiiinnnn  nnnnnnnn       ggggggggg   ggggg          
N:::::::::::N   N::::::Nu::::u    u::::u   mm:::::::m  m:::::::mm b::::::::::::::bb    ee::::::::::::ee  r::::rrr:::::::::r         g:::::::::ggg::::gu::::u    u::::u    ee::::::::::::ee    ss::::::::::s    ss::::::::::s  i:::::in:::nn::::::::nn    g:::::::::ggg::::g          
N:::::::N::::N  N::::::Nu::::u    u::::u  m::::::::::mm::::::::::mb::::::::::::::::b  e::::::eeeee:::::eer:::::::::::::::::r       g:::::::::::::::::gu::::u    u::::u   e::::::eeeee:::::eess:::::::::::::s ss:::::::::::::s  i::::in::::::::::::::nn  g:::::::::::::::::g          
N::::::N N::::N N::::::Nu::::u    u::::u  m::::::::::::::::::::::mb:::::bbbbb:::::::be::::::e     e:::::err::::::rrrrr::::::r     g::::::ggggg::::::ggu::::u    u::::u  e::::::e     e:::::es::::::ssss:::::ss::::::ssss:::::s i::::inn:::::::::::::::ng::::::ggggg::::::gg          
N::::::N  N::::N:::::::Nu::::u    u::::u  m:::::mmm::::::mmm:::::mb:::::b    b::::::be:::::::eeeee::::::e r:::::r     r:::::r     g:::::g     g:::::g u::::u    u::::u  e:::::::eeeee::::::e s:::::s  ssssss  s:::::s  ssssss  i::::i  n:::::nnnn:::::ng:::::g     g:::::g           
N::::::N   N:::::::::::Nu::::u    u::::u  m::::m   m::::m   m::::mb:::::b     b:::::be:::::::::::::::::e  r:::::r     rrrrrrr     g:::::g     g:::::g u::::u    u::::u  e:::::::::::::::::e    s::::::s         s::::::s       i::::i  n::::n    n::::ng:::::g     g:::::g           
N::::::N    N::::::::::Nu::::u    u::::u  m::::m   m::::m   m::::mb:::::b     b:::::be::::::eeeeeeeeeee   r:::::r                 g:::::g     g:::::g u::::u    u::::u  e::::::eeeeeeeeeee        s::::::s         s::::::s    i::::i  n::::n    n::::ng:::::g     g:::::g           
N::::::N     N:::::::::Nu:::::uuuu:::::u  m::::m   m::::m   m::::mb:::::b     b:::::be:::::::e            r:::::r                 g::::::g    g:::::g u:::::uuuu:::::u  e:::::::e           ssssss   s:::::s ssssss   s:::::s  i::::i  n::::n    n::::ng::::::g    g:::::g           
N::::::N      N::::::::Nu:::::::::::::::uum::::m   m::::m   m::::mb:::::bbbbbb::::::be::::::::e           r:::::r                 g:::::::ggggg:::::g u:::::::::::::::uue::::::::e          s:::::ssss::::::ss:::::ssss::::::si::::::i n::::n    n::::ng:::::::ggggg:::::g           
N::::::N       N:::::::N u:::::::::::::::um::::m   m::::m   m::::mb::::::::::::::::b  e::::::::eeeeeeee   r:::::r                  g::::::::::::::::g  u:::::::::::::::u e::::::::eeeeeeee  s::::::::::::::s s::::::::::::::s i::::::i n::::n    n::::n g::::::::::::::::g           
N::::::N        N::::::N  uu::::::::uu:::um::::m   m::::m   m::::mb:::::::::::::::b    ee:::::::::::::e   r:::::r                   gg::::::::::::::g   uu::::::::uu:::u  ee:::::::::::::e   s:::::::::::ss   s:::::::::::ss  i::::::i n::::n    n::::n  gg::::::::::::::g           
NNNNNNNN         NNNNNNN    uuuuuuuu  uuuummmmmm   mmmmmm   mmmmmmbbbbbbbbbbbbbbbb       eeeeeeeeeeeeee   rrrrrrr                     gggggggg::::::g     uuuuuuuu  uuuu    eeeeeeeeeeeeee    sssssssssss      sssssssssss    iiiiiiii nnnnnn    nnnnnn    gggggggg::::::g           
                                                                                                                                              g:::::g                                                                                                              g:::::g           
                                                                                                                                  gggggg      g:::::g                                                                                                  gggggg      g:::::g           
                                                                                                                                  g:::::gg   gg:::::g                                                                                                  g:::::gg   gg:::::g           
                                                                                                                                   g::::::ggg:::::::g                                                                                                   g::::::ggg:::::::g           
                                                                                                                                    gg:::::::::::::g                                                                                                     gg:::::::::::::g            
                                                                                                                                      ggg::::::ggg                                                                                                         ggg::::::ggg              
                                                                                                                                         gggggg                                                                                                               gggggg                 
"""
import random
number = random.randint(1,100)
print(logo)
player_name = input("Welcome, Enter your name? ")
number_of_guesses = 0
print('I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number between 1 and 100 then you will guess, alright? \nDon\'t forget! You have only 10 chances so guess:'.format(player_name))

while number_of_guesses < 10:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your estimate is too low, go up a little!')
    if guess > number:
        print('Your estimate is too high, go down a bit!')
    if guess == number:
        break
if guess == number:
    print('Congratulations {}, you guessed the number in {} tries!'.format(player_name, number_of_guesses))
else:
    print('You couldn\'t guess the number.\nGame Over \nWell, the number was {}.\nTry again'.format(number))