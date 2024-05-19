# Caesar
This programmes takes a text and encrypts it by using caesar encryption.

## Criticism of the task
At first, I would like to mention that the task was horribly described. It does not describe what the actual array should show in the end and it doesn't tell me either, if the result should be the transformation from the original to the 5000th iteration, or if there shoudl be output for intermediate encryptions as well. The examples are very confusing since one originally things they have something to do with the task, yet they just appear to be example texts to be encrypted? 

Also, remember that running an encryption 5000 times shouldn't make an encryption any better, when chosing an encryption algorithm, one should actually chose one which is save(-ish) after one iteration.

## My algoritm
I chose to implement the caesar algoritm since it is **the** standard example of all algorithms and the weather in Bergen was too good to implement something else. It somehow ridicules what I wrote in the upper chapter about algorithms being unsecure when running them multiple times over themselves, since it might be the case that choosing a specific shifting value for caesar combined with 5000 iterations results in receiving the same text as the original one.

Other algorithms one could have choosen are:
* Vignere: a different caesar algorithm for each letter, yet equally useless as caesar or ROT13
* the identity algorithm: Return the text itself. Its technically an encryption
* AES, DES, RSA, DSA: some of the fancy (secure) algorithms; but one should actually use a library for this anyway
* Enigma: I would have fancied to implement this one day, but lacked time this time

## Usage
``python3 Caesar.py 5 < Input1.txt``
The command will write to a file named `Output.txt`
It will return an error message if there is no provided shift parameter

I choose to only convert ASCII-characters, so if there is some funy stuff like emojis or the irritating accent symbol from the second text, it will behave differently