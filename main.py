import Weapon

skillvals = {'Str': 16, 'Dex': 24, 'Fai': 22, 'Int': 1, 'Arc': 1}

#Logic to mimic google sheets logic
def IF(i, r, s):
    if i:
        return r
    else:
        return s
#Logic to mimic google sheets logic

def SWITCH(i, *a):
    n = True
    for r in range(len(a)):
        if n:
            n = False
            if a[r] == i:
                return a[r + 1]
        else:
            n = True
#Logic to mimic google sheets logic

def ADD(v1, v2):
    return v1 + v2
#Logic to mimic google sheets logic

def MULTIPLY(v1, v2):
    return v1 * v2

#Logic to mimic google sheets logic
def DIVIDE(v1, v2):
    return v1 / v2

#Logic to mimic google sheets logic
def MINUS(v1, v2):
    return v1 - v2

#Logic to mimic google sheets logic
def POW(v1, v2):
    return (v1)**v2

#Formula to calculate elemental damage for a skill
def elcor(e, id, relskill):
    #E = does the skill scale the element, ID = the Scaling ID, RelSkill = SkillLevel
    return IF(
        e == 0, 0,
        SWITCH(
            id, 0,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 18,
                        ADD(
                            25,
                            MULTIPLY(
                                50,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 18, 42)),
                                        1.2)))),
                        MULTIPLY(25, POW(DIVIDE(relskill - 1, 17), 1.2))))), 1,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 20,
                        ADD(
                            35,
                            MULTIPLY(
                                40,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 20, 40)),
                                        1.2)))),
                        MULTIPLY(35, POW(DIVIDE(relskill - 1, 19), 1.2))))), 2,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 20,
                        ADD(
                            35,
                            MULTIPLY(
                                40,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 20, 40)),
                                        1.2)))),
                        MULTIPLY(35, POW(DIVIDE(relskill - 1, 19), 1.2))))), 4,
            IF(
                relskill > 80, ADD(95, MULTIPLY(5, DIVIDE(relskill - 80, 19))),
                IF(
                    relskill > 50,
                    ADD(80, MULTIPLY(15, DIVIDE(relskill - 50, 30))),
                    IF(relskill > 20,
                       ADD(40, MULTIPLY(40, DIVIDE(relskill - 20, 30))),
                       MULTIPLY(40, DIVIDE(relskill - 1, 19))))), 7,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 20,
                        ADD(
                            35,
                            MULTIPLY(
                                40,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 20, 40)),
                                        1.2)))),
                        MULTIPLY(35, POW(DIVIDE(relskill - 1, 19), 1.2))))), 8,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 16,
                        ADD(
                            25,
                            MULTIPLY(
                                50,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 16, 44)),
                                        1.2)))),
                        MULTIPLY(25, POW(DIVIDE(relskill - 1, 15), 1.2))))),
            12,
            IF(
                relskill > 45, ADD(75, MULTIPLY(25, DIVIDE(relskill - 45,
                                                           54))),
                IF(
                    relskill > 30,
                    ADD(55, MULTIPLY(20, DIVIDE(relskill - 30, 15))),
                    IF(relskill > 15,
                       ADD(10, MULTIPLY(45, DIVIDE(relskill - 15, 15))),
                       MULTIPLY(10, DIVIDE(relskill - 1, 14))))), 14,
            IF(
                relskill > 80, ADD(85, MULTIPLY(15, DIVIDE(relskill - 80,
                                                           19))),
                IF(
                    relskill > 40,
                    ADD(60, MULTIPLY(25, DIVIDE(relskill - 40, 40))),
                    IF(relskill > 20,
                       ADD(40, MULTIPLY(20, DIVIDE(relskill - 20, 20))),
                       MULTIPLY(40, DIVIDE(relskill - 1, 19))))), 15,
            IF(
                relskill > 80, ADD(95, MULTIPLY(5, DIVIDE(relskill - 80, 19))),
                IF(
                    relskill > 60,
                    ADD(65, MULTIPLY(30, DIVIDE(relskill - 60, 20))),
                    IF(relskill > 25,
                       ADD(25, MULTIPLY(40, DIVIDE(relskill - 25, 35))),
                       MULTIPLY(25, DIVIDE(relskill - 1, 24))))), 16,
            IF(
                relskill > 80, ADD(90, MULTIPLY(10, DIVIDE(relskill - 80,
                                                           19))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(relskill > 18,
                       ADD(20, MULTIPLY(55, DIVIDE(relskill - 18, 42))),
                       MULTIPLY(20, DIVIDE(relskill - 1, 17)))))))


