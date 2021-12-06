import numpy as np
#Finding the probability that a student knows the material given that the student answers it correctly (P(knows the material | answers correctly))
knows_the_material = 0.60
answers_correctly_knows_material = 1 - 0.15
#Using weighted average to find probability of student answering correctly since there are two scenarios to this (student knowing the answer or ot, but answering correctly)
answers_correctly = (answers_correctly_knows_material * knows_the_material) + (0.20 * 0.40)
knows_material_answers_correctly = (answers_correctly_knows_material * knows_the_material) / (answers_correctly)
print(knows_material_answers_correctly)
#The probability of a student knowing the material when he/she has answered correctly is 86%