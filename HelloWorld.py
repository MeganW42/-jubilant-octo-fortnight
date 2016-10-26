__author__ = 'bigdata'
import re
import nltk
import pandas
#To be able to read csv formated files, we will first have to import the
#csv module.import csv
#print "the methods of package re which is used for regular expressions"
#print (dir(re))

#print "the methods of package nltk which is a natural language toolkit"
#print (dir(nltk))



#read csv with csv module


#with open('/home/bigdata/data/carehome.csv', 'rb') as f:
   #reader = csv.reader(f)
   #for row in reader:
       #print row

#read csv with pandas module

#chomes = pandas.read_csv('/home/bigdata/data/carehome.csv')

chomes = pandas.read_csv('/home/bigdata/data/small.csv')

#print (chomes)

text = 'Group: South Tyneside Metropolitan Borough Council Person in charge: Dawn Hill (Manager) Local Authority / Social Services: South Tyneside Metropolitan Borough Council (click for contact details) Type of Service: Care Home only (Residential Care) \xe2\x80\x93 Local Authority Owned  30 residents Registered Care Categories*: Mental Health Condition \xe2\x80\xa2 Old Age \xe2\x80\xa2 Physical Disability \xe2\x80\xa2 Sensory Impairment Specialist Care Categories: Hearing Impairment & Deafness \xe2\x80\xa2 Speech Impairment Single Rooms: 30 Rooms with ensuite WC: 1 Latest CQC* Report on Perth Green House: click here * Care Quality Commission (CQC) is responsible for the registration and inspection of social care services in England.'
print (text)

address = 'Charmouth Road Lyme Regis DT7 3HH '

#Postcode
postcode = re.search(r'[A-Z][A-Z][0-9]+\s[0-9][A-Z][A-Z]\s', address, flags=0)
postcode = str(postcode.group())
print postcode

#City
city = re.search(r'\s[A-Z][^-]+[A-Z][A-Z][0-9]+\s[0-9][A-Z][A-Z]\s', address, flags=0)
city = str(city.group())
print city

#Single Rooms
srooms = re.search(r'Rooms:\s[0-9][0-9]', text, flags=0)
sroom=str(srooms.group())
print(sroom)

sroomsno = re.sub(r'Rooms:\s', '', sroom)
print(sroomsno)

#Ensuite Rooms
erooms = re.search(r'ensuite\sWC:\s[0-9]+', text, flags=0)
eroom=str(erooms.group())
print(eroom)

eroomsno = re.sub(r'ensuite\sWC:\s', '', eroom)
print(eroomsno)

#Ages Accepted
ages = str(re.search(r'Ages[0-9][0-9]\+', text, flags=0))
if ages <> 'None':
    print str(ages.group())
else :
    print 'All Ages'

#Support Types
support = re.search(r'Registered\sCare\sCategories[^-]+Single', text, flags=0)
supportTypes = str(support.group())
print(supportTypes)

support = re.sub(r'Single','', supportTypes)
print(support)

support = re.sub(r'\xe2\x80\xa2', '-', support)
print(support)

alcoholDependence = 0
if str(re.search(r'Alcohol\sDependence', support, flags=0)) <> 'None' :
    alcoholDependence = 1
print 'Alcohol Dependence:',alcoholDependence

alzheimers = 0
if str(re.search(r'Alzheimer.s', support, flags=0)) <> 'None' :
    alzheimers = 1
print 'Alzheimer\'s:',alzheimers

anorexia = 0
if str(re.search(r'Anorexia/Bulimia/Self\sHarming', support, flags=0)) <> 'None' :
    anorexia = 1
print 'Anorexia/Bulimia/Self Harming:',anorexia

bipolar = 0
if str(re.search(r'Bipolar/Manic\sDepression', support, flags=0)) <> 'None' :
    bipolar= 1
print 'Bipolar/Manic Depression:',bipolar

cancerCare = 0
if str(re.search(r'Cancer\sCare', support, flags=0)) <> 'None' :
    cancerCare = 1
print 'Cancer Care:',cancerCare

cerebralPalsy = 0
if str(re.search(r'Cerebral\sPalsy', support, flags=0)) <> 'None' :
    cerebralPalsy = 1
print 'Cerebral Palsy', cerebralPalsy

challengingBehaviour= 0
if str(re.search(r'Challenging\sBehaviour', support, flags=0)) <> 'None' :
    sensoryDisorder = 1
print 'Challenging Behaviour', challengingBehaviour

colitis = 0
if str(re.search(r'Colitis\s&\sCrohn\'s\sDisease', support, flags=0)) <> 'None' :
    colitis = 1
print 'Colitis & Crohn\'s Disease', colitis

