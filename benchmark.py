#makes the benchmark that will produce the results for a parameter using 1 algorithm.
import os
import subprocess

algorithmFilePath = './codes/quicksort' #path to the algorithm that will be benchmarked (the exe file)
cacheFilePath = './orgb_configs/systems/caches/basic_caches.py' #path to the file where the cpu specs will be
cpuFilePath = './orgb_configs/systems/cpus/MyO3CPU.py' #path to the file where the cache specs will be
parameterVariableName = 'numPhysIntRegs' #variable name in it's specs file (the cpu or cache file)
declarationLine = 167 #line where the interest parameter variable has been declared.
isCacheParameter = False
isCpuParameter = True
initialValue = 50 #parameter's initial value
incrementValue = 5 #parameter's increment value
numIterations = 5 #total number of interations
statsFilePath = 'm5out/stats.txt' #path to the stats.txt file, where the simulation's output will be.
tLine = 3 #line were the execution time will be written in stats.txt at the end of the simulation
ipcLine = 374 #line were the ipc will be written in stats.txt at the end of the simulation
outputDirPath = 'BenchmarkResults' #name of the dir where the IPC and time execution will be written by this program.
outputFileName = 'quicksort-numRegs.txt' #name of the file where the IPC and time execution will be written by this program.
outputFilePath = os.path.join(outputDirPath, outputFileName)

if not os.path.isdir(outputDirPath):
    os.mkdir(outputDirPath)

	
assert (isCacheParameter and isCpuParameter) is False #the parameter can't be simoutaneously a cache and cpu parameter
parameterValue = initialValue
for i in range(numIterations):

	#open the specs file, finds the parameter declaratin, writes the new value, save and close
	if isCacheParameter:
		specsFile = cacheFilePath
	else:
		specsFilepth = cpuFilePath
	
	specsFile = open(specsFilepth, 'r')
	specsFileLines = specsFile.readlines()
	interestLine = specsFileLines[declarationLine] #get the line where the parameter variable is declared.
	commentary = interestLine.split('#')[1]
	command = interestLine.split('#')[0]
	varname = command.split('=')[0]
	replaceLine = varname + ' = ' + str(parameterValue) + '#' + commentary #rewrites the declaration of the variable, setting the new value
	specsFileLines[declarationLine] = replaceLine
	specsFile = open(specsFilepth, 'w')
	specsFile.writelines(specsFileLines) #rewrites all lines in the file, including the modified line.
	
	specsFile.close()
		
	#performs the gem5 console call simulation
	command = './gem5 orgb_configs/simulate.py run-benchmark -c ' + algorithmFilePath
	os.system(command)
	
	#open the simulation output file, search for the desired outputs (ipc and execution time), read them and close
	statsFile = open(statsFilePath, 'r')
	statsLine = statsFile.readlines()
	executionSeconds = statsLine[tLine-1].split()[1]
	executionIpc = subprocess.run(['grep', '-oP','issued_per_cycle::mean\\s+\\K\\w+[.]\w+', statsFilePath], stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1]


	
	statsFile.close()
	
	#open the output file, write the new information, save and close
	outputFile = open(outputFilePath, 'a+')
	outputFile.write('Tempo: '+str(executionSeconds)+' IPC: '+str(executionIpc)+'\n')
	outputFile.close()
	
	#increments the parameter's value
	parameterValue += incrementValue

