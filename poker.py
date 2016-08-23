import random
suites = ['C', 'D', 'H', 'S'] #clubs, diamonds, hearts, spades
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
"Nine", "Ten", "Jack", "Queen", "King", "Ace"]
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
plays = ["High", "Pair", "Two Pair", "Set", "Straight", "Flush", "Full
House", "Quad", "Straight Flush", "Royal Flush"]
table_cards = []

class Card:
        def __init__(self, rank, suite):
                self.rank = rank
                self.suite = suite
        def getSuite(self):
                return self.suite
        def getRank(self): #full word
                return self.rank
        def getRank1(self):   #symbol
                return rank[ranks.index(self.rank)]

class Player:
        def __init__(self, two_cards, current_bet):
                self.two_cards = two_cards
                self.current_bet = current_bet #this feature is not implemented
        def getCards(self):
                return self.two_cards
        def getHand(self):
                if(len(table_cards) < 3):
                        return self.cards
                else:
                        return self.__calculateHand()
        def __calculateHand(self):
                first_cards = self.two_cards
                if(len(table_cards) < 3):
                        if ranks.index(first_cards[1].getRank()) >
ranks.index(first_cards[2].getRank()): #check one high card pre-flop
                                return (first_cards[1], "High")
                        elif ranks.index(first_cards[1].getRank()) ==
ranks.index(first_cards[2].getRank()): #check for pair pre-flop
                                return (first_cards[1], "Pair")
                        else:
                                return (first_cards[1], "High")
                all_cards = first_cards + table_cards

                all_indexes = []
                for i, na in enumerate(all_cards):                      #order least to greatest based on rank
                        all_indexes.append(ranks.index(all_cards[i].getRank()))
                all_indexes.sort()
                for i, val in enumerate(all_indexes):
                        for k, val2 in enumerate(all_cards):
                                if all_indexes[i] is ranks.index(all_cards[k].getRank()):
                                        c = val2
                                        del all_cards[k]
                                        all_cards.insert(i, c)

                all_suites = []
                for i, val3 in enumerate(all_cards): #create a list of just suites
(ordered least to gr)
                        all_suites.append(val3.getSuite())

                if all_suites.count(max(set(all_suites), key=all_suites.count)) >=
5: #flush of some kind
                        count = 1 #start 1 with a card already
                        i = 0
                        while i < len(all_cards)-1:
                                if ((ranks.index(all_cards[i].getRank()) + 1 !=
ranks.index(all_cards[i+1].getRank()) or #consecutive rank
                                        #(i is not 0 and
ranks.index(all_cards[len(all_cards)-1].getRank()) is not 12 and
ranks.index(all_cards[0].getRank()) is not 0 or
                                                #suites.index(all_cards[len(all_cards)-1].getSuite()) is not
suites.index(all_cards[0].getSuite()))) or #ace as 1
                                                        suites.index(all_cards[i].getSuite()) is not
suites.index(all_cards[i+1].getSuite())) and #same suite
                                                                len(all_cards)-i <= 5): #enough cards left to still have a
straight flush
                                        if (not (i is len(all_cards)-1 and
ranks.index(all_cards[len(all_cards)-1].getRank()) is 12 and
ranks.index(all_cards[0].getRank()) is 0) or
                                                (suites.index(all_cards[len(all_cards)-1].getSuite()) is not
suites.index(all_cards[0].getSuite()))): #ace as 1
                                                count += 1
                                                high_card_84 = all_cards[i] #high card of the straight flush
                                                break
                                else:
                                        count += 1
                                        high_card_84 = all_cards[i+1]
                                i+=1
                        if count >= 5: #straight flush
                                if Rank.index(high_card_84.getRank()) is len(Rank)-1:
                                        print("Royal Flush")
                                return (high_card_84, "Straight Flush")

                if all_indexes.count(max(set(all_indexes), key=all_indexes.count))
