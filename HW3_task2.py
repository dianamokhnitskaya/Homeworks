casino_blacklist = {"Denzel Mayer", "Umair Wallis", "Rees Begum",
                    "Kane Whitehouse", "Jorge Wardle", "Mateo Mccarty",
                    "Menachem Mckay", "Duke Joyce", "Mollie Campbell",
                    "Nelly Steele", "Troy Cotton", "Harper Brook"}
poker_blacklist = {"Awais Lowry", "Kane Whitehouse", "Jorge Wardle",
                   "Mateo Mccarty", "Menachem Mckay", "Duke Joyce",
                   "Mollie Campbell", "Tomasz Bates", "Frankie Mellor",
                   "Tanvir Mair", "Francisco Turner", "Osman Crouch"}
alcohol_blacklist = {"Luna Morrow", "Kane Whitehouse", "Jorge Wardle",
                     "Mateo Mccarty", "Menachem Mckay", "Duke Joyce",
                     "Mollie Campbell", "Antony Smyth", "Trinity Ware",
                     "Bianca Marks", "Dimitri Mayer", "Sammy Boyd"}
# general_black_list = []
# general_black_list.extend(casino_blacklist)
# general_black_list.extend(poker_blacklist)
# general_black_list.extend(alcohol_blacklist)
# duplicate_blacklist = [item for item, count in collections.Counter(general_black_list).items() if count > 1]
# print("People in all black lists:" + str(duplicate_blacklist))
general_black_list = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print("People in all black lists:", general_black_list)
