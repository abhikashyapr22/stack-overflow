nursery_rhyme = [
'This is the house that Jack built.',
'This is the malt that lay in the house that Jack built.',
'This is the rat that ate the malt that lay in the house that Jack built.',
'This is the cat that killed the rat that ate the malt that lay in the house that Jack built.'
]

def recite(start_verse, end_verse):
    
    for line in (start_verse-1, end_verse):
        print(nursery_rhyme[line])
        
        
 recite(1,2)
