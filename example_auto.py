import SurveySimulator as ss

# An example of how the Survey Simulator will be used in auto mode

# First let the Survey Simulator know where the definition of the
# survey is
surveypath = '/path/to/pointing.list/directory'
ss.detect.load_survey(surveypath)

filepath = '/path/to/file'
ss.detect.load_file(filepath)

outfilename = 'name_of_output_no_extension')
outputpath = '/path/to/output') # If not specified, writes to current directory
ss.detect.output(outfilename, outputpath=outputpath)

# Specify which, if any, parameters are to be fuzzed
ss.detect.fuzz_objects(('a',10), ('inc', 1, 'abs'), ('e', 0.1))
ss.detect.hdraw(0.9, 13, hmin=2, hbreak=9, contrast=2)

# Specify the number of simulated detections required
# If this method is not called, the Survey Simulator will simply test all
# of the objects in the file and not draw randomly from them
number_of_detections = 1000 
ss.detect.numdetections(number_of_detections)

ss.detect.auto()