dementia = 0
if str(re.search(r'Dementia', support, flags=0)) <> 'None' :
    dementia = 1
print 'Dementia:',dementia

downSyndrome = 0
if str(re.search(r'Down\sSyndrome', support, flags=0)) <> 'None' :
    downSyndrome = 1
print 'Down Syndrome:',downSyndrome

drugDependence = 0
if str(re.search(r'Drug\sDependence', support, flags=0)) <> 'None' :
    drugDependence = 1
print 'Dementia:',drugDependence

eatingDisorder = 0
if str(re.search(r'Eating\sDisorder', support, flags=0)) <> 'None' :
    eatingDisorder = 1
print 'Eating Disorder:',eatingDisorder

epilepsy = 0
if str(re.search(r'Epilepsy', support, flags=0)) <> 'None' :
    epilepsy = 1
print 'Epilepsy', epilepsy

headInjury = 0
if str(re.search(r'Head/Brain\sInjury', support, flags=0)) <> 'None' :
    headInjury = 1
print 'Head/Brain Injury:',headInjury

hearingImpairment = 0
if str(re.search(r'Hearing\sImpairment', support, flags=0)) <> 'None' :
    hearingImpairment = 1
print 'Hearing Impairment & Deafness:',hearingImpairment

huntingtonsDisease= 0
if str(re.search(r'Huntington\'s\sDisease', support, flags=0)) <> 'None' :
    huntingtonsDisease = 1
print 'Huntington\'s Disease', huntingtonsDisease

learningDisability = 0
if str(re.search(r'Learning\sDisability', support, flags=0)) <> 'None' :
    learningDisability = 1
print 'Learning Disability:',learningDisability

mentalHealthCondition = 0
if str(re.search(r'Mental\sHealth\sCondition', support, flags=0)) <> 'None' :
    mentalHealthCondition = 1
print 'Mental Health Condition', mentalHealthCondition

motorNeuronDisease = 0
if str(re.search(r'Motor\sNeuron\Disease', support, flags=0)) <> 'None' :
    motorNeuronDisease = 1
print 'Motor Neuron Disease', motorNeuronDisease

multipleSclerosis = 0
if str(re.search(r'Multiple\sSclerosis', support, flags=0)) <> 'None' :
    multipleSclerosis = 1
print 'Multiple Sclerosis:',multipleSclerosis

muscularDystrophy = 0
if str(re.search(r'Muscular\sDystrophy', support, flags=0)) <> 'None' :
    muscularDystrophy = 1
print 'Muscular Dystrophy:',muscularDystrophy

oldAge = 0
if str(re.search(r'Old\sAge', support, flags=0)) <> 'None' :
    oldAge = 1
print 'Old Age:',oldAge

orthopaedic = 0
if str(re.search(r'Orthopaedic', support, flags=0)) <> 'None' :
    orthopaedic = 1
print 'Orthopaedic:',orthopaedic

parkinsonsDisease = 0
if str(re.search(r'Parkinson\'s\sDisease', support, flags=0)) <> 'None' :
    parkinsonsDisease = 1
print 'Parkinson\'s Disease:',parkinsonsDisease

physicalDisability = 0
if str(re.search(r'Physical\sDisability', support, flags=0)) <> 'None' :
    physicalDisability = 1
print 'Physical Disability:',physicalDisability

schizophrenia = 0
if str(re.search(r'Schizophrenia', support, flags=0)) <> 'None' :
    schizophrenia = 1
print 'Schizophrenia:',schizophrenia

sensoryImpairment = 0
if str(re.search(r'Sensory\sImpairment\s[^S]', support, flags=0)) <> 'None' :
    sensoryImpairment = 1
print 'Sensory Impairment:',sensoryImpairment

speechImpairment = 0
if str(re.search(r'Speech\sImpairment', support, flags=0)) <> 'None' :
    speechImpairment = 1
print 'Speech Impairment:', speechImpairment

stroke = 0
if str(re.search(r'Stroke', support, flags=0)) <> 'None' :
    stroke = 1
print 'Stroke:',stroke

substanceMisuse = 0
if str(re.search(r'Substance\sMisuse', support, flags=0)) <> 'None' :
   substanceMisuse = 1
print 'Substance Misuse:',substanceMisuse

#Delete uneccessary columns
del chomes['_source']
del chomes['_widgetName']
del chomes['_resultNumber']
del chomes['_pageUrl']
del chomes['name']

#Change columns to appropriate data types and rename
chomes['Number'] = chomes['_num'].astype('int64')
chomes['Address'] = chomes['address'].astype('str')
chomes['Information'] = chomes['info'].astype('str')

#Remove original columns
del chomes['_num']
del chomes['address']
del chomes['info']

print(chomes.dtypes)
print(chomes)


