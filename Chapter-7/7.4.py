def eval_loop():
    while True:
        user_input = raw_input()
        if user_input == 'done':
            break
        print eval(user_input)

eval_loop()
