#!/usr/bin/python3

collection_path = "/home/criuser/.local/share/Anki2/Utilisateur 1/collection.anki2"
synced_deck_path = "Analyse_4.txt"

from anki.collection import Collection,ImportCsvRequest

def main():
   col = Collection(collection_path)

   metadata = col.get_csv_metadata(path=synced_deck_path,delimiter=None)
   request = ImportCsvRequest(path=synced_deck_path, metadata=metadata)
   response = col.import_csv(request)
   print(response.log.found_notes, list(response.log.updated), list(response.log.new))
   col.export_card_csv(out_path="test.txt",with_html=True)
   print(col.sched.deck_due_tree())

   col.close()

if __name__=="__main__":
   main()
