README file for the primate tubulins test data set for reconcili-o-tastic

These are test files for reconcili-o-tastic: 
* 4 input gene-tree files 
* a query URL to get the species tree via Rutger's demo 
* the resulting species tree 

The 4 input gene-tree files all have the same OTUs, but with different labels and different formats (2 Newick, 2 NEXUS).  Each one has a gene tree for tubulins from a subset of primates. These were produced by NCBI's BLAST tree viewer, and slightly edited to correct an anomaly in one of the names auto-generated by NCBI.  

History (not important for the test itself).  This was a nightmare to produce.  I picked a starting protein sequence in a mammalian order, then went to BLAST and did a taxonomically restricted search within that order.  For some cases with tubulins and actins, I found a good number of sequences with lots of paralogy.  Then when I tried to find the resulting species in the mammal tree using Rutger's server, I got low coverage.  

So then I went to the original Bininda-Emonds tree to find out from the start what were some of the mammalian species in the tree, e.g., in Carnivora or Primates.  

Then I just re-did the BLAST search but restricting it to the list of species that I knew were in the mammal tree, or including a higher taxon but excluding lower taxa that I knew were not in the tree.  This had unpredictable results-- I tried it several times and the result was that I got far fewer species than expected, e.g., expected 7 different carnivores with actins, but ended up getting only 2 different species.  This may have something to do with using RefSeq or NR in order to avoid partials or duplicates.  

 