from multiprocessing import Process
from multiprocessing import Condition, Lock
from multiprocessing import Array, Manager
import time
import random


class Table:
    def __init__(self, nump:int, manager):
        self.mutex = Lock()
        self.nump = nump
        self.manager = Manager()
        self.phil = manager.list([False]*nump)
        self.current_phil = None
        self.free_fork = Condition(self.mutex)

    def no_comen_lados(self):
        a = self.current_phil
        dcha = self.num + 1
        izq = self.num -1
        if self.num == 0:
            izq = NPHIL -1
        if self.num == -1:
            dcha = 0
        return not(self.phil[dcha]) and not (self.phil[izq])
        
    def set_current_phil(num):
        self.current_phil = num

    def wants_eat(num):
        mutex.acquire()
        try:
            self.free_fork.wait_for(self.no_comen_lados(self))
            self.phil[num] = True
        finally:
            self.mutex.release()
            
    def wants_think(num):
        self.mutex.acquire()
        try:
            self.phil[num] = False
        finally: 
            self.mutex.acquire()
