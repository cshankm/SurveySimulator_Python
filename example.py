import SurveySimulator as ss

# An example of how the Survey Simulator will be used

# First let the Survey Simulator know where the definition of the
# survey is
path = '/path/to/pointing.list/directory'
ss.detect.load_survey(path)

#Take our friend Drac
a = 45.46
e = 0.553
inc = 103.5 # degrees
Om = 261.024 # degrees
M = 329.635 # degrees
om = 200 # unknown (to wiki) so set to 200
H = 8.81 # (which band?)

candidate = ss.ssobj(a, e, inc, Om, om, H=H, M=M)

# Print the status of the candidate, showing all orbital parameters
print "Original candidate", candidate

# We decide want to randomly perturb (fuzz) a, e, i

# fuzz a by up to +- 10 percent
candidate.fuzz('a', 10)

# fuzz e by up to +- 5 percent
candidate.fuzz('e', 0.05)

#-- note that giving fuzzing percents in decimal or numeric form
#   both work

# fuzz i by up to +- 1 deg
candidate.fuzz('inc', 1, type='abs')

print "Fuzzed candidate", candidate

#-- specify type = 'abs' for absolute fuzzing

# Now imagine we want to draw the H magnitude from a size distribution

# Draw from a single exponential of alpha = 0.9 from in the range 
# H = [1,13]
candidate.drawH(0.9, 13)
print "H drawn from spl", candidate

# Draw from a knee with slopes alpha = 0.9, alpha_faint = 0.5 
# with a break at H = 9 for the range H = [3, 13]
candidate.drawH(0.9, 13, hmin=3, alpha_faint=0.5, hbreak=9)
print "H drawn from knee", candidate

# Draw from a divot with slopes alpha = 0.9, alpha_faint = 0.5
# with a break at H = 9 and a contrast of 15 for H in [3, 13]
candidate.drawH(0.9, 13, hmin=3, alpha_faint=0.5, hbreak=9, contrast=15)
print "H drawn from divot", candidate

# Now we compute the current ephemeris (which actually requires specifying 
# a few things that have yet to be implemented), apparent magnitude so that
# we can then pass this to detect which determines if our survey saw it.
candidate.compute()

ss.detect(candidate)

#and voila, this is how I envision the SS to run
