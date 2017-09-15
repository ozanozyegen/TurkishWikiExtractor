import mwxml
import cleantext

def extractSingleDoc(doc_name):
    for page in dump:
        for revision in page: #For each news
            file.write(cleantext.clean_text(str(revision.text)))

def extractSingleDocWithDocNums(docname):
    cdoc_number = 0  # Counter doc number
    for page in dump:
        for revision in page: # For each news article
            # file.write("\n<doc num="+str(cdoc_number)+">\n") #Elegant version
            file.write("\n<\n") #   Since "<" is eliminated from original text, it can be used as a splitter between articles
            cdoc_number += 1
            file.write(cleantext.clean_text(str(revision.text)))

if __name__ == '__main__':
    doc_name = "wiki.xml"

    file = open("articles_cleaned.txt", "w",    encoding="utf-8")
    dump = mwxml.Dump.from_file(open(doc_name,  "r",    encoding="utf-8"))


    #extractSingleDoc(doc_name)
    extractSingleDocWithDocNums(doc_name)

    file.close()
