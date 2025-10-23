import random


def create_card(rank:str,suite:str) -> dict:
    values = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "J":10, "q":11, "k":12, "a":14 }
    return {"rank": rank, "suite": suite, "value": values[rank]}


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    return ""



def create_deck() -> list[dict]:
    suite = ["h", "c", "d", "s"]
    ranks = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "j", 11: "q", 12: "k", 13: "a"}
    for x in suite:
        for i in range(1,14):
           return [{"rank":ranks[i], "suite":x, "value":str(i)}]


def shuffle(deck:list[dict]) -> list[dict]:
  for i in range(1000):
      #while True:
       index1 = random.randrange(1, 13)
       index2 = random.randrange(1, 13)
       if index1 != index2:
         index1, index2 = index2, index1
       else:

      return [{}]



