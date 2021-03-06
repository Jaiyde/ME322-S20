import math
class pypipe:
    """pypipe is a python module which calculates head loss for fluid systems. 
    A pypipe is a class object with attributes 
        *diameter
        *length
        *material
        *fluid
    All units must be in SI but later versions should be able to convert between. 
    This class represents a single straight pipe and all head loss calculations possible.   
    """
    version = '0.0.0'
    #class constants
    g = 9.81 #[m/s^2]
    units = 'SI'

    #fluid properties

    # Write a dictionaries with fluid properties in SI a fluid outputs a tuple (density, dynamic viscosity).
    liquids = {'water': (1000, 0.001307),
               'carbon tetrachloride': (1590, 0.000958), # @ 20 C
               'ethyl alcohol': (789, 0.00119),          # @ 20 C
               'gasoline': (680, 0.00031),               # @ 15.6 C
               'glycerin': (1260, 1.5),                  # @ 20 C
               'mercury': (13600, 0.00157),              # @ 20 C
               'SAE 30 oil': (912, 0.38),                # @ 15.6 C
               'seawater': (1030,0.00120) ,              # @ 15.6 C
               'air': (1.247, 0.0000176),                # @ 10 C
               'carbon dioxide': (1.83, 0.0000147),      # @ 20 C
               'helium': (0.166, 0.0000194),             # @ 20 C
               'hydrogen': (0.0838, 0.00000884),         # @ 20 C
               'methane': (0.667, 0.0000110),            # @ 20 C
               'nitrogen': (1.16, 0.0000176),            # @ 20 C
               'oxygen': (1.33, 0.0000204)               # @ 20 C
                } #([kg/m^3], [N s /m^2])

    #material properties 
    roughness = {'commercial steel': 0.045,
                 'riveted steel': 9,
                 'concrete': 3,
                 'wood': 0.9,
                 'cast iron': 0.26,
                 'galvanized iron': 0.15,
                 'drawn tubing': 0.0015,
                 'glass': 0}  # [mm]

    #piping components (K values)
    components = {''}


    #constructor methods
    def __init__(self, diameter, length, material = 'commercial steel', fluid = 'water'):
        self.D = diameter
        self.L = length
        self.e = self.roughness[material]
        self.rho, self.mu = self.liquids[fluid]
        self.Q = 0
        self.V = 0

    def __repr__(self):
        return {'Diameter': self.D, 'Length': self.L, 'Material': self.e, 'Fluid': (self.rho, self.mu)}

    def __len__(self):
        #when calling len() in python on the pipe return the length
        return self.L

    def __str__(self):
        txt = "Diameter:{0}[m]__Length:{1}[m]__Roughness:{2}[mm]"
        return txt.format(self.D, self.L, self.e)

    #class methods
    def setFlowrate(self, flowrate):
        #set a flowrate thru the pipe
        self.Q = flowrate # [m^3/s]
        self.V = 4*flowrate**2/(math.pi * self.D**2) #[m/s]

    def addComponent(self):
        pass

    def effectiveLength(self):
        pass

    def majorLoss(self):
        #calculate the major losses due to overcoming viscous forces
        #throw error if now flowrate has been assigned
        return 8*len(self)*self.Q**2/(math.pi^2 * self.g ** self.D**5)

    def minorLoss(self):
        pass