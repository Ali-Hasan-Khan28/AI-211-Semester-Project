import random
import numpy as np

GENES = {
    1: ["DS211", 3, "khuramm", "Ai"],
    2: ["AI201", 3, "raja", "Ai"],
    3: ["CE222", 3, "taj", "Ai"],
    4: ["A211", 2, "farhan", "Ai"],
    5: ["CS225", 3, "ahsan", "CS"],
    6: ["CS232", 3, "ahsan", "CS"],
    7: ["ES202", 3, "omar", "CS"],
    8: ["CE222", 3, "ghulam", "CS"],
    9: ["CS31", 3, "hanif", "CE"],
    10: ["CS211", 3, "badr", "CE"],
    11: ["CS232", 3, "mohsin", "CE"],
    12: ["MT203", 3, "siraj", "CE"],
    13: ["DS211", 3, "beenish", "DS"],
    14: ["CE222", 3, "junaid", "DS"],
    15: ["cs251", 3, "khurram", "DS"],
    16: ["DS212", 2, "taj", "DS"],
    17: ["CS232", 3, "ghulam", "CS"],
    18: ["AI361", 3, "zahid", "CS"],
    19: ["AI319", 3, "Ahsan", "CS"],
    20: ["AIxx", 3, "ghulam", "CS"],
    21: ["CS325", 3, "junaid", "CE"],
    22: ["CS230", 3, "abbas", "CE"],
    23: ["CE324", 3, "ghulam", "CE"],
    24: ["CSxx+", 3, "zahid", "CE"],
    25: ["CExx+", 3, "Ahsan", "CE"],
    26: ["CS325", 3, "junaid", "Ai"],
    27: ["CS342", 3, "Beenish", "Ai"],
    28: ["CS325", 3, "Zulfiqar", "Ai"],
    29: ["CSxxx", 3, "huma", "Ai"],
    30: ["CS417", 3, "farhan", "Ai"],
    31: ["MT102", 3, "Nasir", "CE"],
    32: ["HM102", 3, "Atta", "CE"],
    33: ["ES111", 3, "Fahad", "CE"],
    34: ["MM102", 3, "Shanza", "CE"],
    35: ["CS112", 3, "Salman", "CE"],
    36: ["Mt102", 3, "Minhaj", "DS"],
    37: ["CS112", 3, "zahid", "DS"],
    38: ["MM101", 3, "Salman", "DS"],
    39: ["HM102", 3, "Jadoon", "DS"],
    40: ["ES111", 3, "Fahad", "DS"],
    41: ["Mt102", 3, "Minhaj", "CS"],
    42: ["CS112", 3, "Qasim", "CS"],
    43: ["MM101", 3, "Shanza", "CS"],
    44: ["HM102", 3, "Hira", "CS"],
    45: ["ES111", 3, "Ahmed", "CS"]
}

POPULATION_SIZE = 10
Lec_5 = []


class Individual(object):
    '''
    Class representing individual in population
    '''

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(self):
        '''
        create random genes for mutation
        '''
        global GENES
        gene = random.choice(list(GENES))
        return gene

    @classmethod
    def create_gnome(self):
        '''
        create chromosome or string of genes
        '''

        gnome_len = 8
        return [self.mutated_genes() for _ in range(gnome_len)]

    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''

        # chromosome for offspring
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):

            # random probability
            prob = random.random()

            # if prob is less than 0.45, insert gene
            # from parent 1
            if prob < 0.45:
                child_chromosome.append(gp1)

            # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.90:
                child_chromosome.append(gp2)

            # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome.append(self.mutated_genes())

        # create new Individual(offspring) using
        # generated chromosome for offspring
        return Individual(child_chromosome)

    def cal_fitness(self):
        '''
        Calculate fitness score, it is the number of
        characters in string which differ from target
        string.
        '''
        fitness = 0

        # Teachers can only give two lectures consecutively
        list1 = []
        for gs in self.chromosome:
            list1.append(GENES[gs][2])

        from itertools import groupby
        count_dups = [sum(1 for _ in group) for _, group in groupby(list1)]

        for i in count_dups:
            if i == 2:
                fitness = fitness+1

        # Students can only take 3 hours lecture consecutively
        list1 = []
        for gs in self.chromosome:
            list1.append(GENES[gs][3])

        from itertools import groupby
        count_dups = [sum(1 for _ in group) for _, group in groupby(list1)]

        for i in count_dups:
            if i == 3:
                fitness = fitness+1

        # check if no credit hour left
        list1 = []
        for gs in self.chromosome:
            list1.append(GENES[gs][1])
        if i in list1:
            if i == 0:
                fitness = fitness+1

        # One teacher can have only one lecture at one lecture hall
        # One faculty can have one class at a time
        teachers = []
        faculties = []

        for gs in self.chromosome:
            teachers.append(GENES[gs][2])

        for gs in self.chromosome:
            faculties.append(GENES[gs][3])

        for i in range(0,len(Lec_5)):
            for j in range(0,8):
                if teachers[j]==GENES[Lec_5[i][j]][2] or faculties[j]==GENES[Lec_5[i][j]][3]:
                    fitness=fitness+1


        listing=[]
        s=0
        if len(Lec_5)!=0:
                new = list(np.concatenate(Lec_5))
                for n in self.chromosome:
                    num = new.count(n)
                    listing.append(num)
                for u in listing:
                    if u>=3:
                        s=s+1
                if s>0:
                    fitness=fitness+1
        return fitness
    

    def minus_ch(ch):
        for gs in ch:
            if GENES[gs][1] != 0:
                GENES[gs][1] -= 1
                #print(GENES[gs][0], GENES[gs][1])
            





