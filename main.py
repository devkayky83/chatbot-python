from bot.chatbot import bot_answer

messages = []

print("\nWelcome to Keiki.Bot")

while True:
    question = input('\nUsuário: ')
    if question.lower() == 'x':
        break
    messages.append(('user', question))
    answer = bot_answer(messages)
    messages.append(('assistant', answer))
    print('-' * 140)
    print(f'\nKeiki: {answer}')

print('\nThank you for using Keiki.Bot!')