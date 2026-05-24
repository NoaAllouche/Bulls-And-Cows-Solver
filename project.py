# Noa Allouche (216369140), Noya Laniado (212673925)


import random

# Creating all the possible codes
def generate_unique_digit_strings(num_digits: int = 4, vocabulary: str = "0123456789") -> list:
    temp_candidates = []
    if num_digits == 0:
        return []
    if num_digits == 1:
        temp_candidates.append(vocabulary)
        return temp_candidates
    total_options = len(vocabulary) ** num_digits

    for num in range(total_options):
        code = ""
        for j in range(num_digits):
            code = vocabulary[num % len(vocabulary)] + code
            num //= len(vocabulary)
        temp_candidates.append(code)

    candidates = []
    for code in temp_candidates:
        if len(set(code)) == len(code):
            candidates.append(code)

    return sorted(candidates)

def test_generate_unique_digit_strings():
    if generate_unique_digit_strings(0, '123456') != []:
        print("Test 1 failed: there is no code for secret")
    elif generate_unique_digit_strings(1, '456789') != ['4','5','6','7','8','9']:
        print("Test 2 failed: code that is only one digit long")
    elif generate_unique_digit_strings(2) != ['01', '02', '03', ..., '97', '98', '99', '10', '12', '13', ..., '98']:
        print("Test 3 failed: '0123456789' is the default vocabulary")
    else:
        print("All test cases passed")


# Checking if the guess is the same as the secret
def evaluate(secret: str, guess: str) -> tuple:
    bulls = 0
    cows = 0
    guess_remaining = []
    secret_remaining = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        else:
            guess_remaining.append(guess[i])
            secret_remaining.append(secret[i])
    for j in set(guess_remaining):
        cows += min(guess_remaining.count(j), secret_remaining.count(j))

    return (bulls, cows)

def test_evaluate():
    if evaluate('435','234') != (1,1):
        print("Test 1 failed: one digit in guess in the right place and one digit in guess is right but not in the right place")
    elif evaluate('35','34') != (1,0):
        print("Test 2 failed: one digit in both codes in the right place")
    elif evaluate('245','345') != (2,0):
        print("Test 3 failed: two digits in both codes in the right place")
    elif evaluate('4567','4567') != (4,0):
        print("Test 4 failed: secret and guess identical")
    else:
        print("All test cases passed")


# Filtering the matching candidates
def filter_candidates(candidates: list, guess: str, feedback: tuple) -> list:
    filtered_candidates = []
    for code in candidates:
        if evaluate(code, guess) == feedback:
            filtered_candidates.append(code)
    return filtered_candidates

def test_filter_candidates():
    if filter_candidates(['08','12','13','19'], '12', (0,1)) != ['12','13','19']:
        print("Test 1 failed: 3 feedbacks from the candidates match the guess feedback")
    elif filter_candidates(['012','013','014','015'], '015', (2,0)) != ['012','013','014','015']:
        print("Test 2 failed: all the feedbacks from the candidates match the guess feedback")
    elif filter_candidates(['75','89'], '89', (0,0)) != ['75']:
        print("Test 3 failed: only one code math the guess feedback")
    else:
        print("All test cases passed")


# Checking if the secret is valid
def check_secret(candidates: list, secret: str) -> bool:
    if secret in candidates and len(secret) == digits_num and len(set(secret)) == len(secret):
        return True
    else:
        return False

def test_check_secret():
    if check_secret(['01','02','05'], '52') != False:
        print("Test 1 failed: secret not in candidates")
    elif check_secret(['0123','123','023','321','120'], '00112') != False:
        print("Test 2 failed: length of secret different than then the guess")
    elif check_secret(['89','87','76','65','54'], '123') != False:
        print("Test 3 failed: secret not in candidates and length of secret different than then the guess")
    elif check_secret(['6544','4522','8522'], '4522') != True:
        print("Test 4 failed: secret in candidates and in the right length")
    else:
        print("All test cases passed")


# Getting candidates
def get_candidate(candidates: list, strategy: str = 'first') -> str:
    if strategy == 'first':
        return candidates[0]
    elif strategy == 'random':
        return random.choice(candidates)
    elif strategy == 'knuth':
        return get_best_knuth_guess(candidates)

def test_get_candidate():
    # for 'random' - every test will be correct
    if get_candidate(['01', '12', '13', '14'], 'first') != '01':
        print("Test 1 failed: not the first code on the list")
    elif get_candidate(['789','521', '546','785'], 'knuth') != '521':
        print("Test 2 failed: not the best knuth guess")
    elif get_candidate(['0152', '1572', '4113', '9514']) != '0152':
        print("Test 3 failed: Not the first code on the list ('first' is the default)")
    else:
        print("All test cases passed")


# Getting candidates with Knuth algorithm
def get_best_knuth_guess(candidates: list):
    v_min = float('inf')
    f_min = None
    for c in candidates:
        feedback_dict = {}
        for s in candidates:
            feedback = evaluate(s, c)
            if feedback in feedback_dict:
                feedback_dict[feedback] += 1
            else:
                feedback_dict[feedback] = 1
        f_min_curr = max(feedback_dict.values())
        if f_min_curr < v_min:
            v_min = f_min_curr
            f_min = c

    return f_min

def test_get_best_knuth_guess():
    if get_best_knuth_guess(['789', '521', '546', '785']) != '521':
        print("Test 1 failed: not the guess that minimizes the worst-case feedback group size")
    elif get_best_knuth_guess(['01', '10', '23', '32']) != '01':
        print("Test 2 failed: not the guess that best splits the candidates by feedback")
    elif get_best_knuth_guess(['12', '21']) not in ['12', '21']:
        print("Test 3 failed: result is not one of the valid candidates when all give same feedback")
    else:
        print("All test cases passed")


# MAIN
random.seed(1)
vocabulary = str(input())
digits_num = int(input())
if digits_num < 2 or digits_num > 5:
    print()
    digits_num = int(input())
strategy = str(input())
secret = str(input())
candidates = generate_unique_digit_strings(digits_num, vocabulary)

if not check_secret(candidates, secret):
    print("illegal secret")
    exit()

#steps = 0
guess = get_candidate(candidates, strategy)
feedback = evaluate(secret, guess)

steps = 1
if feedback == (digits_num, 0):
    print(secret, steps)
    exit()
while feedback != (digits_num, 0):
    candidates = filter_candidates(candidates, guess, feedback)
    if not candidates:
        print("No candidates left. Something went wrong with filtering.")
        exit()
    guess = get_candidate(candidates, strategy)
    feedback = evaluate(secret, guess)
    steps += 1

print(secret, steps)