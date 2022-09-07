eleks_employees = ["Erick Green", "Monica Blanc",
                   "Hanna Brown", "Peter Black",
                   "Rebecca Stoun", "John Daw"]
toshiba_employees = ["Tomas Loyd", "Veronica Bill",
                     "Richard Calt", "Erick Green",
                     "Monica Blanc", "Robert Dauson",
                     "Sam Brown", "Amanda Stainback"]
toshiba_employees.extend(eleks_employees)

print("List of Toshiba employees after Eleks takeover:" + format(str(toshiba_employees)))
