Build a Challenging Game for Humans (50 points). 
 
Create a Python program run_Guess_My_Number that randomly selects a number between 0 and 1000, and then asks the user to figure out what the number is, carrying on a dialog with the user until the game is over. The user should be offered the opportunity to ask questions such as the following:
If we subtract 6 from n, is the result divisible by 13?
Thus, the questions are of this form:
If we subtract k from n, is the result divisible by m?
The rules here are that n is the secret number, k is in the range 0 to m, and m is a prime number less than 1000. 
 
In each turn, the user should be given the opportunity to either ask a question of the type above, guess the number directly, or quit. In the end the user's score is 0 if s/he quits, or ceiling(n/t) where n is the secret number, and t is the number of turns taken by the user to determine the number, including the correct "guess". 
 
Your program should follow these guidelines:
It should compile and run properly under Python 3.6.
It must not contain any tab characters. All whitespace should be blanks and newline characters only.
The user's input during each turn should be in two phases: (1) Ask, Guess, Quit, and if not "Quit" then, (2) if "Ask" then (k, m), and if "Guess" then g. Here g is the user's guess for the number n.
Whenever the first phase answer is "Ask", then the value of k should be compared with m, and accepted only if0 <= k < m, and also m is prime.
Your program should test the primality of m by using a separate function isPrimeUnder1000(m) which should return either True of Ralse.
Your program should determine the answer to the "Ask" questions by calling another separate function that you should write. This function must be called is_n_minus_k_divisible_by_m(n, k, m), and it must return True or False.
Your program should print the score when the game is over.
Your Python file should be named in the following manner: YourUWNetID_A1.py
Your program may be imported by the autograder, and when being imported, it is important that the game does not automatically run. However, when you simply run your program as the main module, the game should automatically start. You can do this by ending your file with the following code.
if __name__ == '__main__':
  run_Guess_My_Number()C. All whitespace should be blanks and newline characters only.
The user's input during each turn should be in two phases: (1) Ask, Guess, Quit, and if not "Quit" then, (2) if "Ask" then (k, m), and if "Guess" then g. Here g is the user's guess for the number n.
Whenever the first phase answer is "Ask", then the value of k should be compared with m, and accepted only if0 <= k < m, and also m is prime.
Your program should test the primality of m by using a separate function isPrimeUnder1000(m) which should return either True of Ralse.
Your program should determine the answer to the "Ask" questions by calling another separate function that you should write. This function must be called is_n_minus_k_divisible_by_m(n, k, m), and it must return True or False.
Your program should print the score when the game is over.
Your Python file should be named in the following manner: YourUWNetID_A1.py
Your program may be imported by the autograder, and when being imported, it is important that the game does not automatically run. However, when you simply run your program as the main module, the game should automatically start. You can do this by ending your file with the following code.
if __name__ == '__main__':
  run_Guess_My_Number()