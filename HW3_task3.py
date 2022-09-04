omnivores = [{"name": "Jessie Church",
              "omnivore": True,
              "vegetarian": True},
             {"name": "Zaid Maguire",
              "omnivore": True,
              "vegetarian": True},
             {"name": "Catrina Wilde",
              "omnivore": True,
              "vegetarian": True},
             {"name": "Fay Wilkerson",
              "omnivore": True,
              "vegetarian": True}]
vegetarians = [{"name": "Benjamin Herring",
                "omnivore": False,
                "vegetarian": True},
               {"name": "Herman Sawyer",
                "omnivore": False,
                "vegetarian": True},
               {"name": "Simona Neale",
                "omnivore": False,
                "vegetarian": True},
               {"name": "Ricardo Mercado",
                "omnivore": False,
                "vegetarian": True}]
list_of_guests = [omnivores + vegetarians]
can_eat_vegetables_and_herbs = [list_of_guests for list_of_guests in list_of_guests
                                if ["vegetarian"] is True in list_of_guests]
print("List of guests who can eat vegetables and herbs:", can_eat_vegetables_and_herbs)
