import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QFileDialog
import os
import re

#Removes evry signa other than nucleotide ACTG
def Purifier(genome):
    Seq = genome.upper()
    Seq = re.sub("[^ACTG]", "", Seq)
    return Seq

#Changes T to U if sequence origins from NCBI
def NcbiTtoU(genome):
    genome = Purifier(genome).upper()
    seq = re.sub("T", 'U', genome)
    return seq

def Transcription(sequence):

    Seq = Purifier(sequence)

    Length = len(Seq)
    if Length < 2:
        print("Sequence to short! Abort mission!")
        quit()

    n = 1
    z = [Seq[i:i+n] for i in range(0, len(Seq), n)]
    delimiter = ' '
    z = delimiter.join(z)
    t = z.split()
    for index, letter in enumerate(t):
        if letter == "A":
            t[index] = "U"
        elif letter == "T":
            t[index] = "A"
        elif letter == "G":
            t[index] = "C"
        elif letter == "C":
            t[index] = "G"
    t = str(''.join(t))
    return t

def NumberOfNucleotides(t):
    lenght = len(t)
    return lenght

def GCPercentageCount(Seq):
    P = Seq.count('G') + Seq.count('C')
    GC = (P*100)/len(Seq)
    AT = 100 - GC
    return GC

def ATPercentageCount(GC):
    AT = 100 - GC
    return AT

def Translation(sequence):
    Seq = Purifier(sequence)
    Seq = sequence.lower()
    if "t" in Seq:
        Seq = str(Transcription(Seq)).lower()
    n = 3
    t = [Seq[i:i+n] for i in range(0, len(Seq), n)]
    delimiter = ' '
    t = delimiter.join(t)
#transkrypcja:
    t = t.replace('aug', 'M')
    t = t.replace('aua', 'I')
    t = t.replace('auc', 'I')
    t = t.replace('auu', 'I')
    t = t.replace('acu', 'T')
    t = t.replace('acc', 'T')
    t = t.replace('aca', 'T')
    t = t.replace('acg', 'T')
    t = t.replace('aau', 'N')
    t = t.replace('aac', 'N')
    t = t.replace('aaa', 'K')
    t = t.replace('aag', 'K')
    t = t.replace('agu', 'S')
    t = t.replace('agc', 'S')
    t = t.replace('ucg', 'S')
    t = t.replace('uca', 'S')
    t = t.replace('ucu', 'S')
    t = t.replace('ucc', 'S')
    t = t.replace('agg', 'R')
    t = t.replace('aga', 'R')
    t = t.replace('cgg', 'R')
    t = t.replace('cga', 'R')
    t = t.replace('cgc', 'R')
    t = t.replace('cgu', 'R')
    t = t.replace('guu', 'V')
    t = t.replace('guc', 'V')
    t = t.replace('gua', 'V')
    t = t.replace('gug', 'V')
    t = t.replace('gcu', 'A')
    t = t.replace('gcc', 'A')
    t = t.replace('gca', 'A')
    t = t.replace('gcg', 'A')
    t = t.replace('gau', 'D')
    t = t.replace('gac', 'D')
    t = t.replace('gaa', 'E')
    t = t.replace('gag', 'E')
    t = t.replace('ggu', 'G')
    t = t.replace('ggc', 'G')
    t = t.replace('gga', 'G')
    t = t.replace('ggg', 'G')
    t = t.replace('uuu', 'F')
    t = t.replace('uuc', 'F')
    t = t.replace('uua', 'L')
    t = t.replace('uug', 'L')
    t = t.replace('cuu', 'L')
    t = t.replace('cuc', 'L')
    t = t.replace('cua', 'L')
    t = t.replace('cug', 'L')
    t = t.replace('uau', 'Y')
    t = t.replace('uac', 'Y')
    t = t.replace('ugu', 'C')
    t = t.replace('ugc', 'C')
    t = t.replace('ugg', 'W')
    t = t.replace('ccu', 'P')
    t = t.replace('ccc', 'P')
    t = t.replace('cca', 'P')
    t = t.replace('ccg', 'P')
    t = t.replace('cau', 'H')
    t = t.replace('cac', 'H')
    t = t.replace('caa', 'Q')
    t = t.replace('cag', 'Q')
    t = t.replace('uag', '|')
    t = t.replace('uaa', '|')
    t = t.replace('uga', '|')
#deletes additional nucleotides
    t = t.replace("t", "")
    t = t.replace('u', "")
    t = t.replace('c', "")
    t = t.replace('g', "")
    t = t.replace('a', "")
#licza aminowkasów
    t = t.replace(" ", "")
    return t

def ProteinLenght(t):
    if "STOP" in t:
        p1 = len(t)-4
        return p1
    else:
        p2 = len(t)
        return p2

def IterativeNeighbors(pattern, d):
    neighborhood = [pattern]
    neighborhood2 = []
    for x in range(0, d):
        for patterns in neighborhood:
            addon = ImmediateNeigbhors(patterns)
            neighborhood = neighborhood + addon
            for z in neighborhood:
                if z not in neighborhood2:
                    neighborhood2.append(z)
    return neighborhood2

def ImmediateNeigbhors(pattern):
    nuc = "ACGT"
    Neighborhood = [pattern]
    for i in range(len(pattern)):
        symbol = pattern[i]
        for nucleotide in nuc:
            if nucleotide != symbol :
                neighbor = pattern[:i] + nucleotide + pattern[i+1:]
                if neighbor not in Neighborhood:
                    Neighborhood.append(neighbor)
    return Neighborhood

def SymbolToNumbers(symbol):
    if symbol == "A":
        return 0
    elif symbol == "C":
        return 1
    elif symbol == "G":
        return 2
    elif symbol == "T":
        return 3

