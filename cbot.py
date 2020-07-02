from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['Hello %1 !']],
    ['(hey|hello|hi)', ['Hello sir ! how can i help you ?']],
    ['(.*) name', ['my name is MR. WICK, the chatbot of focus.']],
    ['(.*) created you', ['I was created by Yash Raj']],
    ['((.*)help(.*)|help)', ['Currently cannot help due to under development phase']]
 ]
chat = Chat(pairs, reflections)
chat.converse()