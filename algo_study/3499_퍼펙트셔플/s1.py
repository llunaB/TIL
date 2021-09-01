import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    # 카드 수가 홀수라면 => 맨 뒤에 임의의 카드 추가
    if len(cards) % 2:
        cards.append('temp_card')
        # 덱을 두 개로 나눠 이중 리스트를 만든다
        mid = N // 2 + 1  # INDEX
        new_decks = [cards[:mid], cards[mid:]]
        # 빈 덱을 만든다
        shuffled_deck = []
        # 각 리스트(덱)에서 가장 앞의 카드를 빼서 빈 덱에 넣는다.
        for i in range(mid):
            shuffled_deck.append(new_decks[0].pop(0))
            shuffled_deck.append(new_decks[1].pop(0))
        shuffled_deck.pop()

    # 카드 수가 짝수라면
    else:
        # 덱을 두 개로 나눠 이중 리스트를 만든다
        mid = N // 2 # INDEX
        new_decks = [cards[:mid], cards[mid:]]
        # 빈 덱을 만든다
        shuffled_deck = []
        # 각 리스트(덱)에서 가장 앞의 카드를 빼서 빈 덱에 넣는다.
        for i in range(mid):
            shuffled_deck.append(new_decks[0].pop(0))
            shuffled_deck.append(new_decks[1].pop(0))

    print("#{} {}".format(tc, ' '.join(shuffled_deck)))