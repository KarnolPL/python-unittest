amount = 1000
tax_rate = 1.15

assert amount >= 0, 'The amount should not be negativ.'
assert 0 < tax_rate < 1, 'Tax rate should be between 0 and 1.'