def main():
    global POPULATION_SIZE
    # by using this function you can acess variable from outside.

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))


    k = []
    chec=0
    for i in range(0,5):
        for j in range(0, 6):
            if chec==0:
                found = False
            while not found:

                # sort the population in increasing order of fitness score
                population = sorted(population, key=lambda x: x.fitness)
                # if the individual having lowest fitness score ie
                # 0 then we know that we have reached to the targe
                # and break the loop
                if population[0].fitness <= 0:
                    print(123456789765432)
                    chec+=1
                    print(8888888888888888888888888888888888888888888888888888888888888)
                    found = True
                    Individual.minus_ch(population[0].chromosome)
                    Lec_5.append(population[0].chromosome)
                    population.pop(0)
                    break
            
                # Otherwise generate new offsprings for new generatio
                new_generation = []
                # Perform Elitism, that mean 10% of fittest population
                # # goes to the next generation
                s = int((10*POPULATION_SIZE)/100)
                new_generation.extend(population[:s])

                # From 50% of fittest population, Individuals
                # will mate to produce offspring
                s = int((90*POPULATION_SIZE)/100)
                for _ in range(s):
                    parent1 = random.choice(population[:5])
                    parent2 = random.choice(population[:5])
                    child = parent1.mate(parent2)
                    new_generation.append(child)

                population = new_generation

                print("Generation: {}\tString: {}\tFitness: {}".
                    format(generation,(population[0].chromosome),population[0].fitness))

                generation += 1




            else:
                found = False
            for u in range(0,3):

                k.append(Individual(population[0].chromosome))

                population=k
                k=[]

                # sort the population in increasing order of fitness score
                population = sorted(population, key=lambda x: x.fitness)
                # if the individual having lowest fitness score ie
                # 0 then we know that we have reached to the targe
                # and break the loop
                if population[0].fitness <= 0:
                    print(123456789765432)
                    found = True
                    Individual.minus_ch(population[0].chromosome)
                    Lec_5.append(population[0].chromosome)
                    population.pop(0)
                    break
            
                # Otherwise generate new offsprings for new generatio
                new_generation = []
                # Perform Elitism, that mean 10% of fittest population
                # # goes to the next generation
                s = int((10*POPULATION_SIZE)/100)
                new_generation.extend(population[:s])

                # From 50% of fittest population, Individuals
                # will mate to produce offspring
                s = int((90*POPULATION_SIZE)/100)
                for _ in range(s):
                    parent1 = random.choice(population[:5])
                    parent2 = random.choice(population[:5])
                    child = parent1.mate(parent2)
                    new_generation.append(child)

                population = new_generation

                print("Generation: {}\tString: {}\tFitness: {}".
                    format(generation,(population[0].chromosome),population[0].fitness))

                generation += 1


            
        #print("Generation: {}\tString: {}\tFitness: {}".
        #    format(generation,
        #            (population[0].chromosome),
        #             population[0].fitness))
    
    #print(Lec_5)
    print(len(Lec_5))

    for i in range(1,len(GENES)):
        if GENES[i][1]!=0:
            print(GENES[i])
        if GENES[i][1]<0:
            print(1233123)

    represent=[["TIMETABLE FOR LECTURE HALL 1 (FCSE)"],["TIMETABLE FOR LECTURE HALL 2 (FCSE)"],
               ["TIMETABLE FOR LECTURE HALL 3 (FCSE)"],["TIMETABLE FOR ROOM NO 1 (ACB)"],
               ["TIMETABLE FOR ROOM NO 2 (ACB)"],["TIMETABLE FOR ROOM NO 3 (ACB)"]]
    
    #for i in range(0,len(Lec_5)):
    #    if i==4 or i==9 or i==14 or i==19 or i==24 or i==29:
    #        print(Lec_5[i])
    #        print("\n") 
    #    else:
    #        print(Lec_5[i])

    j=0
    pr=[]
    for i in range (0,6):
       j=i
       print(represent[i])
       print(     )
       for f in range(0,6):
           for t in range(0,8):
               temp=GENES[Lec_5[j][t]][0]+"("+GENES[Lec_5[j][t]][3]+")"
               pr.append(temp)
           print(pr)
           pr=[]         
           j=5+j
       print(     )
       print(     )
       print(     )

if __name__ == '__main__':
    main()
