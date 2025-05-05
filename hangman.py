from words_list import words
import random

def get_words():
    word = random.choice(words).upper()
    return word


def hangman(chances):
    dispaly_stages =["""
                        --------
                        |      |
                        |      O
                        |     \|/
                        |      |
                        |     / \\
                    """, 
                    """
                        --------
                        |      |
                        |      O
                        |     \|/
                        |      |
                        |     / 
                    
                    """,
                    """
                        --------
                        |      |
                        |      O
                        |     \|/
                        |      |
                        |     
                    
                    """,
                    """
                        --------
                        |      |
                        |      O
                        |     \|
                        |      |
                        |     
                    
                    """,
                    """
                        --------
                        |      |
                        |      O
                        |      |
                        |      |
                        |     
                    
                    """,
                    """
                        --------
                        |      |
                        |      O
                        |      
                        |      
                        |     
                    
                    """,
                    """
                        --------
                        |      |
                        |      
                        |      
                        |      
                        |     
                    
                    """
                    ]
    return dispaly_stages[chances]