def PatternToNumber(pattern):
    if len(pattern) <= 0:
        return 0
    symbol = pattern[-1]
    prefix = pattern[:len(pattern) - 1]
    return 4 * PatternToNumber(prefix) + SymbolToNumbers(symbol)

def NumberToSymbol(number):
    if number == 0:
        return "A"
    elif number == 1:
        return "C"
    elif number == 2:
        return "G"
    elif number == 3:
        return "T"

def NumberToPattern (index, k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = index // 4
    r = index % 4
    symbol = NumberToSymbol(r)
    prefixPattern = NumberToPattern(prefixIndex, k-1)
    return prefixPattern + symbol

def ComplementaryReverse(pattern):
    x = pattern
    x = x.upper()

    n = 1
    z = [x[i:i+n] for i in range(0, len(x), n)]
    delimiter = ' '
    z = delimiter.join(z)
    t = z.split()

    for index, letter in enumerate(t):
        if letter == "A":
            t[index] = "T"
        elif letter == "T":
            t[index] = "A"
        elif letter == "G":
            t[index] = "C"
        elif letter == "C":
            t[index] = "G"
    t.reverse()
    t = ''.join(t)
    return t

#Calculates number of differences between to patterns
def HammingDistance(pattern, pattern2):
    diffCount = 0
    y = 0
    for i in pattern:
        if pattern[y] != pattern2[y]:
            diffCount += 1
        y += 1
    return diffCount

#Calculates and return number of times given pattern occured in provided genome
#with d numbers of differences with original pattern allowed
def ApproximatePatternCount(genome, pattern, d):
    appCount = 0
    index = -1
    for i in range(len(genome) - len(pattern)+1):
        pattern2 = genome[i: i + len(pattern)]
        x = HammingDistance(pattern, pattern2)
        index += 1
        if x <= d:
            appCount += 1
    return appCount

#Method that finds given pattern in a genome, returns it loction and cuts this genome accordingly
#Propably based on ApproximatePatterCount()
def restrictionSiteQuery(genome, pattern):
    locList = []
    for i in range(len(genome) - len(pattern)+1):
        pattern2 = genome[i: i + len(pattern)]
        if pattern2 == pattern:
            loc = genome.index(pattern2, i)
            locList.append(loc)
    return locList


def MostFrequentPattern(genome, d, patternLenght):

    frequencyArray = {}
    patterns = []
    output = []

    for i in range(len(genome)-patternLenght+1):
        pattern = genome[i:i + patternLenght]
        patterns.append(pattern)
    for pattern in patterns:
        neighborsList = IterativeNeighbors(pattern, d)
        for z in range(0, len(neighborsList)):
            neighbor = neighborsList[z]
            reverse = ComplementaryReverse(neighbor)
            if neighbor not in frequencyArray:
                frequencyArray[neighbor] = 1
            elif neighbor in frequencyArray:
                frequencyArray[neighbor] += 1
            if reverse not in frequencyArray:
                frequencyArray[reverse] = 1
            elif reverse in frequencyArray:
                frequencyArray[reverse] += 1


    numbers = list(frequencyArray.values())
    max = 0
    for g in numbers:
        if g > max:
            max = g

            for sequence in frequencyArray:
                if frequencyArray.get(sequence) == max:
                    output.append(sequence)
    return output

def SkewDiagram(genome):
    genome = Purifier(genome)
    skew = []
    x = 0
    xAxisList = []
    xAxisIndex = -1
    for i in genome:
        if i == "C":
            x -= 1
            skew.append(x)
            xAxisIndex += 1
            xAxisList.append(xAxisIndex)
        elif i == "G":
            x += 1
            skew.append(x)
            xAxisIndex += 1
            xAxisList.append(xAxisIndex)
        else:
            skew.append(x)
            xAxisIndex += 1
            xAxisList.append(xAxisIndex)
    mini = min(skew)
    indices = [i for i, x in enumerate(skew) if x == mini]
    diag = plt.figure()
    plt.plot(xAxisList, skew, figure = diag)
    plt.xlim(xmin=0)
    diag.savefig('SkewDiagram.png')
    return indices, diag

def MolecularWeight(protSequence):

    molecularWeight = 0

    for aa in protSequence:
        if aa == "A":
            molecularWeight += 89.1
        elif aa == "R":
            molecularWeight += 174.2
        elif aa == "N":
            molecularWeight += 132.1
        elif aa == "D":
            molecularWeight += 133.1
        elif aa == "C":
            molecularWeight += 121.2
        elif aa == "E":
            molecularWeight += 147.1
        elif aa == "Q":
            molecularWeight += 146.2
        elif aa == "G":
            molecularWeight += 75.1
        elif aa == "H":
            molecularWeight += 155.2
        elif aa == "I":
            molecularWeight += 131.2
        elif aa == "L":
            molecularWeight += 131.2
        elif aa == "K":
            molecularWeight += 146.2
        elif aa == "M":
            molecularWeight += 149.2
        elif aa == "F":
            molecularWeight += 165.2
        elif aa == "P":
            molecularWeight += 115.1
        elif aa == "S":
            molecularWeight += 105.1
        elif aa == "T":
            molecularWeight += 119.1
        elif aa == "W":
            molecularWeight += 204.2
        elif aa == "Y":
            molecularWeight += 181.2
        elif aa == "V":
            molecularWeight += 117.1

    return molecularWeight

def SaveDiagram(file_name, figure):
    folderName = QFileDialog.getExistingDirectory(None)
    os.chdir(folderName)
    figure.savefig(file_name)
