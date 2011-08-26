Sometimes you might want to have a working subset of the [Library of Congress Subject Headings](http://en.wikipedia.org/wiki/Library_of_Congress_Subject_Headings) for some SKOS driven applications.

For example at the [Library of Congress](http://loc.gov) there is a government
policy web archive, where it is desirable to catalog portions of the collection
using the [HIVE software](http://code.google.com/p/hive-mrc/), which can load
SKOS RDF.

This command line program uses the OpenSearch API at
id.loc.gov to do a query, page through the results, build up a graph
of the SKOS concepts, and output the graph as RDF/XML.

For example:

    % ./lcsh-subset.py "government policy"

dumps all the SKOS RDF for concepts mentioning beer to the file:

    government_policy.rdf


License: Public Domain
Author: [Ed Summers](mailto:ehs@pobox.com)
