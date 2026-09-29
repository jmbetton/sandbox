# Given an array of positive integers 
# Return the number of elements that are strictly greater than the average of the previous elements
# Skip the first value


def countResponseTimeRegressions(responseTimes):
    greater = 0
    for i in range(len(responseTimes)):
        if i == 0:
            continue
        average = (sum(responseTimes[0:i]) / len(responseTimes[0:i]))
        if responseTimes[i] > average:
            greater += 1
    
    return greater
        
        