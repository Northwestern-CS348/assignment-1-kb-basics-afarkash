import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        if(factq(fact.name)) and (fact not in self.facts):
            self.facts.append(fact)
        """Assert a fact or rule into the KB
        
        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
            
        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        print("Asking {!r}".format(fact))        
        list_b = ListOfBindings()
        for f in self.facts:
            result = match(f.statement, fact.statement)
            if(result != False):
                list_b.add_bindings(result, fact)
        if(list_b.__len__() > 0):
            return list_b
        else:
            print("Returning False")
            return False
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
