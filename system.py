import os

def counting_words(text): #function to count the words
    word_count = {}
    words = text.split() #converting a sentence into words
    for word in words:
        word = word.strip(".,!'?[]").lower() #converting the string into lower and removing all symbols or special characters
        if word:
            word_count[word] = word_count.get(word,0)+1
    return word_count


def file_info(file_name,content): #function to get the file
    print(f"File: {file_name}")
    print("Content:")
    print(content)
    print(f"Word Count:{len(content.split())}")

    word_count = counting_words(content)
    if word_count:
        print("Word Recurrence: ")
        for word,count in word_count.items():
            print(f"{word} : {count}")
    else:
        print("No recuring words found")

if __name__ == "__main__":

# Created an empty dictionary to store content
    file_content = {}
    # Using for loop to iterate through the given directory
    for filename in os.listdir(): #os.listdir gets the list of filenames in the current directory
        if filename.endswith(".txt"):
            with open(filename, "r") as file:
                content = file.read()
                file_content[filename] = content
    
    while True:
        file_name = input("Enter the name of the file(or 'quit' to exit): ")
        if file_name == 'quit':
            break
        content = file_content.get(file_name)
        if content:
            file_info(file_name,content)
        else:
            print(f"File '{file_name}' not found in the database")


    
    
