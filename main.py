alphabet_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                'F': 8, 'G': 3, 'H': 5,
                'I': 1,
                'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5,
                'O': 7, 'P': 8,
                'Q': 1, 'R': 2, 'S': 3, 'T': 4,
                'U': 6, 'V': 6, 'W': 6,
                'X': 5, 'Y': 1, 'Z': 7}

number_map = {
    1: "Number 1 - The Sun, golden, ruby. The brightest star in the sky, without which we wouldn’t be here. As such, symbolises leadership, and the one that everybody looks up to. This number stands for the forefront of creative capabilities, enduring strength, focus and positivity. Nothing holds Number 1 in their quest to rise to the top.",
    2: "Number 2 - The Moon, white, pearl. Like the sun, stands out from the crowd, but in mastery of the creative planes. As such creativity and artistry are key strengths, but always carried out with restraint. Kindness and tact are positive features of this number. However, number 2 people only thrive in positive environments and are too easily scattered.",
    3: "Number 3 - Jupiter, yellow, sapphire. A large and dominant planet, as reflected in the number 3 personality type. An authority figure and delegator, is disciplined and expects the same of others. Whilst a natural born leader, this doesn’t make number 3 a friend to everybody.",
    4: "Number 4 - Uranus, blue, ruby. Definition of a true individual, if not a maverick. Thinking outside of the box and contrary to popular belief and expectation. Not a rule follower, not necessarily out of disrespect, but that’s just who you are. However there is enough self awareness there to know what other people think about you.",
    5: "Number 5 - Mercury, green, emerald. Flows and glides effortlessly just like liquid mercury. Excellent with other people, especially other number 5’s! Very strong willed, but just as much open to acting on an acute sense of instinct. Dreams up ideas and has the will to make them happen. But far too easy to wind up the wrong way.",
    6: "Number 6 - Venus, yellow, diamond. Attraction is the key concept to number 6. Just as people are drawn fondly to them, number 6’s attach themselves to their dreams and ambitions with long-lasting faithfulness. Appreciate the finer things in life and highly cultured. Stands for the qualities of love and harmony over all others.",
    7: "Number 7 - Neptune, white, pearl. A healthy independence permeates the number 7. The freedom to move about and travel is craved, and there is a thirst for knowledge about the world. They do not naturally seek out wealth, but still do well for themselves by their originality and application to the task at hand, not least their talent for self expression. Can be a bit far fetched at times, for better or for worse.",
    8: "Number 8 - Saturn, green, sapphire. Intense, strong and an important outlier. Has a crucial arm in overturning systems and making history. Proponent of robust philosophy and conduct. However is seldom on the same page as others, and can get isolated, if not reviled.",
    9: "Number 9 - Mars, red, coral. Gains strength through conflict, learns from battles lost, but in the end always strives towards victory. Likes being in charge, those beneath a number 9 find them temperamental. Has a lot of potential for success but needs guidance not to fall victim to their own impulsiveness and reckless behaviour.",
    10: "Number 10 - The Wheel of Fortune. This number symbolises vision, and seeing that vision through to the end. Being the wheel, it also refers to the cycle of events, life with its ups and downs, but with the support to make it through.",
    11: "Number 11 - Justice. However this is justice with all its connotations, and highlights to us risk, deceit and dangers that are all around, and how we choose to rise above these.",
    12: "Number 12 - Sacrifice. Just as it describes, being the fall guy so that others may succeed, due to your own unresolved weaknesses and worries.",
    13: "Number 13 - Transition. This corresponds with the infamous tarot card of “Death”, which serves as a warning, although not to be taken literally! The message behind this number is more one of forced change, and advising against abuse of power, and you would do well to take heed of it.",
    14: "Number 14 - Temperance. This signifies times and situations where moderation is required, where one element or force needs balance from another, where finances need to be stablised, or where a middle ground needs to be reached to appease various parties.",
    15: "Number 15 - The Occult. A reminder firstly that the physical plane is not the be all and end all. Secondly, that good and bad are inseparable, and that there are those who will play dirty tricks for bright reward.",
    16: "Number 16 - The Tower. Imagine a tall strong tower being struck down by lightning, and this tells you what you need to know about this number, a sudden and unexpected fate to what was on the surface a stable situation. Be on guard, don’t get complacent.",
    17: "Number 17 - The Star. This symbolises hope and the journey to rise above life’s issues, and even to understand one’s true purpose…although it doesn’t mean that you are quite there yet!",
    18: "Number 18 - Illusion. We are examining here the material world overrunning the higher planes. Wars and conflicts are a good example of how we spend our time so fruitlessly battling for purely materialistic reasons.",
    19: "Number 19 - Enlightenment. Usually indicates assured success, understanding, warmth, courage and positive energies.",
    20: "Number 20 - Awakening. This means it’s time to take action! But think first about why and what your higher self requires. Probably a call to give more structure to your spiritual duties, rather than to pluck up the courage to ask for a job promotion.",
    21: "Number 21 - The World. The number of fulfillment. The feeling of having reached a significant goal, or just that feeling of inner calm.",
    22: "Number 22 - The Fool. The person who lives from day to day in blissful ignorance of the problems that will catch up with them.",
    23: "Number 23 - Strength. Not necessarily your own strength, but that your back is covered by the power and influence of others in higher places.",
    24: "Number 24 - Not too dissimilar to 23, this signifies the importance of others coming to your aid in achieving your aspirations, in personal life too.",
    25: "Number 25 - Success, but only through hard graft, rather than “right time right place”.",
    26: "Number 26 - Troubles, and to look closely at who you are dealing with, as those around you may be to blame for your misfortunes more than any error of your own.",
    27: "Number 27 - Firm execution of a well thought out plan. This is about the importance of strategy and intellect, aside from the actual doing where things will fall into place.",
    28: "Number 28 - For the person who has it all, a reminder that nothing lasts forever and you’re not exempt. Have a backup plan and don’t put all your eggs into one basket.",
    29: "Number 29 - A sneaking suspicion that somebody is having you on. Business and personal partners might show their other side, and it will be your loss.",
    30: "Number 30 - Is your glass half full or half empty? The results of your general mindset are going to take a boost for better or for worse.",
    31: "Number 31 - Current predicaments could swing either way, but for sure you may become lonelier whatever happens.",
    32: "Number 32 - It’s time to stick to your guns and take control of the situation, else be held back by the conflicting opinions and incompetence of others.",
    33: "Number 33 - Not too dissimilar to 23, this signifies the importance of others coming to your aid in achieving your aspirations, in personal life too.",
    34: "Number 34 - Success, but only through hard graft, rather than “right time right place”.",
    35: "Number 35 - Troubles, and to look closely at who you are dealing with, as those around you may be to blame for your misfortunes more than any error of your own.",
    36: "Number 36 - Firm execution of a well thought out plan. This is about the importance of strategy and intellect, aside from the actual doing where things will fall into place.",
    37: "Number 37 - Positive number when it comes for forming partnerships, particularly in one’s personal life.",
    38: "Number 38 - A sneaking suspicion that somebody is having you on. Business and personal partners might show their other side, and it will be your loss.",
    39: "Number 39 - Is your glass half full or half empty? The results of your general mindset are going to take a boost for better or for worse.",
    40: "Number 40 - Current predicaments could swing either way, but for sure you may become lonelier whatever happens.",
    41: "Number 41 - It’s time to stick to your guns and take control of the situation, else be held back by the conflicting opinions and incompetence of others.",
    42: "Number 42 - Not too dissimilar to 23, this signifies the importance of others coming to your aid in achieving your aspirations, in personal life too.",
    43: "Number 43 - Signifies a considerable and somewhat negative overhaul in circumstance.",
    44: "Number 44 - Troubles, and to look closely at who you are dealing with, as those around you may be to blame for your misfortunes more than any error of your own.",
    45: "Number 45 - Firm execution of a well thought out plan. This is about the importance of strategy and intellect, aside from the actual doing where things will fall into place.",
    46: "Number 46 - For the person who has it all, a reminder that nothing lasts forever and you’re not exempt. Have a backup plan and don’t put all your eggs into one basket.",
    47: "Number 47 - A sneaking suspicion that somebody is having you on. Business and personal partners might show their other side, and it will be your loss.",
    48: "Number 48 - Is your glass half full or half empty? The results of your general mindset are going to take a boost for better or for worse.",
    49: "Number 49 - Current predicaments could swing either way, but for sure you may become lonelier whatever happens.",
    50: "Number 50 - It’s time to stick to your guns and take control of the situation, else be held back by the conflicting opinions and incompetence of others.",
    51: "Number 51 - This number indicates strong fortune, or more likely greater ease, in defeating conflict and challenges.",
    52: "Number 52 - Signifies a considerable and somewhat negative overhaul in circumstance.",
}


def reduce_number_to_single_digit(num: int) -> int:
    return num if num <= 9 else reduce_number_to_single_digit(num - 9)


def map_name_to_number(names: list) -> dict:
    global alphabet_map
    name_num_map = {}

    for name in names:
        name_num_map[name] = sum([alphabet_map[c] for c in name.upper()])

    return name_num_map


if __name__ == '__main__':
    while True:
        try:
            user_input = input('\nEnter name (space separated): ')
            user_input_list = user_input.split()
            name_number_map = map_name_to_number(user_input_list)

            for name, compound_number in name_number_map.items():
                name_number = reduce_number_to_single_digit(compound_number)

                print(f'{name} = {compound_number} -> {name_number}')
                print(f'  {number_map[name_number]}')
                print()

            full_name_number = sum([reduce_number_to_single_digit(i) for i in name_number_map.values()])
            single_digit = reduce_number_to_single_digit(full_name_number)

            print(' '.join(name_number_map.keys()) + ' = ', end='')
            print(full_name_number, end='')
            print(' -> ', end='')
            print(single_digit)
            print(f'  {number_map[single_digit]}')
            print(f'  {number_map[full_name_number]}')
        except KeyboardInterrupt:
            exit()
