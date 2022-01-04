from logic import * 

# question 2/1
#  read(maria, logic programming book) ==> by(peter lucas)
maria = Symbol("maria")
peter_lucas = Symbol("peter lucas")
read = Symbol(f" read ({maria}, logic programming book)")
by = Symbol(f"by ({peter_lucas})")
knowledgeForQuestion1 = And(Implication(read, by))
print(knowledgeForQuestion1.formula())

#-----------------------------------------------------------

# question 2/2
# is_girl(x) ==> like(x, shopping)
is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
like = Symbol(f"like(x, {shopping} )")
knowledgeForQuestion2 = And(Implication(is_girl, like))
print(knowledgeForQuestion2.formula())

#-----------------------------------------------------------
# question 2/3
# ? likes( x , shopping)
who = Symbol("?")
knowledgeForQuestion3  = And(who ,like)
print(knowledgeForQuestion3.formula())
#-----------------------------------------------------------
# question 2/4
# city( x ,big , crowdy) ==> hates(kirke, x)
city = Symbol("city(x, big, crowdy)")
hates = Symbol("kirke, x")
knowledgeForQuestion4 = And(Implication(city, hates))
print(knowledgeForQuestion4.formula())