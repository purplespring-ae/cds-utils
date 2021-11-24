# '''
# EXTERNAL MODULES
# '''

# import docxtpl
# import docx
# import os

# '''
# LOCAL MODULES
# '''
from config import *

# '''
# CLASSES
# '''


class Medication():
    def __init__(self, name, strength_val, strength_unit, dtype, n, i, qty_in, timing=None):
        self.name = self.valid_name(name)
        self.strength_val = self.valid_strength(strength_val)
        # self.strength_unit = self.valid_strength_unit(strength_unit)
        self.strength_unit = strength_unit if strength_unit in valid_strength_units else ValueError(
            f"Strength unit must be in {valid_strength_units}. {SUGGEST_MANUAL}")
        self.dosage = Dosage(n, i, dtype, timing)
        self.qty_in = qty_in if isinstance(qty_in, int) else 0
        self.qty = qty_in
        self.report()

    def valid_name(self, name):
        if isinstance(name, str) and len(name) != 0:
            #print(f"Medication name {name} is accepted and set.")
            return name
        elif isinstance(name, str):
            raise ValueError("Name of length 0 is not accepted")
        else:
            raise ValueError("Medication name must be a string.")

    def valid_strength(self, strength_val):
        if isinstance(strength_val, int) or isinstance(strength_val, float):
            # print(
            #    f"Medication strength value of {strength_val} is accepted and set.")
            return strength_val
        else:
            raise ValueError(
                "Medication strength must be an integer or float (decimal).")

    def report(self, out=False):
        process = "out" if out else "in"
        report = f"{self.qty} units of {self.name} to be checked {process}."
        if not out:
            report += f" Dosage: {self.dosage.instruction}"
        print(report)

    def update_qty(self, new_qty):
        self.qty = new_qty  # if isinstance(new_qty, int) else ValueError(
        # "New quantity must be an integer.")

    def check_out(self, qty):
        self.update_qty(qty)
        self.report(out=True)


class Dosage():
    def __init__(self, i, n, freq, timing=None):
        self.i = i
        self.n = n
        self.freq = freq if freq in valid_freqs else ValueError(
            f"Frequency must be in {valid_freqs}.")
        # self.timing = self.valid_timing(timing)
        self.timing = timing if timing in valid_timings else ValueError(
            f"Timing must be in {valid_timings}. Defaults to None. {SUGGEST_MANUAL}")
        self.instruction = self.build_instruction(self.i, self.n, self.freq)
        #print(f"Dosage accepted and set: {self.instruction}")

    def build_instruction(self, i, n, freq):
        n_str = "times" if n != 1 else "time"
        if freq == "i_n_per_day":
            return f"Take {i}, {n} {n_str} per day."
        elif freq == "as_needed":
            return f"Take {i} as needed, up to {n} {n_str} per day."
        elif freq == "regime":
            return "Take according to regime."
        else:
            raise ValueError


# '''
# INPUT
# '''

med_1 = Medication("Fluoxetine", 200, "mg", "i_n_per_day", 1, 1, 28)
med_2 = Medication("Paracetamol", 500, "mg", "as_needed", 2, 4, 32)

med_1.check_out(3)

# '''
# OUTPUT
# '''
