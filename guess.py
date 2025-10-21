def play_once(low: int = LOW, high: int = HIGH) -> int:
    """Play one round of the guessing game. Returns number of tries this round."""
    """The player tries to guess a randomly selected number between the parameters `low` and `high`.
    Returns the number of attempts the player took to guess correctly or to give up."""

    # --- Step 2: Difficulty selection ---
    DIFFICULTIES = {
        "easy": (1, 50, 10),
        "medium": (1, 100, 7),
        "hard": (1, 200, 5)
    }
    choice = input("Choose difficulty (easy, medium, hard): ").lower()
    low, high, max_tries = DIFFICULTIES.get(choice, (low, high, MAX_TRIES))
    # --------------------------------------

    secret = random.randint(low, high)
    # Displays the game intro line (colored if c() exists)
    try:
        print(c(f"I'm thinking of a number between {low} and {high}. You have {max_tries} attempts. (Type 'q' to give up)", "96"))
    except NameError:
        print(f"I'm thinking of a number between {low} and {high}. You have {max_tries} attempts.")

    tries = 0
    # Continues looping guesses until the player runs out of attempts
    while tries < max_tries:
        result = read_int("Your guess: ")   # may be int or None if user typed 'q'
        # Handles user quitting the game
        if result is None:
            try:
                print(c(f"You gave up! The correct number was {secret}.", "95"))
            except NameError:
                print(f"You gave up! The correct number was {secret}.")
            return tries

        guess = result
        tries += 1

        # Makes sure the guess is within the given range
        if guess < low or guess > high:
            try:
                print(c(f"Out of range! Guess between {low} and {high}.", "95"))
            except NameError:
                print(f"Out of range! Guess between {low} and {high}.")
            continue # skips to the next iteration without counting the current iteration as a valid attempt

        # Gives feedback based on how close the guess is, based on the difference between the guess and the actual number
        diff = abs(guess - secret)
        try:
            if diff <= 3:
                print(c("🔥 Very close!", "92"))      # Green - guess is within 3 units of the secret number
            elif diff <= 10:
                print(c("🙂 Close!", "94"))           # blue - guess is within 10 units of the secret number
            else:
                print(c("❄️ Way off!", "90"))         # gray - guess is more than 10 units away from the secret number
        except NameError:
            if diff <= 3:
                print("Very close!")
            elif diff <= 10:
                print("Close!")
            else:
                print("Way off!")

        # High/low hints
        if guess < secret:
            try:
                print(c("Too low!", "93"))            # yellow
            except NameError:
                print("Too low!")
        elif guess > secret:
            try:
                print(c("Too high!", "93"))           # yellow
            except NameError:
                print("Too high!")
        else:
            try:
                print(c(f"Correct! You got it in {tries} tries.", "92"))  # green
            except NameError:
                print(f"Correct! You got it in {tries} tries.")
            return tries

    # Out of attempts
    try:
        print(c(f"Out of attempts! The correct number was {secret}.", "91"))  # red
    except NameError:
        print(f"Out of attempts! The correct number was {secret}.")

    return tries # returns the total number of tries it took to guess the secret number
