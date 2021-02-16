# thorlabsBC
Automatic data compilation for ThorLabs orders to fill the LKB bon de command.

The script reads a Thorlabs shopping cart file (.xls or .xlsx). It grabs the description and pricing information form the file, calculates the discount and translates the description into french via the google translate API. Finally, everything is written to template bon de command in .xlsx format.  

The "Code Nomenclature" NACRES is partially implemented for the most common articles. The full NACRES table is included in the repo if needed. Take a look at "nacres_from_thorlabs.py" if ou want to implement a simple rule for an article. Be sure the rule is right, and other articles are not included in the rule by chance (e.g. fr word matching, just try to type the word in the search box of the thorlabs site...)

ALWAYS CHECK ON THE QUOTE IF THE INFOS ARE CORRECT !!
Shipment cost must included and added by hand (can be easily implemented...if someone have two minutes)