#Formula to calculate physical damamge for a skill
def physcor(e, id, relskill):
     #E = does the skill scale the phys, ID = the Scaling ID, RelSkill = SkillLevel
    return IF(
        e == 0, 0,
        SWITCH(
            id, 0,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 18,
                        ADD(
                            25,
                            MULTIPLY(
                                50,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 18, 42)),
                                        1.2)))),
                        MULTIPLY(25, POW(DIVIDE(relskill - 1, 17), 1.2))))), 1,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 20,
                        ADD(
                            35,
                            MULTIPLY(
                                40,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 20, 40)),
                                        1.2)))),
                        MULTIPLY(35, POW(DIVIDE(relskill - 1, 19), 1.2))))), 2,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 20,
                        ADD(
                            35,
                            MULTIPLY(
                                40,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 20, 40)),
                                        1.2)))),
                        MULTIPLY(35, POW(DIVIDE(relskill - 1, 19), 1.2))))), 4,
            IF(
                relskill > 80, ADD(95, MULTIPLY(5, DIVIDE(relskill - 80, 19))),
                IF(
                    relskill > 50,
                    ADD(80, MULTIPLY(15, DIVIDE(relskill - 50, 30))),
                    IF(relskill > 20,
                       ADD(40, MULTIPLY(40, DIVIDE(relskill - 20, 30))),
                       MULTIPLY(40, DIVIDE(relskill - 1, 19))))), 7,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 20,
                        ADD(
                            35,
                            MULTIPLY(
                                40,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 20, 40)),
                                        1.2)))),
                        MULTIPLY(35, POW(DIVIDE(relskill - 1, 19), 1.2))))), 8,
            IF(
                relskill > 80, ADD(90, MULTIPLY(20, DIVIDE(relskill - 80,
                                                           70))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(
                        relskill > 16,
                        ADD(
                            25,
                            MULTIPLY(
                                50,
                                MINUS(
                                    1,
                                    POW(MINUS(1, DIVIDE(relskill - 16, 44)),
                                        1.2)))),
                        MULTIPLY(25, POW(DIVIDE(relskill - 1, 15), 1.2))))),
            12,
            IF(
                relskill > 45, ADD(75, MULTIPLY(25, DIVIDE(relskill - 45,
                                                           54))),
                IF(
                    relskill > 30,
                    ADD(55, MULTIPLY(20, DIVIDE(relskill - 30, 15))),
                    IF(relskill > 15,
                       ADD(10, MULTIPLY(45, DIVIDE(relskill - 15, 15))),
                       MULTIPLY(10, DIVIDE(relskill - 1, 14))))), 14,
            IF(
                relskill > 80, ADD(85, MULTIPLY(15, DIVIDE(relskill - 80,
                                                           19))),
                IF(
                    relskill > 40,
                    ADD(60, MULTIPLY(25, DIVIDE(relskill - 40, 40))),
                    IF(relskill > 20,
                       ADD(40, MULTIPLY(20, DIVIDE(relskill - 20, 20))),
                       MULTIPLY(40, DIVIDE(relskill - 1, 19))))), 15,
            IF(
                relskill > 80, ADD(95, MULTIPLY(5, DIVIDE(relskill - 80, 19))),
                IF(
                    relskill > 60,
                    ADD(65, MULTIPLY(30, DIVIDE(relskill - 60, 20))),
                    IF(relskill > 25,
                       ADD(25, MULTIPLY(40, DIVIDE(relskill - 25, 35))),
                       MULTIPLY(25, DIVIDE(relskill - 1, 24))))), 16,
            IF(
                relskill > 80, ADD(90, MULTIPLY(10, DIVIDE(relskill - 80,
                                                           19))),
                IF(
                    relskill > 60,
                    ADD(75, MULTIPLY(15, DIVIDE(relskill - 60, 20))),
                    IF(relskill > 18,
                       ADD(20, MULTIPLY(55, DIVIDE(relskill - 18, 42))),
                       MULTIPLY(20, DIVIDE(relskill - 1, 17)))))))
    
