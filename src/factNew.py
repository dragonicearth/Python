# import re
# fact = "Daylight: 260 F Nighttime: -280 F"
# fact2 = re.split('; |, |\*|\n|:',fact)
# print(fact2)

# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.count("Mars"))
# print(temperatures.count("Moon"))

# print("""THE MOON AND THE EARTH""".lower())

# print("""()The Moon And The Earth""".upper())

# temperatures = "Mars Average Temperature: -60 C"
# parts = temperatures.split(':')
# print(parts)
# print(parts[-1])

# mars_temperature = "The highest 2 temperature on Mars is about 30 C"
# for item in mars_temperature.split():
#     if item.isnumeric():
#         print(''.join(item))

# text = "Temperatures on the Moon can vary wildly."
# BooSalve = "temperatures" in text.lower()
# if BooSalve == True:print(BooSalve)
# else: print('False')

# moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
# print(' '.join(moon_facts))

# mass_percentage = "1/6"
# print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

# print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

# mass_percentage = "1/6"
# print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

# mass_percentage = "1/6"
# print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

# mass_percentage = "1/6"
# print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

# print(round(100/6, 1))

# print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

# subject = "interesting facts about the moon"
# heading = f"text aleatory {subject.title()}"
# print(heading)

name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))

