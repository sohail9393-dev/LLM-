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

import tiktoken

# Initialize the encodings for GPT-2, GPT-3, and GPT-4
encodings = {
    "gpt2": tiktoken.get_encoding("gpt2"),
    "gpt3": tiktoken.get_encoding("p50k_base"),  # Commonly associated with GPT-3 models
    "gpt4": tiktoken.get_encoding("cl100k_base")  # Used for GPT-4 and later versions
}

# Get the vocabulary size for each encoding
vocab_sizes = {model: encoding.n_vocab for model, encoding in encodings.items()}

# Print the vocabulary sizes
for model, size in vocab_sizes.items():
    print(f"The vocabulary size for {model.upper()} is: {size}")


# CREATING INPUT TARGET PAIRS

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

enc_text = tokenizer.encode(raw_text)
print(len(enc_text))

enc_sample = enc_text[50:]

context_size = 4 #length of the input
#The context_size of 4 means that the model is trained to look at a sequence of 4 words (or tokens) 
#to predict the next word in the sequence. 
#The input x is the first 4 tokens [1, 2, 3, 4], and the target y is the next 4 tokens [2, 3, 4, 5]

x = enc_sample[:context_size]# Take the first 4 tokens as input sequence (x)
y = enc_sample[1:context_size+1]# Take the next 4 tokens (shifted by one position) as target sequence (y)

print(f"x: {x}")# Print the input sequence (x)
print(f"y:      {y}")# Print the target sequence (y) aligned for clarity

for i in range(1, context_size+1):# Loop through 1 to context_size (inclusive)
    context = enc_sample[:i]# Get a growing context (from the first token up to i)
    desired = enc_sample[i]# The desired next token is the one immediately after the context

    print(context, "---->", desired)

for i in range(1, context_size+1):# Repeat the loop, but this time decode tokens back to text
    context = enc_sample[:i]# Get the same context sequence
    desired = enc_sample[i]# Get the same desired next token

    print(tokenizer.decode(context), "---->", tokenizer.decode([desired])) # Print the decoded text of context and the decoded desired token

from torch.utils.data import Dataset, DataLoader  # Import Dataset and DataLoader

class GPTDatasetV1(Dataset):
    def __init__(self, txt, tokenizer, max_length, stride):
        self.input_ids = []
        self.target_ids = []

        # Tokenize the entire text
        token_ids = tokenizer.encode(txt, allowed_special={"<|endoftext|>"})

        # Use a sliding window to chunk the book into overlapping sequences of max_length
        for i in range(0, len(token_ids) - max_length, stride):
            input_chunk = token_ids[i:i + max_length]
            target_chunk = token_ids[i + 1: i + max_length + 1]
            self.input_ids.append(torch.tensor(input_chunk))
            self.target_ids.append(torch.tensor(target_chunk))

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]

def create_dataloader_v1(txt, batch_size=4, max_length=256, 
                         stride=128, shuffle=True, drop_last=True,
                         num_workers=0):

    # Initialize the tokenizer
    tokenizer = tiktoken.get_encoding("gpt2")

    # Create dataset
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)

    # Create dataloader
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last,
        num_workers=num_workers
    )

    return dataloader


with open("the-verdict.txt", "r", encoding="utf-8") as f:  # Open file for reading
    raw_text = f.read()  # Read file content
# It only gives us the input output pair


import torch  # Import torch
print("PyTorch version:", torch.__version__)  # Print PyTorch version
dataloader = create_dataloader_v1(
    raw_text, batch_size=1, max_length=4, stride=1, shuffle=False
)  # Create dataloader

data_iter = iter(dataloader)  # Get iterator
first_batch = next(data_iter)  # Get first batch
print(first_batch)  # Print first batch

second_batch = next(data_iter)  # Get second batch
print(second_batch)  # Print second batch

dataloader = create_dataloader_v1(raw_text, batch_size=8, max_length=4, stride=4, shuffle=False)  # Create dataloader

data_iter = iter(dataloader)  # Get iterator
inputs, targets = next(data_iter)  # Get inputs and targets
print("Inputs:\n", inputs)  # Print inputs
print("\nTargets:\n", targets)  # Print targets

