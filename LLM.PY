# Open the file 'the-verdict.txt' in read mode using UTF-8 encoding
with open("the-verdict.txt", "r", encoding="utf-8") as f:  # Open file for reading
    raw_text = f.read()  # Read the entire content of the file into the variable 'raw_text'

# Print the total number of characters in the loaded text
print("Total number of character:", len(raw_text))  # Print character count
# Print the first 99 characters of the loaded text to preview its content
print(raw_text[:99])  # Print preview of text

# Import the regular expressions module for text processing
import re  # Import regex module

# Example text for demonstrating tokenization
text = "Hello, world. This, is a test."  # Example string for splitting
# Split the text by whitespace, keeping the delimiter in the result
result = re.split(r'(\s)', text)  # Split by whitespace, keep delimiter

# Print the result of splitting by whitespace
print(result)  # Print split result
# Split the text by comma, period, or whitespace, keeping the delimiter in the result
result = re.split(r'([,.]|\s)', text)  # Split by punctuation or whitespace

# Print the result of splitting by punctuation and whitespace
print(result)  # Print split result
# Remove empty strings and whitespace-only items from the result
result = [item for item in result if item.strip()]  # Remove empty/whitespace items
# Print the cleaned result after removing empty/whitespace-only items
print(result)  # Print cleaned result
# Another example text for tokenization demonstration
text = "Hello, world. Is this-- a test?"  # New example string
# Split the text by punctuation, double dash, or whitespace, keeping the delimiter in the result
result = re.split(r'([,.:;?_!"()\']|--|\s)', text)  # Split by more punctuation
# Remove empty strings and whitespace-only items from the result
result = [item.strip() for item in result if item.strip()]  # Clean split result
# Print the cleaned result after removing empty/whitespace-only items
print(result)  # Print cleaned result
# Strip whitespace from each item and then filter out any empty strings.
result = [item for item in result if item.strip()]  # Remove empty/whitespace items
print(result)  # Print cleaned result
text = "Hello, world. Is this-- a test?"  # Example string

result = re.split(r'([,.:;?_!"()\']|--|\s)', text)  # Split by punctuation/whitespace
result = [item.strip() for item in result if item.strip()]  # Clean result
print(result)  # Print cleaned result
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)  # Split raw text
preprocessed = [item.strip() for item in preprocessed if item.strip()]  # Clean split
print(preprocessed[:30])  # Print first 30 tokens
print(len(preprocessed))  # Print total number of tokens
all_words = sorted(set(preprocessed))  # Get sorted unique tokens
vocab_size = len(all_words)  # Get vocabulary size

print(vocab_size)  # Print vocabulary size
vocab = {token:integer for integer,token in enumerate(all_words)}  # Map tokens to integers
for i, item in enumerate(vocab.items()):  # Iterate over vocab items
    print(item)  # Print vocab item
    if i >= 50:  # Stop after 50 items
        break
    class SimpleTokenizerV1:
     def __init__(self, vocab):  # Constructor
        self.str_to_int = vocab  # Token to integer mapping
        self.int_to_str = {i:s for s,i in vocab.items()}  # Integer to token mapping
    
     def encode(self, text):  # Encode text to token ids
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)  # Split text
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()  # Clean split
        ]
        ids = [self.str_to_int[s] for s in preprocessed]  # Map tokens to ids
        return ids  # Return ids
        
     def decode(self, ids):  # Decode ids to text
        text = " ".join([self.int_to_str[i] for i in ids])  # Join tokens
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)  # Clean up spaces
        return text  # Return decoded text
tokenizer = SimpleTokenizerV1(vocab)  # Instantiate tokenizer

text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

vocab = {token:integer for integer,token in enumerate(all_tokens)}
print(len(vocab.items()))
for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)

class SimpleTokenizerV2:
    def __init__(self, vocab):  # Constructor
        self.str_to_int = vocab  # Token to integer mapping
        self.int_to_str = { i:s for s,i in vocab.items()}  # Integer to token mapping
    
    def encode(self, text):  # Encode text to token ids
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)  # Split text
        preprocessed = [item.strip() for item in preprocessed if item.strip()]  # Clean split
        preprocessed = [
            item if item in self.str_to_int 
            else "<|unk|>" for item in preprocessed  # Replace unknown tokens
        ]

        ids = [self.str_to_int[s] for s in preprocessed]  # Map tokens to ids
        return ids  # Return ids
        
    def decode(self, ids):  # Decode ids to text
        text = " ".join([self.int_to_str[i] for i in ids])  # Join tokens
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)  # Clean up spaces
        return text  # Return decoded text
    
tokenizer = SimpleTokenizerV2(vocab)
# Initialize a simple tokenizer (your custom version) with a given vocabulary.

text1 = "Hello, do you like tea?"# First input text string.
text2 = "In the sunlit terraces of the palace."# Second input text string.

text = " <|endoftext|> ".join((text1, text2))
# Concatenate both texts with a special separator token <|endoftext|>.  
# This token is commonly used by GPT models to mark text boundaries.
print(text)# Print the combined text so you can see how it looks after joining.
tokenizer.encode(text)# Convert the text into a list of token IDs (integers) using your custom tokenizer.
tokenizer.decode(tokenizer.encode(text))
# Convert the token IDs back into text, verifying that encoding and decoding work properly.



# BYTE PAIR ENCODER

import importlib.metadata  # Import metadata module
import tiktoken  # Import tiktoken library
print("tiktoken version:", importlib.metadata.version("tiktoken"))
# Print the currently installed version of the tiktoken library.
tokenizer = tiktoken.get_encoding("gpt2")
# Load the GPT-2 tokenizer (uses Byte Pair Encoding).  
# This tokenizer knows how to split text into GPT-2 tokens.
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     "of someunknownPlace."
)
# Define an input text string that includes a special token <|endoftext|>  
# and a made-up word "someunknownPlace" to test how the tokenizer handles it.


integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
# Encode the text into token IDs (integers).  
# The 'allowed_special' argument ensures <|endoftext|> is kept as a special token.


print(integers)
# Print the tokenized output (a list of integers).  
# Each integer corresponds to a subword token from the GPT-2 vocabulary.


strings = tokenizer.decode(integers)
# Decode the list of token IDs back into a human-readable text string.
print(strings)
# Print the reconstructed text after decoding.  
