from logic import *

# question 1/1
# in English : Carrots color is orange
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledgeForQuestion1 = And(Implication(carrots, orange))
print(knowledgeForQuestion1.formula())  # print the output formula of knowledge base

#---------------------------------------------------


# question 1/2
# in English : " if person likes carrots , person is vegetarian  "
person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
personLikesCarrots = Symbol("like(x, carrots)")
knowledgeForQuestion2 = Implication( personLikesCarrots,vegetarian)

print(knowledgeForQuestion2.formula())  # print the output formula of knowledge base
#---------------------------------------------------

# question 1/3
# in English : "if he studies hard ,student pass "
passExam = Symbol("pass(x)")
studyHard = Symbol("studyHard(x)")
knowledgeForQuestion3 = Implication(studyHard, passExam)
print(knowledgeForQuestion3.formula())  # print the output formula of knowledge base
#---------------------------------------------------

# question 1/4
# in English : " who will pass? "
Pass = Symbol("? pass(who)")
knowledgeForQuestion4 = And(Pass)
print(knowledgeForQuestion4.formula())  # print the output formula of knowledge base
#---------------------------------------------------

# question 1/5
# in English : " which course teacher teach ? "
teaches = Symbol("? teaches(teacher,course)")
knowledgeForQuestion5 = And(teaches)
print(knowledgeForQuestion5.formula())   # print the output formula of knowledge base

# question 1/6
# in English : " if x & y are enemies, x hate y and x fight y "
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledgeForQuestion6 = And(Implication(enemies, And(hates, fight)))
print(knowledgeForQuestion6.formula()) # print the output formula of knowledge base