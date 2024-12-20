def text_filter(arg):
    banned_words = ["Turkey", "Dog", "Fox", "Cat","Chicken"]
    input_list = arg.lower().title().split()
    for i in banned_words:
        for j in input_list:
            if i == j:
                input_list.remove(j)
    output_message = " ".join(input_list)
    print(f'Input Message: {arg}\nOutput Message: {output_message}')
input_message = input('>: ')
text_filter(input_message)