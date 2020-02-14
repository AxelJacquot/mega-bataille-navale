from src.client.py import replaceMultiple

def test_replaceMultiple():
   assert replaceMultiple("hello",['l'],'c')=="hecco" 