#weapon = Weapon.Weapeon(BasePhys, BaseMag, BaseFir, BaseLit, BaseHol, [StrScalingValue, StrScalesPhys, StrScalesMag, StrScalesFir,StrScalesLit, StrScalesHol] Repeat for dex, fai, int, arc, {PhysScaling Id, MagScaling Id, FirScaling Id, LitScaling Id, HolScaling ID)
weapon = Weapon.Weapeon(177.56,0, 113.85, 0,0,[0.28,1,0,0,0,0],[0.84,1,0,0,0,0],[0.56,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],{'phy':0,'mag':0,'fir':4,'lit':0,'hol':0})
#Calculate total PhysDmg
def getwephisCal(weapon):
    global skillvals
    scals = [weapon.Str,weapon.Dex,weapon.Fai,weapon.Int,weapon.Arc]
    sscals = ["Str","Dex","Fai","Int","Arc"]
    bPhys = weapon.BasePhys
    vals = {}
    k=0
    i = 0
    for scale in scals:
        if scale[1] == 1:
            vals[sscals[i]]=physcor(1,weapon.ids['phy'],skillvals[sscals[i]])
        else:
            vals[sscals[i]]=0
        i+=1
        
    i = 0
    for r in scals:
        k+=IF(bPhys>0,MULTIPLY(bPhys,MULTIPLY(r[0],DIVIDE(vals[sscals[i]],100))),0)
        i+=1
    k += bPhys
    return k
#Calculate total Magic Damage
def getwemagCal(weapon):
    global skillvals
    scals = [weapon.Str,weapon.Dex,weapon.Fai,weapon.Int,weapon.Arc]
    sscals = ["Str","Dex","Fai","Int","Arc"]
    bPhys = weapon.BaseMag
    vals = {}
    k=0
    i = 0
    for scale in scals:
        if scale[2] == 1:
            vals[sscals[i]]=elcor(1,weapon.ids['mag'],skillvals[sscals[i]])
        else:
            vals[sscals[i]]=0
        i+=1
        
    i = 0
    for r in scals:        
        k+=IF(bPhys>0,MULTIPLY(bPhys,MULTIPLY(r[0],DIVIDE(vals[sscals[i]],100))),0)
        i+=1
    k += bPhys
    return k
#Calculate total Fir Damage
def getwefirCal(weapon):
    global skillvals
    scals = [weapon.Str,weapon.Dex,weapon.Fai,weapon.Int,weapon.Arc]
    sscals = ["Str","Dex","Fai","Int","Arc"]
    bPhys = weapon.BaseFir
    vals = {}
    k=0
    i = 0
    for scale in scals:
        if scale[3] == 1:
            vals[sscals[i]]=elcor(1,weapon.ids['fir'],skillvals[sscals[i]])
        else:
            vals[sscals[i]]=0
        i+=1
        
    i = 0
    for r in scals:        
        k+=IF(bPhys>0,MULTIPLY(bPhys,MULTIPLY(r[0],DIVIDE(vals[sscals[i]],100))),0)
        i+=1
    k += bPhys
    return k
#Calculate total Lit Damage   
def getwelitCal(weapon):
    global skillvals
    scals = [weapon.Str,weapon.Dex,weapon.Fai,weapon.Int,weapon.Arc]
    sscals = ["Str","Dex","Fai","Int","Arc"]
    bPhys = weapon.BaseLit
    vals = {}
    k=0
    i = 0
    for scale in scals:
        if scale[4] == 1:
            vals[sscals[i]]=elcor(1,weapon.ids['lit'],skillvals[sscals[i]])
        else:
            vals[sscals[i]]=0
        i+=1
        
    i = 0
    for r in scals:        
        k+=IF(bPhys>0,MULTIPLY(bPhys,MULTIPLY(r[0],DIVIDE(vals[sscals[i]],100))),0)
        i+=1
    k += bPhys
    return k
#Calculate total Holy Damage
def getweholCal(weapon):
    global skillvals
    scals = [weapon.Str,weapon.Dex,weapon.Fai,weapon.Int,weapon.Arc]
    sscals = ["Str","Dex","Fai","Int","Arc"]
    bPhys = weapon.BaseHol
    vals = {}
    k=0
    i = 0
    for scale in scals:
        if scale[5] == 1:
            vals[sscals[i]]=elcor(1,weapon.ids['hol'],skillvals[sscals[i]])
        else:
            vals[sscals[i]]=0
        i+=1
        
    i = 0
    for r in scals:        
        k+=IF(bPhys>0,MULTIPLY(bPhys,MULTIPLY(r[0],DIVIDE(vals[sscals[i]],100))),0)
        i+=1
    k += bPhys
    return k
#Get total ar
def getAr():
    return getwephisCal(weapon)+getwemagCal(weapon)+getwefirCal(weapon)+getwelitCal(weapon)+getweholCal(weapon)
def optimize(levels):
    global skillvals
    skillval = skillvals
    ar = getAr()
    for i in range(levels):
        upskill = "Str"
        for skill in skillval:
            skillvals[skill]+=1
            if ar < getAr():
                upskill = skill
                ar = getAr()
            skillvals[skill]-=1
        skillvals[upskill]+=1
    return skillvals
print(optimize(11))
            
