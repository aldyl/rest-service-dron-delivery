from enum import Enum
import random

class StateType(Enum):
    
    IDLE = "IDLE"
    LOADING = "LOADING"
    LOADED = "LOADED"
    DELIVERING = "DELIVERING"
    DELIVERED = "DELIVERED"
    RETURNING = "RETURNING"

    RANDOM = random.choice([IDLE, LOADING, LOADED, DELIVERING, DELIVERED, RETURNING])