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