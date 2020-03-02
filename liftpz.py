import timeit
import sys
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
    
    #update the left ppl in the floor after people got in the lift
    def eliminate(self, people:list, floor:int):
        new_queue = list(self.queues[floor])
        #for floor in [pf for pf in  self.lift if pf in range(len(queues))]:
        for p in people:
            new_queue.remove(p)
        #update the floor with the new value
        self.queues.update({floor:tuple(new_queue)})

    #check if the person in the queues wanna go to the direction that lift is currently heading
    def check_floor(self,people):
        return True if (people < self.currentFloor and self.direction == 0 or people > self.currentFloor and self.direction == 1) else False
            
    #change lift direction
    def change_direction(self):
        self.direction = 1 - self.direction

    #add people to the lift and remove the people in the queues
    def fill_lift(self, floor):
        got_in = []
        for p in self.queues[floor]:
            if len(self.lift) < self.capacity and self.check_floor(p):
                self.lift.append(p)
                got_in.append(p)
        self.eliminate(got_in, floor)

    #getitng people out from the lift
    def checkout_ppl(self, floor):
        new_lift = []
        test = []
        for i, ppl in enumerate(self.lift):
            if ppl != floor:
                new_lift.append(ppl)
            else:
                test.append(ppl)
        self.lift = new_lift

    #move lift up by one floor
    def move_up(self, floor,lift):
        for fl in range(floor+1,self.topFloor+1):
            if (len(self.queues[fl]) != 0 and max(self.queues[fl]) >fl) or (fl in lift):
                if floor != fl:
                    self.currentFloor = fl
                break

        if self.currentFloor == floor:
            self.change_direction()
            self.move_down(self.topFloor+1,lift)


    #move lift down by one floor
    def move_down(self, floor, lift):
        for fl in range(floor-1,self.botFloor-1,-1):
            if (len(self.queues[fl]) != 0 and min(self.queues[fl])<fl) or fl in lift:
                if fl != floor:
                    self.currentFloor = fl
                break
        
        if self.currentFloor == floor:
            self.change_direction()
            self.move_up(self.botFloor-1,lift)

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
                    self.checkout_ppl(self.currentFloor) #get people of the lift when reached their destination
                else:
                    self.change_direction()

            elif self.direction == 0:
                self.fill_lift(self.currentFloor)
                if self.currentFloor > self.botFloor:
                    self.move_down(self.currentFloor,self.lift)
                    self.checkout_ppl(self.currentFloor)
                else:
                    self.change_direction()
            
            if working_floor != self.currentFloor:
                self.stops.append(self.currentFloor)

            #returns to the ground floor when there is no queue of ppl
            if self.all_floors_are_empty() and len(self.lift)==0:
                all_not_empty = False
                if self.stops[-1] != 0:
                    self.currentFloor = self.botFloor
                    self.stops.append(self.currentFloor)
        return self.stops


if __name__ == "__main__":
    test = Dinglemouse(((3, 3, 3, 3, 3, 3), (), (), (), (), (), ()),5)
    print("Finished in: ",timeit.Timer(test.theLift).timeit(1))