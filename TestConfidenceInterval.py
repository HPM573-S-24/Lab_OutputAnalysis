import numpy as np
import matplotlib.pyplot as plt
import InputData as D
import SurvivalModelClasses as Cls

NUM_CIs = 100   # number of confidence intervals to visualize

# create a multi cohort object
multiCohort = Cls.MultiCohort(
    ids=range(0, NUM_CIs),  # [0, 1, 2 ..., NUM_CIs]
    pop_sizes=[D.SIM_POP_SIZE] * NUM_CIs,  # [POP_SIZE, POP_SIZE, ..., POP_SIZE]
    mortality_probs=[D.MORTALITY_PROB] * NUM_CIs)  # [p, p, ....]

# simulate the multiple cohorts
multiCohort.simulate(D.TIME_STEPS)

# create the figure
fig = plt.figure('t-confidence intervals')
plt.title('95% Confidence Intervals')
plt.xlim([0, 2 * 1 / D.MORTALITY_PROB])   # range of x-axis
plt.ylim([0, NUM_CIs+1])            # range of y-axis

# add confidence intervals to the figure
for i in range(0, NUM_CIs):
    # mean survival time
    mean = multiCohort.multiCohortOutcomes.meanSurvivalTimes[i]
    # confidence interval of mean survival time
    CI = multiCohort.multiCohortOutcomes.get_cohort_CI_mean_survival(i, D.ALPHA)
    # plot the confidence interval
    x = np.linspace(CI[0], CI[1], 2)
    y = np.ones(2)
    plt.plot(x, y+i)

# adding a vertical line to show the true survival mean
plt.axvline(1 / D.MORTALITY_PROB, color='b')

# labels
plt.ylabel('Trials')
plt.xlabel('Survival time' + ' (true mean = ' + str(1 / D.MORTALITY_PROB) + ')')
plt.show()