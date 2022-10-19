from enum import Enum
import random

class ModelType(Enum):
    
    LIGTHWEIGHT = "Ligthweight"
    MIDDLEWEIGHT = "Middleweight"
    CRUISERWEIGHT = "Cruiserweight"
    HEAVYWEIGHT = "Heavyweight"

    RANDOM = random.choice([LIGTHWEIGHT, MIDDLEWEIGHT, CRUISERWEIGHT, HEAVYWEIGHT])