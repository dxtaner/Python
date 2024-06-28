def get_jury_scores():
    jury_scores = []
    for counter in range(1, 6):
        score = int(input("Jury #{} please enter your score: ".format(counter)))
        jury_scores.append(score)
    return jury_scores


def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average


def make_comment(average):
    if 3.5 <= average <= 5:
        print("You didn't pass, you need to work a bit more.")
    elif 1 <= average < 3.5:
        print("The jury didn't like you very much.")
    elif 5 < average <= 7:
        print("Congratulations, you passed!")
    elif 7 < average <= 9:
        print("You were amazing, the jury was impressed. Your average: {:.2f}".format(
            average))


jury_scores = get_jury_scores()
average = calculate_average(jury_scores)
make_comment(average)