# IN THIS LEC. WE ARE GOING TO CREATE TOKEN EMBEDDINGS
input_ids = torch.tensor([2, 3, 5, 1])  # Example token ids

vocab_size = 6  # Set vocabulary size
output_dim = 3  # Set output dimension

torch.manual_seed(123)  # Set random seed
embedding_layer = torch.nn.Embedding(vocab_size, output_dim)  # Create embedding layer

print(embedding_layer.weight)  # Print embedding weights

print(embedding_layer(torch.tensor([3])))  # Print embedding for token 3

print(embedding_layer(input_ids))  # Print embeddings for input ids

# LECTURE NUMBER 11 STARTS FROM HERE
# IN THIS LEC. WE ARE GOING TO CREATE POSITIONAL VECTOR EMBEDDINGS

vocab_size = 50257  # Set vocabulary size
output_dim = 256  # Set output dimension
token_embedding_layer = torch.nn.Embedding(vocab_size, output_dim)  # Create token embedding layer

max_length = 4  # Set max sequence length
dataloader = create_dataloader_v1(
    raw_text, batch_size=8, max_length=max_length,
    stride=max_length, shuffle=False 
)  # Create dataloader
data_iter = iter(dataloader)  # Get iterator
inputs, targets = next(data_iter)  # Get inputs and targets

print("Token IDs:\n", inputs)  # Print token ids
print("\nInputs shape:\n", inputs.shape)  # Print input shape

token_embeddings = token_embedding_layer(inputs)  # Get token embeddings
print(token_embeddings.shape)  # Print shape of token embeddings

context_length = max_length  # Set context length
pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)  # Create positional embedding layer


pos_embeddings = pos_embedding_layer(torch.arange(max_length))  # Get positional embeddings
print(pos_embeddings.shape)  # Print shape of positional embeddings

input_embeddings = token_embeddings + pos_embeddings  # Add token and positional embeddings
print(input_embeddings.shape)  # Print shape of input embeddings

import torch  # Import torch

inputs = torch.tensor(
  [[0.43, 0.15, 0.89], # Your     (x^1)
   [0.55, 0.87, 0.66], # journey  (x^2)
   [0.57, 0.85, 0.64], # starts   (x^3)
   [0.22, 0.58, 0.33], # with     (x^4)
   [0.77, 0.25, 0.10], # one      (x^5)
   [0.05, 0.80, 0.55]] # step     (x^6)
)  # Example input embeddings

import matplotlib.pyplot as plt  # Import matplotlib
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting toolkit

# Corresponding words
words = ['Your', 'journey', 'starts', 'with', 'one', 'step']  # List of words

# Extract x, y, z coordinates
x_coords = inputs[:, 0].numpy()  # Get x coordinates
y_coords = inputs[:, 1].numpy()  # Get y coordinates
z_coords = inputs[:, 2].numpy()  # Get z coordinates

# Create 3D plot
fig = plt.figure()  # Create figure
ax = fig.add_subplot(111, projection='3d')  # Add 3D subplot

# Plot each point and annotate with corresponding word
for x, y, z, word in zip(x_coords, y_coords, z_coords, words):  # Loop over points
    ax.scatter(x, y, z)  # Plot point
    ax.text(x, y, z, word, fontsize=10)  # Annotate point

# Set labels for axes
ax.set_xlabel('X')  # Set x label
ax.set_ylabel('Y')  # Set y label
ax.set_zlabel('Z')  # Set z label

plt.title('3D Plot of Word Embeddings')  # Set plot title
plt.show()  # Show plot

attn_scores = torch.empty(6, 6)  # Create empty attention scores tensor

for i, x_i in enumerate(inputs):  # Loop over inputs
    for j, x_j in enumerate(inputs):  # Loop over inputs
        attn_scores[i, j] = torch.dot(x_i, x_j)  # Compute dot product

print(attn_scores)  # Print attention scores

attn_weights = torch.softmax(attn_scores, dim=-1)  # Compute softmax weights
print(attn_weights)  # Print attention weights

row_2_sum = sum([0.1385, 0.2379, 0.2333, 0.1240, 0.1082, 0.1581])  # Sum of row 2
print("Row 2 sum:", row_2_sum)  # Print row 2 sum
print("All row sums:", attn_weights.sum(dim=-1))  # Print all row sums