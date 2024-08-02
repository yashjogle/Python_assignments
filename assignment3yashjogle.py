class Vehicle: #Vehicle class
    def __init__(self, vehicle_id, make, model, year, category):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.category = category

class VehicleRental: #VehicleRental Class
    def __init__(self): # constructor is used here to directly initialize
        self.vehicles = []
        self.vehicle_set = set()
        self.categorized_vehicles = {}

    def remove_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                self.vehicles.remove(vehicle)
                self.vehicle_set.remove(vehicle_id)
                self.categorize_vehicles()
                print(f"Vehicle {vehicle_id} removed successfully!")
                return
        print("Vehicle not found in the system")
    def list_vehicles(self):
        i1=0
        for i in self.vehicles:
            i1+=1
            print(i1,i.vehicle_id,i.make,i.model,i.year,i.category)
    def add_vehicle(self, vehicle):
        if vehicle.vehicle_id not in self.vehicle_set:
            self.vehicles.append(vehicle)
            self.vehicle_set.add(vehicle.vehicle_id)
            self.categorize_vehicles()
            print(f"Vehicle{vehicle.vehicle_id}added successfully!")
        else:
            print("Vehicle already exists:")        

    def categorize_vehicles(self):
        self.categorized_vehicles = {}
        for vehicle in self.vehicles:
            if vehicle.category not in self.categorized_vehicles:
                self.categorized_vehicles[vehicle.category] = [vehicle]
            else:
                self.categorized_vehicles[vehicle.category].append(vehicle)

    def categorizedVehicles(self):
        for category, vehicles in self.categorized_vehicles.items():
            print(f"Category:{category}")
            for i in vehicles:
                print(i.vehicle_id,i.make,i.model,i.year,i.category)
            print()
    def search_vehicles(self, search_term):
        results = [vehicle for vehicle in self.vehicles if search_term in vehicle.make or search_term in vehicle.model]
        i1=0
        for i in results:
            i1+=1
            print(i1,i.vehicle_id,i.make,i.model,i.year,i.category)

system = VehicleRental() #object creation

while True:
    print("1.Add a vehicle\n2.Remove a vehicle\n3.Search a vehicle\n4.List all \n5.Catogrized\n6.Exit")
    ch=int(input("Enter your choice:"))
    
    if ch==1:
        idv=input("Enter ID for Vehicle:")
        bname=input("Enter vehical Brand:")
        vname=input("Enter vehical name:")
        yearv=input("Enter vehical year:")
        typev=input("Enter vehical category:")
        vehicle1 = Vehicle(idv,bname,vname,yearv,typev)
        system.add_vehicle(vehicle1)
    elif ch==2:
        vid=input('Enter id of vehical to be removed:')
        system.remove_vehicle(vid)
    elif ch==3:
        search=input('Enter vehical to be searched:')
        system.search_vehicles(search)
    elif ch==4:
        system.list_vehicles()
    elif ch==5:
        system.categorizedVehicles()
    elif ch==6:
        print("Exited Successfully")
        break
    else:
        print("Invalid choice")
    



