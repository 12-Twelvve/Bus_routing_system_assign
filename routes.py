# program to determine which  routes would most benefit from additional busses.
import re 
r_routes = re.compile('[0-9]+,(\d*\.)?\d+')
# routesData file
file = 'routes.txt'
# list of routes
def read_route_data(file):
    try :
        routes = []
        # open file routes.txt
        with open(file, 'r') as rf:
            # loop through each line
            for lin in rf:
                # dictionary
                eachDict = {}
                # check for an error
                if r_routes.match(lin):
                    l = lin.split(",")
                    route_number = l[0]
                    happy_ratio = l[1].strip()
                    # check for duplicate
                    for route in routes:
                        if route_number == route['route_number']:
                            raise Exception('Dublicate routes Data')
                    # return the list of dictionaries
                    eachDict['route_number']=route_number
                    eachDict['happy_ratio']=happy_ratio
                    routes.append(eachDict)
                else:
                    raise Exception("Invalid data format")
        return routes 

    except Exception as e:
        raise Exception(e)
def sort_route_data(routes):
    return sorted(routes, key=lambda route: route['happy_ratio'])

def ask_route_number():
    pas =False
    while not pas:
        try:
            rn = input('How many routes can have an extra bus?')
            if 0<=int(rn)<=len(routes):
                pas = True
                return rn
            else:
                print('Invalid value.Please enter a non-negative integer')
        except Exception as e:
            print('Invalid value.Please enter a non-negative integer')
            pass
try:
    routes = read_route_data(file)
    sorted_routes = sort_route_data(routes)
    n = int(ask_route_number())
    # for zero at the end
    sorted_routes_without_zeros = [i for i in sorted_routes if float(i['happy_ratio'])!=float(0)]
    sorted_routes_only_zeros = [i for i in sorted_routes if float(i['happy_ratio'])==float(0)]
    sorted_data =sorted_routes_without_zeros + sorted_routes_only_zeros
    for sr in sorted_data:
        if n<=0:
            break
        print(sr['route_number'])
        n-=1
except Exception as e:
    print(e)
