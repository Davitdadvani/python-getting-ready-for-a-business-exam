import math
import random
import time
import threading
import sys


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 100
    return 0

def play_slots(balance):
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    weights = [40, 25, 20, 10, 5]

    while True:
        print(f' Current Balance: ${balance} ---')
        bet_input = input('Place your bet amount: ')
        if not bet_input.isdigit():
            print('Please enter a valid number.')
            continue
        bet = int(bet_input)
        if bet > balance:
            print(f'Cap u cant bet more than u have. You only have ${balance}.')
            continue
        if bet <= 0:
            print('Bet must be greater than 0 twin.')
            continue
        break

    balance -= bet
    row = random.choices(symbols, weights=weights, k=3)

    print(f'Result: {" ".join(row)}')

    payout = get_payout(row, bet)
    new_balance = balance + payout
    net_loss = bet - payout

    if net_loss >= 50: difficulty = 'HARD'
    elif net_loss >= 15: difficulty = 'MEDIUM'
    else: difficulty = 'EASY'

    if payout > 0:
        print(f'You survived twin! Payout: ${payout}')
    else:
        print(f'LOSER, HAHAHAH GG! You lost ${bet}')

    print(f'Difficulty set to: {difficulty}')
    return difficulty, new_balance

def math_warmup(difficulty):
    print(f' Math Warmup ({difficulty}) ---')
    if difficulty == 'HARD': low, high = 50, 100
    elif difficulty == 'MEDIUM': low, high = 20, 50
    else: low, high = 1, 20

    for i in range(5):
        operators = ['+', '-', '*']
        op = random.choice(operators)
        a, b = random.randint(low, high), random.randint(low, high)
        try:
            ans = int(input(f'Question {i+1}: What is {a} {op} {b}? '))
            if op == '+': correct = a + b
            elif op == '-': correct = a - b
            else: correct = a * b
            if ans == correct: print('Correct!')
            else: print(f'Incorrect. It was {correct}.')
        except ValueError:
            print('Invalid input. Counting as incorrect.')

