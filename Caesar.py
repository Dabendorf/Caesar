import sys

def main():
	# Read the shift
	if len(sys.argv) < 2:
		print("Error: No shift parameter provided")
		return
	
	shift_val = sys.argv[1]
	
	try:
		shift_val = int(shift_val)
	except ValueError:
		print("Error: the shift parameter is not an integer")
		return
	
	print(shift_val)

	# some fancy reading function which returns a flattended array of words (words are split by space and newline)
	original = [word for line in sys.stdin.readlines() for word in line.strip().split(" ") if word!= ""]
	#print(original)

	encrypted = [caesar(word, shift_val) for word in original]
	#print(encrypted)

	decrypted = [caesar(word, -shift_val) for word in encrypted]
	#print(decrypted)

	# Check if the decrypted-encrypted-value is the same as the original one
	print(" ".join(original) == " ".join(decrypted))
	print(" ".join(original))
	print(" ".join(decrypted))

	# Write to file
	with open("Output.txt", "w") as output_file:
		output_file.write(" ".join(encrypted))

def caesar(word, shift):
	encrypted_word = []
	for letter in word:
		new_letter = chr((ord(letter) + shift) % 128)
		encrypted_word.append(new_letter)
	return ''.join(encrypted_word)


if __name__ == "__main__":
	main()
