import os
import collections
import re
OrderedDict = collections.OrderedDict

def summaryInfo(directory,delimeter):
	"Prints summary data on abalone image directories"
	fileNames = os.listdir("./" + directory)
	numbers = [name.split(delimeter, 1)[0] for name in fileNames]
	uniqNumbers = list(OrderedDict.fromkeys(numbers))
	print("Unique tags in folder" + directory)
	print(uniqNumbers)
	print("Total images:")
	print(len(fileNames))
	print("Total Unique Identifiable Tags:")
	print(len(uniqNumbers))

	summary = {
	  'uniqTags':uniqNumbers,
	  'totalImages':len(fileNames),
	  'uniqTagCount':len(uniqNumbers)
	}

	return summary

def intersect(a, b):
	"returns the intersection of two lists"
	return sorted(list(set(a) & set(b)))

def union(a, b):
	"return the union of two lists"
	return sorted(list(set(a) | set(b)))

tagged1yo = summaryInfo('tagged1yoAbalone','IMG')
sept1yr9mo = summaryInfo('September2017RedAbalone1year9monthPhotos','UNADJUSTEDNONRAW')
prespawn = summaryInfo('AbalonePre-spawnPhotos','UNADJUSTEDNONRAW')

#intersect tag arrays
print("Abs with 1y and post 1y tagged images(using nonstandard color tags")
print(intersect(tagged1yo['uniqTags'],sept1yr9mo['uniqTags']))
print(intersect(tagged1yo['uniqTags'],prespawn['uniqTags']))

#filter out letters and intersect tag arrays
print("Abs with 1y and post 1y tagged images(color tag ignored)")
print("Sept1yr9mo:")
print(intersect(tagged1yo['uniqTags'],[re.sub("[^0-9]", "",tag) for tag in sept1yr9mo['uniqTags']]))
print("Prespawn")
print(intersect(tagged1yo['uniqTags'],[re.sub("[^0-9]", "",tag) for tag in prespawn['uniqTags']]))

print("Abs with images in all three folders")
print(intersect(
  intersect(tagged1yo['uniqTags'],[re.sub("[^0-9]", "",tag) for tag in sept1yr9mo['uniqTags']]),
  intersect(tagged1yo['uniqTags'],[re.sub("[^0-9]", "",tag) for tag in prespawn['uniqTags']])
))

print("Full set of uniq tags from images")
fullUniqUnion = list(OrderedDict.fromkeys(union(
  union(tagged1yo['uniqTags'],[re.sub("[^0-9]", "",tag) for tag in sept1yr9mo['uniqTags']]),
  [re.sub("[^0-9]", "",tag) for tag in prespawn['uniqTags']])
))
print(sorted(fullUniqUnion))
print(len(fullUniqUnion))

