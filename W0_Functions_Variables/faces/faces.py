# Prompt the user to say something
user_input = input("Use an emoticon ")

# Now convert emoticons into emojis
user_output = user_input.replace(":)", "🙂").replace(":(", "🙁")

# Now print the final emoji
print(user_output)
