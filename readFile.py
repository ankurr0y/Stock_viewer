

def rFile():
    companies=[]
    with open('company_list.txt') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            companies.append(appender)
    return(companies)

def rFileDates():
    dates=[]
    with open('date_list') as file:
        remove="\n"
        for f in file:
            appender=""
            for j in f:
                if j not in remove:
                    appender=appender+j
            dates.append(appender)
    return(dates)
