# -*- coding: utf-8 -*-
"""

This script is created for the purpose of identifying the name of the supplier company of the issued invoice.

To be excecuted from a terminal window.
The user will be prompted for the path of suppliernames.txt and invoice.txt 

author: Alex Bi
created: 08/10/2019

"""

import re
from nltk.tokenize import RegexpTokenizer
#import nltk
#nltk.download('stopwords')
#nltk.download('punkt')


class MatchNames:
    
    def __init__(self, namesfile_path, invoicefile_path):
        
        self.namesfile_path= namesfile_path
        self.invoicefile_path=invoicefile_path
    
    def invoice_to_tokens(self):
        
        invoicefile = open(self.invoicefile_path)
        patterns_regex=r"[{}:,.'']|\w+\_\w+"
        invoicefile_re=re.sub(patterns_regex, ' ', invoicefile.read())

        patterns_token=r"\w+|\d+"
        tokenizer=RegexpTokenizer(patterns_token)
        
        invoice_tokens=list(set(tokenizer.tokenize(invoicefile_re)))
        invoicefile.close()
        
        #print(invoice_tokens)
        return(invoice_tokens)
        
    def matching_invoice_names(self, invoice_tokens):
    
        suppliernames_file=open(self.namesfile_path)

        #for lines in supplier_file:
        patterns=r"\w+|\d+"
        tokenizer = RegexpTokenizer(patterns)

        name_tok_list=[tokenizer.tokenize(lines) for lines in suppliernames_file]
        name_tok_list= name_tok_list[1:]

        
        records=[]
        for toks in name_tok_list:
            l=list(set(toks[1:]).intersection(invoice_tokens))
            
            if len(l)==len(toks[1:]):
                        
                records.append(toks)
                
        suppliernames_file.close()
        return (records)
    
    def show_results(self, matching_records):
        
        count= len(matching_records)   
        if count==0:
            print("No matching supplier found.")
        else:
            frequency_str= " {} matching records(s) found.".format(count)
        
            print(frequency_str)
        
            for counter, infos in enumerate(matching_records):
            
                c_str= "Company {} : ".format(counter+1)
                print(c_str, infos)

def main():
    # user input file paths
    namesfile_path=input("Enter supplier names file path: ")
    
    invoicefile_path=input("Enter invoice file path: ")
    
    # execution 
    matching=MatchNames(namesfile_path,invoicefile_path)
    invoice_tokens=matching.invoice_to_tokens()
    matching_records=matching.matching_invoice_names(invoice_tokens)
    matching.show_results(matching_records)
    

if __name__ == "__main__":
    main()

    
    
    
                
        
        