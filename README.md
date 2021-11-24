# thorlabsBC
Automatic generation of a filled LKB bon de command (BC) for ThorLabs orders.

## general:
The script reads a Thorlabs shopping cart file (.xls or .xlsx). It grabs the description and pricing information form the file, adds the discount (generally 9%), translates the description into french via the google translate API and checks the "Code Nomenclature" where implemented. Finally, everything is written to the template bon de command in .xlsx format.  

## usage:
- open the thorlabs_exel.py script and go to the INPUT bloc
- enter the target directory where the 'shoppingCart.xls' file can be found and where you want the output BC file to be stored
- check the dicount which is usually 9% for the LKB (i.e. enter 0.09)
- enter the shipping costs and run the code
- ALWAYS CHECK THE GENERATED QUOTE IF THE INFOS ARE CORRECT!!

## deatils:
- It would be great to have a simple GUI to enter the path of the input file and discount/shipping. If you got time and want to implement this it would be great (we tried with easygui but had some problems). If you do, make sure it works on win/mac/linux!!
- The "Code Nomenclature" NACRES is partially implemented for the most common articles. The full NACRES table is included in the repo for reference. Take a look at "nacres_from_thorlabs.py" if you want to implement a simple rule for an item. Be sure the rule applies in any scenario and no other items could be included accidentially (e.g. when using a rule by word matching, just try to type the word in the search box of the thorlabs site and see if only the articles you had in mind are popping out)