>= 4: #quads
                        return (all_cards[all_indexes.index(max(set(all_indexes),
key=all_indexes.count))], "Quad")

                trips = list(set([x for x in all_indexes if all_indexes.count(x) ==
3])) #triplets set
                dupes = list(set([x for x in all_indexes if all_indexes.count(x) ==
2])) #pairs
                if len(trips) > 1: #full house
                        return (all_cards[all_indexes.index(max(trips))],
all_cards[all_indexes.index(min(trips))], "Full House", "and")
                elif len(dupes) > 0 and len(trips) > 0:
                        return (all_cards[all_indexes.index(trips[0])],
all_cards[all_indexes.index(max(dupes))], "Full House", "of")

                flush_length = all_suites.count(max(set(all_suites), key=all_suites.count))
                flush_type = list(set([x for x in all_suites if all_suites.count(x) >= 5]))
                if flush_length >= 5:                                       #normal flush
                        i =0
                        while i < len(all_suites):
                                if all_suites[i] is flush_type[0]:
                                        flush_high_index = i
                                i+=1
                        return (all_cards[flush_high_index], "Flush")

                #straight
                count = 1
                i = 0
                while i < len(all_cards)-1:
                        if ((ranks.index(all_cards[i].getRank()) + 1 !=
ranks.index(all_cards[i+1].getRank()) and
                                len(all_cards)-i <= 5)):
                                if not (i is len(all_cards)-1 and
ranks.index(all_cards[len(all_cards)-1].getRank()) is 12 and
ranks.index(all_cards[0].getRank()) is 0): #ace as 1
                                        count += 1
                                        high_card_55 = all_cards[i] #high card of the straight
                                break
                        else:
                                count += 1
                                high_card_55 = all_cards[i+1]
                        i+=1
                if count >= 5:
                        return (high_card_55, "Straight")

                if len(trips) is 1: #set
                        return (all_cards[all_indexes.index(trips[0])], "Set")

                if len(dupes) > 1: #two pair
                        return (all_cards[all_indexes.index(dupes[len(dupes)-1])], #two
pair with one higher and one lower
                                                all_cards[all_indexes.index(dupes[len(dupes)-2])], "Two Pair")

                elif len(dupes) is 1:
                        return (all_cards[all_indexes.index(dupes[0])], "Pair"); #one pair

                else: #high card left to right, right being lowest
                        return all_cards.reverse()
class Print:
        #def __init__(self):
        def printCards(self, cards):
                lines = ["", "", "", "", "", "", "", "", ""]

                i = 0
                buffer = 0
                while i < len(cards):
                        lines[0]+="┌─────────┐"
                        lines[1]+="│         │"
                        lines[2]+="│         │"
                        lines[3]+="│         │"
                        lines[4]+="│         │"
                        lines[5]+="│         │"
                        lines[6]+="│         │"
                        lines[7]+="│         │"
                        lines[8]+="└─────────┘"

                        line1 = list(lines[1])
                        line4 = list(lines[4])
                        line7 = list(lines[7])
                        if cards[i].getRank1() is not "10":
                                line1[2+buffer] = cards[i].getRank1()
                                lines[1] = ''.join(line1)
                                line4[5+buffer] = cards[i].getSuite()
                                lines[4] = ''.join(line4)
                                line7[7+buffer] = cards[i].getRank1()
                                lines[7] = ''.join(line7)
                        else:
                                line1[2+buffer] = '1'
                                line1[3+buffer] = '0'
                                lines[1] = ''.join(line1)
                                line4[5+buffer] = cards[i].getSuite()
                                lines[4] = ''.join(line4)
                                line7[7+buffer] = '1'
                                line7[8+buffer] = '0'
                                lines[7] = ''.join(line7)
                        buffer+=12
                        lines = [(x+" ") for x in lines]
                        i+=1

                i = 0
                while i < len(lines):
                        print(lines[i])
                        i+=1

if __name__ == "__main__":
        i =1
        while i > 0:
                card1 = Card(random.choice(ranks), random.choice(suites))
                card2 = Card(random.choice(ranks), random.choice(suites))
                nick = Player([card1, card2], None)
                table_cards= [Card(random.choice(ranks), random.choice(suites)),
Card(random.choice(ranks), random.choice(suites)),
                        Card(random.choice(ranks), random.choice(suites)),
Card(random.choice(ranks), random.choice(suites)),
                                Card(random.choice(ranks), random.choice(suites))]
                printer = Print()
                try:
                        if a.getRanks() is "Ace" and b is "Straight Flush":
                                print("Royal Flush")
                                printer.printCards(table_cards)
                                printer.printCards(nick.getCards())
                                break
                except:
                        pass
                i+=1