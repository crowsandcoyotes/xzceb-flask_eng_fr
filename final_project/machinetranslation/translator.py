"""
Translate English To French And French To English
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English To French
    """
    #write the code here
    french_text = MyMemoryTranslator('en-GB', 'fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French To English
    """
    #write the code here
    english_text = MyMemoryTranslator('fr-FR', 'en-GB').translate(french_text)
    return english_text
