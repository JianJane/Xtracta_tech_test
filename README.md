# Xtracta_tech_test
Technical test for entry level AI engineer at Xtracta Auckland

Read Me

Purpose:
matchsupplier.py  is created for matching matching invoice “invoice.txt” to its issuing company, which might or might not exist in the supplier name list “supplier names.txt”.

Components:

The script contains a class named “MatchNames”, and three method functions: 
	•	invoice_to_tokens; 
	•	matching_invoice_names; 
	•	show_results

The class attributes are the paths to the “invoice.txt” and “supplier names.txt”


Output:
The script outputs the record of the matched company record. Ideally, there is only one matching record or None if the company is not yet in the supplier name file.

Execution:
	•	Save the script, invoice.txt, and supplier names.txt in the designated directory.
	•	Open a terminal window, set the directory as working directory.
	•	execute “matchsupplier.py” under python3
	•	enter file paths when prompted 
