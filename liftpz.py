import timeit
class Dinglemouse:
    def __init__(self, queues:tuple, capacity:int):
        self.queues = dict(zip(range(len(queues)), queues))
        self.capacity = capacity
        self.currentFloor = 0
        self.lift = []
        self.direction = 1 #1 means lift is going up and 0 means is going down direction
        self.stops = [0] # which floors did the lift stop
        self.topFloor = len(queues)-1
        self.botFloor = 0
    
    def eliminate(self, people:list, floor:int): #update the left ppl in the floor after people got in the lift
        new_queue = list(self.queues[floor])
        for p in people:
            new_queue.remove(p)
        self.queues.update({floor:tuple(new_queue)}) #update the floor with the new value

    def check_floor(self,people): #check if the person in the queues wanna go to the direction that lift is currently heading
        return True if (people < self.currentFloor and self.direction == 0 or people > self.currentFloor and self.direction == 1) else False
            
    def change_direction(self): #change lift direction
        self.direction = 1 - self.direction

    def fill_lift(self, floor): #add people to the lift and remove the people in the queues
        got_in = []
        for p in self.queues[floor]:
            if len(self.lift) < self.capacity and self.check_floor(p):
                self.lift.append(p)
                got_in.append(p)
        self.eliminate(got_in, floor)

    def checkout_ppl(self, floor): #getitng people out from the lift
        self.lift = [ppl for ppl in self.lift if ppl != floor]

    def move_up(self, floor,lift): #move lift up by one floor
        for fl in range(floor+1,self.topFloor+1):
            if (len(self.queues[fl]) != 0 and max(self.queues[fl]) >fl) or (fl in lift):
                if floor != fl:
                    self.currentFloor = fl
                break

    def move_down(self, floor, lift): #move lift down by one floor
        for fl in range(floor-1,self.botFloor-1,-1):
            if (len(self.queues[fl]) != 0 and min(self.queues[fl])<fl) or fl in lift:
                if fl != floor:
                    self.currentFloor = fl
                break

    def all_floors_are_empty(self):
        return all([True if len(ppl) == 0 else False for floor,ppl in self.queues.items()])

    def in_between_are_empty(self, floor, nearest):
        return all([True if len(self.queues[floor]) == 0 else False for floor in range(floor+1, nearest+1)])

    def theLift(self):
        all_not_empty = True
        while all_not_empty:
            working_floor = self.currentFloor
            if self.direction == 1: #and self.currentFloor <= self.topFloor:
                self.fill_lift(self.currentFloor) #making people get in the lift
                if self.currentFloor < self.topFloor:   #moving lift up
                    self.move_up(self.currentFloor,self.lift)
                    if working_floor == self.currentFloor:
                        self.change_direction()
                        self.move_down(self.topFloor+1,self.lift)
                    self.checkout_ppl(self.currentFloor) #get people of the lift when reached their destination
                else:
                    self.change_direction()

            elif self.direction == 0:
                self.fill_lift(self.currentFloor)
                if self.currentFloor > self.botFloor:
                    self.move_down(self.currentFloor,self.lift)
                    if self.currentFloor == working_floor:
                        self.change_direction()
                        self.move_up(self.botFloor-1,self.lift)
                    self.checkout_ppl(self.currentFloor)
                else:
                    self.change_direction()
            
            if working_floor != self.currentFloor:
                self.stops.append(self.currentFloor)

            if self.all_floors_are_empty() and len(self.lift)==0: #returns to the ground floor when there is no queue of ppl
                all_not_empty = False
                if self.stops[-1] != 0:
                    self.currentFloor = self.botFloor
                    self.stops.append(self.currentFloor)
        return self.stops

if __name__ == "__main__":
    test = Dinglemouse(((3, 3, 3, 3, 3, 3), (), (), (), (), (), ()),5)
    print("Finished in: ",timeit.Timer(test.theLift).timeit(1))