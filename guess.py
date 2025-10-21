def play_once(low: int = LOW, high: int = HIGH) -> int:

    # Makes sure the range between low and high is valid to prevent errors

    if low > high:

        print("Sorry, the range between the low and high bars is invalid")

        return -1
 
    """

    Play one round of the guessing game. Returns number of tries this round.

    The player tries to guess a randomly selected number between `low` and `high`.

    """
 
    secret = random.randint(low, high)

    try:

        print(c(f"I'm thinking of a number between {low} and {high}. You have {MAX_TRIES} attempts. (Type 'q' to give up)", "96"))

    except NameError:

        print(f"I'm thinking of a number between {low} and {high}. You have {MAX_TRIES} attempts.")
 
    tries = 0

    while tries < MAX_TRIES:

        result = read_int("Your guess: ")  # may be int or None if user typed 'q'
 
        # ✅ Suggestion #1 — Add explicit input validation

        if result is None or not isinstance(result, int):

            print("Invalid input! Please enter a number or 'q' to quit.")

            continue
 
        guess = result
 
        if guess < low or guess > high:

            try:

                print(c(f"Out of range! Guess between {low} and {high}.", "95"))

            except NameError:

                print(f"Out of range! Guess between {low} and {high}.")

            continue
 
        tries += 1

        diff = abs(guess - secret)

        try:

            if diff <= 3:

                print(c("🔥 Very close!", "92"))

            elif diff <= 10:

                print(c("🙂 Close!", "94"))

            else:

                print(c("❄️ Way off!", "90"))

        except NameError:

            if diff <= 3:

                print("Very close!")

            elif diff <= 10:

                print("Close!")

            else:

                print("Way off!")
 
        if guess < secret:

            try:

                print(c("Too low!", "93"))

            except NameError:

                print("Too low!")

        elif guess > secret:

            try:

                print(c("Too high!", "93"))

            except NameError:

                print("Too high!")

        else:

            try:

                print(c(f"Correct! You got it in {tries} tries.", "92"))

            except NameError:

                print(f"Correct! You got it in {tries} tries.")

            return tries
 
    try:

        print(c(f"Out of attempts! The correct number was {secret}.", "91"))

    except NameError:

        print(f"Out of attempts! The correct number was {secret}.")

    return tries
 
