"""
secret_message.py
=====

Write an interactive console program that allows a user to encrypt or
decrypt a message using either a substitution cipher or the vigenère
cipher. Use the spytools module you created to encrypt and decrypt
messages.

1. Continually ask the user if they want to (e)ncrypt, (d)ecrypt or
(q)uit.
2. If the user types in e, ask which cipher they would like to use:
(s)ubstitution cipher or the (v)igenère cipher
    * if the user picks (s)ubstitution:
        * ask for the password and the message
        * encrypt the message and print out the ciphertext
    * if the user picks (v)igenère:
        * ask for the key and the message
        * encrypt the message and print out the ciphertext
    * if the user does not pick s or v
        * print out an error message
        * ask for a new command, encrypt or decrypt
3. If the user types in d, ask which cipher the message was encrypted in
(s)ubstitution cipher or the (v)igenère cipher
    * if the user picks (s)ubstitution:
        * ask for the password and the encrypted message
        * decrypt the message and print out the plain text
    * if the user picks (v)igenère:
        * ask for the key and the encrypted message
        * decrypt the message and print out the plain text
    * if the user does not pick s or v
        * print out an error message
        * ask for a new command, encrypt or decrypt
4. If the user types in q, end the program
5. If the user types in any other letter
    * print out and error message
    * ask for a new command, encrypt or decrypt

Example Interaction
-----
TOP SECRET SPY STUFF!
Hi... would you like to (e)ncrypt or (d)ecrypt a message.. or (q)uit?
> e
What cipher would you like to use: (v)igenère or (s)ubstitution)
> v
Enter a key to encrypt your message with
> DAVINCI
Enter a message to encrypt
> the eagle has landed
whz rcooe pnu oailrf
Hi... would you like to (e)ncrypt or (d)ecrypt a message.. or (q)uit?
> d
What cipher would you like to use: (v)igenère or (s)ubstitution)
> v
Enter a key to encrypt your message with
> DAVINCI
Enter a message to encrypt
> whz rcooe pnu oailrf
the eagle has landed
"""
