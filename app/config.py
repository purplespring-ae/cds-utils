# '''
# GLOBAL VARS
# '''

# ''' DEBUG MESSAGE STRINGS
SUGGEST_MANUAL = "Consider editing the medication in sheet manually after it has been generated."

# ''' INPUT VALIDATION
# These have not been set as CONST to allow easier implementation of user customisation later
valid_freqs = ["i_n_per_day", "as_needed", "regime"]
freqs = {"i_n_per_day": "Take [i], [n] times per day.",
         "as_needed": "Take [i] as needed up to [n] times per day.",
         "regime": "Take according to regime."}
valid_strength_units = ["mg", "ml", None]
valid_timings = ["morning", "night"]

freq_dicts = [
    {"statement": "Take [i], [n] times per day.",
     "has_i": True,
     "has_n": True},
    {"statement": "Take [i] as needed up to [n] times per day.",
     "has_i": True,
     "has_n": True},
    {"statement": "Take according to regime.",
     "has_i": False,
     "has_n": False}

]

list_freqs = [
    "Take [i], [n] times per day.",
    "Take [i] as needed up to [n] times per day.",
    "Take according to regime."
]
