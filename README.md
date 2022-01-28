# thorlabsBC
Automatic generation of an LKB bon de command (BC) for ThorLabs orders.

## general:
The script reads a Thorlabs shopping cart file (.xls or .xlsx). It grabs the description and pricing information form the file, adds the discount, translates the description into french via a cloud API and checks the "Code Nomenclature" where implemented. Finally, everything is written to the template bon de command in .xlsx format.  

## usage:
- if you you are not from team Gigan edit the 'Equipe' and 'NOM PERMANENT' fields accordingly
- open the thorlabs_exel.py script and go to the INPUT bloc
- enter the target directory where the 'shoppingCart.xls' file can be found and where you want the output BC file to be stored
- check if you got an initial discount subtracted by the webshop (usually 2% for orders above 5k). If so enter it (i.e. discount_init = 0.02), otherwise set it to zero.
- check the dicount which is usually 9% for the LKB (i.e. discount_fin = 0.09)
- enter the shipping costs and run the code
- ALWAYS COMPARE TO THE OFFICIAL QUOTE AND CHECK IF TRANSLATIONS MAKE SENSE!!

## deatils:
- The code implements two APIs for translation, Google translate and DeepL. The default is Google translate (trans_flag = 0) but this sometimes produces unsatisfying results (see known issues below). For the DeepL translation (trans_flag = 0) you need an account. There is a free version supporting 500k char a month which should be well enough even if you order a lot. Since I want this git to be public but don't want my athentification credentials to be in there you need to set up your own account and share the key with your collegues. Store the key in a text file named 'auth_deepl.txt' in the git directory.
- It would be great to have a simple GUI to enter the path of the input file and discount/shipping. If you got time and want to implement this it would be great (we tried with easygui but had some problems). If you do, make sure it works on win/mac/linux!!
- The "Code Nomenclature" NACRES is partially implemented for the most common articles. The full NACRES table is included in the repo for reference. Take a look at "nacres_from_thorlabs.py" if you want to implement a simple rule for an item. Be sure the rule applies in any scenario and no other items could be included accidentially (e.g. when using a rule by word matching, just try to type the word in the search box of the thorlabs site and see if only the articles you had in mind are popping out)

## known issues:
- The implementation of the google translate API has some problems. Sometimes strange translations appear although entering the same text in the google translate web mask gives good results. Use the DeepL option for better translations (see above).
- If the webshop subtracts a discount it rounds to the next cent value. As this operation cannot be deterministically reversed there can be price differences of +/- 1 cent in the item prices from orders where the initial discount is added again.

