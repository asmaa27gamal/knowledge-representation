
from logic import *


x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates1 = Symbol(f"hates({x}, {y})")
hates2 = Symbol(f"hates({y}, {x})")
knowledgeForQuestion1 = And(Implication( And(hates1, hates2),enemies))
print(knowledgeForQuestion1.formula())

#------------------------------------------------------------------------


p = Symbol("p(x)")
q = Symbol("q(x)")
r = Symbol("r(x)")
knowledgeForQuestion2 = And(Implication(p , Implication(q, r)))
print(knowledgeForQuestion2.formula())