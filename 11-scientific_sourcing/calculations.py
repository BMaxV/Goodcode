from wikidatainteraction import simplewikidata
import matplotlib.pyplot as plt
import subprocess


fig, ax = plt.subplots()

wd_get = simplewikidata.get_property_of_entity

paris_population = wd_get("Q90","P1082")
london_population = wd_get("Q84","P1082")
berlin_population = wd_get("Q64","P1082")
new_york_population = wd_get("Q60","P1082")
buenos_aires_population = wd_get("Q1486","P1082")

# print(paris_population)

mybarlist = [paris_population, london_population, berlin_population, new_york_population, buenos_aires_population]
lables = ["paris","london","berlin","new york","buenos aires"]

ax.bar(lables,mybarlist)
ax.set_title("populations")
ax.set_ylabel("population")

plt.savefig("myfig.svg")

subprocess.run("weasyprint Paper_raw.html Paper_out.pdf".split(" "))
