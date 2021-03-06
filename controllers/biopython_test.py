
#Added path by appending to the sys.path
import sys
biopython_lib = request.folder + "modules/"
sys.path.append(biopython_lib)

from Bio import Phylo
from Bio.Phylo import BaseTree
from StringIO import StringIO

def index():
   # Dump a Bio.Phylo tree object as string
   tree = Phylo.read(StringIO("(A, (B, C), (D, E))"), "newick")
   #tree_str = Phylo.draw_ascii(tree)
   count = BaseTree.TreeMixin.count_terminals(tree)
   #return "<pre>" + str(tree) + "</pre>" 
   return count
