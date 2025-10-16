import logging
from . import config
from ortools.sat.python import cp_model

logger = logging.getLogger(__name__)

def building_model(required_groups, sport_fest, semestrs = config.SEMESTRS, slots = config.SLOTS):
    
    cources = []
    for sport, amount in required_groups.items():
        for i in range(int(amount)):
            cources.append(f"{sport}_{i+1}")
    
    
    model = cp_model.CpModel()
    X = {}
    for c in cources:
        for s in semestrs:
            for slot in slots:
                X[c,s,slot] = model.NewBoolVar(f"x_{c}_s{s}_p{slot}")
                
    for c in cources:
        model.Add(sum(X[c,s,slot] for s in semestrs for slot in slots) == 1)
        
    for s in semestrs:
        for slot in slots:
            model.Add(sum(X[c,s,slot] for c in cources) <= 1)
    
    sports = {}
    for cource in cources:
        sport = cource.split('_')[0]
        sports.setdefault(sport, []).append(cource)
    
    for sport, c_list in sports.items():
        for s in semestrs:
            model.Add(sum(X[c,s,slot] for c in c_list for slot in slots) <= 1)
            
    if sport_fest and config.FIXED_SPORT in sports:
        la_cource = sports[config.FIXED_SPORT][0]
        model.Add(X[la_cource, semestrs[0], slots[0]] == 1)
    
    if sport_fest and config.FIXED_SPORT in sports:
        for s in semestrs:
            for slot in slots:
                if not (s == semestrs[0] and slot == slots[0]):
                    model.Add(sum(X[c,s,slot] for c in sports[config.FIXED_SPORT]) == 0) 
        
    for s in semestrs:
        model.Add(sum(X[c,s,slot] for c in cources for slot in slots) == 3)
        
    solver = cp_model.CpSolver() 
    solver.parameters.max_time_in_seconds = 10 
    solver.parameters.num_search_workers = 8 
    status = solver.Solve(model)
    
    schedule = {s: {slot : None for slot in slots} for s in semestrs}
    for c in cources:
        sport = c.split('_')[0]
        for s in semestrs:
            for slot in slots:
                if solver.Value(X[c,s,slot]) == 1:
                    schedule[s][slot] = sport
    
    logger.debug(f"schedule - {schedule}")

    return schedule