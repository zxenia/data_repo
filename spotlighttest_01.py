__author__ = 'Ksenia'

import json

import spotlight

annotations = spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', 'President Obama on Monday will call '
                                                                               'for a new minimum tax rate for '
                                                                               'individuals making more than '
                                                                               '$1 million a year to ensure '
                                                                               'that they pay at least the same '
                                                                               'percentage of their earnings as '
                                                                               'other taxpayers, according '
                                                                               'to administration officials.', confidence=0.4, support=20)

#print(annotations)
f = open('mydata.txt', 'w')
for item in annotations:
    f.write(str(item) + '\n')
f.close()
#out_file = open('ann_data.txt', 'w') #this code worked
#out_string = str(annotations)
#out_file.write(out_string)


