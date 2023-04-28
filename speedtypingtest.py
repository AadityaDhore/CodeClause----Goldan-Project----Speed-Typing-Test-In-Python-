import time

def typing_speed_test():
    prompt = "Jay Hind"
    print("Type this: \"" + prompt + "\"")

    start_time = time.time()
    user_input = input()

    end_time = time.time()
    time_elapsed = end_time - start_time

    words_typed = len(user_input.split())
    speed = words_typed / time_elapsed * 60

    print("You typed", words_typed, "words in", round(time_elapsed, 2), "seconds.")
    print("Your typing speed is", round(speed, 2), "words per minute.")

typing_speed_test()