from wikidataintegrator import wdi_core
import pprint

item1 = wdi_core.WDItemEngine(wd_item_id="Q35869")
item1.get_wd_json_representation()
statements = []
statements.append(wdi_core.WDItemID("Q42", prop_nr="P31"))
item2 = wdi_core.WDItemEngine(wd_item_id="Q35869", data = statements)
item2.get_wd_json_representation()

print("Item 1:")
pprint.pprint(item1)

print("Item 2:")
pprint.pprint(item2)