def main_quiz():
    time_limit = 1800
    time_up = False

    def timer_func():
        nonlocal time_up
        time.sleep(time_limit)
        time_up = True
        print('TIME IS UP CUH! Finish this question to see results.')

    timer_thread = threading.Thread(target=timer_func, daemon=True)
    timer_thread.start()
    print('QUIZ 30-MINUTE TIMER STARTED NOW ')

    print('Starting Business Quiz...')

    questions = [
        'What is the definition of a business?', "How is 'adding value' described in a business system?",
        "What is the definition of profit?", 'Which of the following is a primary benefit of competition for customers?',
        'What defines a competitive advantage?', 'How do nonprofit organizations differ from businesses?',
        'What does effectiveness mean in organizations?', 'How is efficiency defined in business?',
        'Which characteristic is unique to service businesses?', 'What are tangible goods?',
        'Why are goods producing businesses capital intensive?', 'What is an entry barrier?',
        'Who are stakeholders?', 'What are disruptive technologies?',
        'Which environment affects labor costs and supply?', 'What characterizes the legal environment?',
        'Which department sets product prices and identifies market opportunities?', 'What is the main role of research and development?',
        'Which function ensures the company has money to operate?', 'What is the main responsibility of human resources?',
        'What is economics?', 'What does microeconomics study?',
        'Which is a factor of production?', 'What is scarcity?',
        'What is opportunity cost?', 'What defines capitalism?',
        'What does it mean to nationalize an industry?', 'What defines a sellers market?',
        'What happens at market equilibrium?', 'What does GDP measure?',
        'What is the purpose of a value chain?', 'What value does a manufacturer add in a furniture value chain?',
        'What value does a retailer add in a value chain?', 'What risk occurs when companies reduce prices aggressively?',
        'What is the goal of cost leadership?', 'What is product differentiation?',
        'Why might higher revenue not increase profit?', 'What does lean manufacturing reduce?',
        'What is strategic sourcing?', 'Which industry provides financial security services?',
        'What is a major barrier to entry in the coffee shop example?', 'What role did securitization play in the 2008 crisis?',
        'What is moral hazard?', 'What does opportunity cost represent?',
        'Why do higher gas prices reduce grill demand?', 'Why does Deutsche Bahn face unique challenges?',
        'What is frictional unemployment?', 'What is structural unemployment?',
        'What problem occurred at FlexCorp with remote work?', 'What is the purpose of hybrid work?',
        'What risk exists with extremely generous customer service?', 'What is the least risky international expansion strategy?',
        'What does foreign direct investment involve?', 'What is the principal agent problem?',
        'What solution reduces agency problems?', 'What is a disadvantage of sole proprietorship?',
        'What is an advantage of corporations?', 'What is the difference between first mover and fast follower?',
        'What role do management dashboards support?', "What leadership lesson comes from Dyson's prototype story?"
    ]

    answers = [
        ['A Government agency', 'B Social club', 'C Profit seeking organization selling goods or services', 'D Nonprofit group'],
        ['A Transform inputs into higher value outputs', 'B Reduce wages', 'C Increase advertising', 'D Lower quality'],
        ['A Total revenue', 'B Investment capital', 'C Raw material cost', 'D Revenue minus costs'],
        ['A Fewer choices', 'B Better customer service', 'C Higher prices', 'D Lower quality'],
        ['A Feature making product more attractive', 'B Most expensive product', 'C No competitors', 'D Highest profit'],
        ['A No customers', 'B No management', 'C Government owned', 'D No profit motive'],
        ['A Achieving goals', 'B Using resources well', 'C Doing things right', 'D Minimizing waste'],
        ['A Achieving goals', 'B Total revenue', 'C Using resources efficiently', 'D Number of products'],
        ['A Physical ownership', 'B Intangible value creation', 'C Physical product', 'D Inventory'],
        ['A Digital products', 'B Software', 'C Insurance', 'D Physical goods'],
        ['A Human labor', 'B Intangible goods', 'C Requires large investment', 'D No barriers'],
        ['A Marketing tactic', 'B Requirement to enter market', 'C Government tax', 'D Economic cycle'],
        ['A Groups affected by business decisions', 'B Only owners', 'C Only customers', 'D Only regulators'],
        ['A Small improvements', 'B Rare materials', 'C Manufacturing machines', 'D Industry changing technology'],
        ['A Social environment', 'B Technology environment', 'C Economic environment', 'D Legal environment'],
        ['A Population trends', 'B Laws and regulations', 'C Technology use', 'D Competition'],
        ['A Marketing', 'B Production', 'C Accounting', 'D HR'],
        ['A Reselling products', 'B Hiring employees', 'C Creating innovations', 'D Auditing finances'],
        ['A Marketing', 'B Customer service', 'C Operations', 'D Finance'],
        ['A Recruiting and supporting employees', 'B Market research', 'C Product design', 'D Equipment maintenance'],
        ['A Study of psychology', 'B History of trade', 'C Study of scarce resources', 'D Corporate law'],
        ['A Unemployment rates', 'B Government policy', 'C Trade patterns', 'D Consumer and business decisions'],
        ['A Entrepreneurship', 'B Advertising', 'C Customer feedback', 'D Sales volume'],
        ['A Unlimited resources', 'B Limited resources', 'C High demand', 'D Low prices'],
        ['A Price', 'B Production cost', 'C Revenue', 'D Value of best alternative lost'],
        ['A Economic freedom and competition', 'B Government ownership', 'C No private property', 'D Central planning'],
        ['A Selling state firms', 'B Reducing regulation', 'C Government takeover', 'D Free trade'],
        ['A Supply greater than demand', 'B Prices falling', 'C High competition', 'D Demand greater than supply'],
        ['A Highest price', 'B Supply equals demand', 'C Lowest price', 'D Bankruptcy point'],
        ['A Imports', 'B Businesses', 'C Final goods value', 'D Average income'],
        ['A Coordinate value creating activities', 'B Remove intermediaries', 'C Eliminate competition', 'D Standardize cost'],
        ['A Supply raw materials', 'B Convert timber to furniture', 'C Deliver products', 'D Price goods'],
        ['A Manufacturing', 'B Market access and service', 'C Timber harvesting', 'D Machine design'],
        ['A Lower costs', 'B Brand growth', 'C Brand damage', 'D Efficiency'],
        ['A Lowest operating cost', 'B Luxury products', 'C High marketing', 'D Limited production'],
        ['A Lower wages', 'B Unique product features', 'C Increase output', 'D Reduce marketing'],
        ['A Wage increases', 'B Rising costs', 'C Low demand', 'D Taxes'],
        ['A Advertising', 'B Waste', 'C Variety', 'D Labor'],
        ['A Improve supplier contracts', 'B Remove supply chain', 'C Train employees', 'D Outsource marketing'],
        ['A Automobile', 'B Banking', 'C Agriculture', 'D Manufacturing'],
        ['A Low demand', 'B High startup cost', 'C No suppliers', 'D Illegal business'],
        ['A Bundled risky mortgages', 'B Reduced housing price', 'C Stopped risk', 'D Prevented failure'],
        ['A Avoid risk', 'B Risk taking expecting bailout', 'C Consumer refusal', 'D Government restriction'],
        ['A Hiring cost', 'B Lost potential alternative', 'C Production cost', 'D R&D spending'],
        ['A Electricity use', 'B Complementary goods', 'C No relation', 'D Price increase'],
        ['A Balance profit and public service', 'B No government funding', 'C No competition', 'D Only international'],
        ['A Tech job loss', 'B Temporary job search', 'C Seasonal work', 'D Retirement'],
        ['A Job search', 'B Technology skill mismatch', 'C Seasonal layoffs', 'D Retirement'],
        ['A Heavy workload', 'B Communication issues', 'C Lack of tools', 'D Low salary'],
        ['A Remove office work', 'B Balance flexibility and teamwork', 'C Expand offices', 'D Reduce autonomy'],
        ['A Low motivation', 'B Unrealistic customer expectations', 'C Poor quality', 'D More production'],
        ['A Build factories abroad', 'B Export products', 'C Buy competitors', 'D Hire foreign managers'],
        ['A Export goods', 'B Invest in foreign operations', 'C License products', 'D Outsource factories'],
        ['A Owner manager conflict', 'B Employee conflict', 'C Government policy', 'D Demand shifts'],
        ['A Longer hours', 'B Performance monitoring', 'C Salary cuts', 'D No freelancers'],
        ['A Unlimited liability', 'B No decisions', 'C Government ownership', 'D High turnover'],
        ['A Personal liability', 'B Transfer impossible', 'C Limited liability', 'D No regulation'],
        ['A Enter market early', 'B Avoid markets', 'C Wait always', 'D Reduce R&D'],
        ['A Avoid mistakes by observing competitors', 'B Launch innovation first', 'C Avoid innovation', 'D Remove competition'],
        ['A Leadership role', 'B Information support', 'C Recruiting', 'D Marketing'],
        ['A Persistence and resilience', 'B No experimentation', 'C Immediate success', 'D Low support']
    ]

    correct_answers = [
        'C','A','D','B','A','D','A','C','B','D',
        'C','B','A','D','C','B','A','C','D','A',
        'C','D','A','B','D','A','C','D','B','C',
        'A','B','B','C','A','B','B','B','A','B',
        'B','A','B','B','B','A','B','B','B','B',
        'B','B','B','A','B','A','C','A','B','A'
    ]

    quiz_data = list(zip(questions, answers, correct_answers))
    random.shuffle(quiz_data)
    questions, answers, correct_answers = zip(*quiz_data)

    score = 0
    total_q = len(questions)

    for i in range(total_q):
        if time_up:
            print('TIME IS UP TWIN')
            break

        print(f'Question {i+1} / {total_q}')
        print(questions[i])
        for opt in answers[i]:
            print(opt)

        guess = input('Enter (A, B, C, D): ').strip().upper()
        if guess == correct_answers[i]:
            print(' Correct!')
            score += 1
        else:
            print(f' Incorrect! It was {correct_answers[i]}')

    final_score = int(score / total_q * 100)
    grade = 'F'
    if final_score >= 90: grade = 'A'
    elif final_score >= 80: grade = 'B'
    elif final_score >= 70: grade = 'C'
    elif final_score >= 60: grade = 'D'

    print(f' RESULTS: {final_score}% | GRADE: {grade} ')
    print(f' Score: {score}/{total_q} ')

def weather_condition():
    try:
        temp = int(input('Celsius for today? '))
        if temp >= 35: print('Stay home and hydrate.')
        elif temp >= 18: print('Go outside for a walk.')
        else: print('Go to the gym for today.')
    except ValueError:
        print('Invalid input.')

def main():
    balance = 100
    while balance > 0:
        difficulty, balance = play_slots(balance)
        math_warmup(difficulty)
        main_quiz()
        weather_condition()

        play_again = input('Do you want to spin again? (Y/N): ').upper()

        if play_again != 'Y':
            break

if __name__ == '__main__':
    main()
