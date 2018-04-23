from iceconnect import *
svarid = 0
while svarid != "exit":
    valmyndGUI()
    svarid = input("Sláðu inn valmöguleikann sem þú vilt (1 - 3): ")
    print("\n")

    if svarid == "1":
        places = PlaceDB()
        CrudGUI()
        CrudSvar = input("Sláðu inn valmöguleikann sem þú vilt (C,R,U,D): \n")

        if CrudSvar == "c" or CrudSvar =="C":
            Place_name_crud = input("Name of Place: ")
            Place_region_crud = input("Place region: ")
            Place_population_crud = input("Place population: ")
            Place_web_crud = input("Place webpage URL: ")
            Place_latitude_crud = input("latitude: ")
            Place_longitude_crud = input("longitude: ")
            places.add_place(Place_name_crud, Place_region_crud, Place_population_crud, Place_web_crud, Place_latitude_crud, Place_longitude_crud)

        elif CrudSvar == "r" or CrudSvar =="R":
            placelist = places.get_place_list()
            print("--- THE PROGRAM WILL NOW PRINT ALL THE PLACES IN THE DATABASE ---")
            for p in placelist:
                print(p[0] + " , " + p[1] + " , " + p[2] + "\n")
                print("-----------------------------------------------------------")

        elif CrudSvar == "u" or CrudSvar =="U":
            #Place_name_select = input("Name of the place you want to update: ")
            Place_name_crud = input("Name of Place: ")
            Place_region_crud = input("Place region: ")
            Place_population_crud = input("Place population: ")
            Place_web_crud = input("Place webpage URL: ")
            places.update_place(Place_name_crud,Place_region_crud,Place_population_crud,Place_web_crud)

        elif CrudSvar == "d" or CrudSvar =="D":
            Place_id_crud = input("ID of place to be deleted: ")
            places.delete_place(Place_id_crud)

    elif svarid == "2":
        hotels = HotelDB()
        CrudGUI()
        CrudSvar = input("Sláðu inn valmöguleikann sem þú vilt (C,R,U,D): \n")

        if CrudSvar == "c" or CrudSvar == "C":
            Hotel_name_crud = input("Name of Hotel: ")
            Hotel_adress_crud = input("Hotel adress: ")
            Hotel_manager_crud = input("Hotel manager ")
            Hotel_web_crud = input("Hotel website URL: ")
            Hotel_email_crud = input("Hotel email: ")
            Hotel_phone_crud = input("Hotel Phone: ")
            Hotel_dist_crud = input("Hotel dist: ")
            hotels.add_hotel(Hotel_name_crud,Hotel_adress_crud,Hotel_manager_crud,Hotel_web_crud,Hotel_email_crud,Hotel_phone_crud,Hotel_dist_crud)

        elif CrudSvar == "r" or CrudSvar == "R":
            hotellist = hotels.get_hotel_list()
            print("--- THE PROGRAM WILL NOW PRINT ALL THE HOTELS IN THE DATABASE ---")
            for p in hotellist:
                print(p[0] + " , " + p[1] )
                print("-----------------------------------------------------------")

        elif CrudSvar == "u" or CrudSvar == "U":
            # Place_name_select = input("Name of the place you want to update: ")
            Hotel_id_crud = input("Hotel id: ")
            Hotel_name_crud = input("Name of hotel: ")
            Hotel_adress_crud = input("Hotel adress: ")
            Hotel_manager_crud = input("Hotel manager ")
            Hotel_web_crud = input("Hotel website URL: ")
            Hotel_email_crud = input("Hotel email: ")
            Hotel_phone_crud = input("Hotel Phone: ")
            Hotel_dist_crud = input("Hotel dist: ")
            hotels.update_hotel(Hotel_id_crud,Hotel_name_crud,Hotel_adress_crud,Hotel_adress_crud,Hotel_web_crud,Hotel_email_crud,Hotel_phone_crud,Hotel_dist_crud)

        elif CrudSvar == "d" or CrudSvar == "D":
            Hotel_id_crud = input("ID of Hotel to be deleted: ")
            hotels.delete_hotel(Hotel_id_crud)

    elif svarid == "3":
        restaurants = RestaurantDB()
        CrudGUI()
        CrudSvar = input("Sláðu inn valmöguleikann sem þú vilt (C,R,U,D): \n")

        if CrudSvar == "c" or CrudSvar == "C":
            Res_name_crud = input("Name of Restaurant: ")
            Res_cusine_crud = input("Main cusine: ")
            Res_capacity_crud = input("Max Capacity: ")
            Res_adress_crud = input("Restaurant adress: ")
            Res_manager_crud = input("Restaurant manager ")
            Res_web_crud = input("Restaurant website URL: ")
            Res_phone_crud = input("Restaurant Phone: ")
            Res_dist_crud = input("Restaurant dist: ")
            restaurants.add_restaurant(Res_name_crud,Res_cusine_crud,Res_capacity_crud,Res_adress_crud,Res_manager_crud,Res_web_crud,Res_phone_crud,Res_dist_crud)

        elif CrudSvar == "r" or CrudSvar == "R":
            RestaurantList = restaurants.get_restaurant_list()
            print("--- THE PROGRAM WILL NOW PRINT ALL THE RESTAURANT IN THE DATABASE ---")
            for p in RestaurantList:
                print(p[0] + " , " + p[1])
                print("-----------------------------------------------------------")

        elif CrudSvar == "u" or CrudSvar == "U":
            # Place_name_select = input("Name of the place you want to update: ")
            Res_id_crud = input("Restaurant ID: ")
            Res_name_crud = input("Name of Restaurant: ")
            Res_cusine_crud = input("Main cusine: ")
            Res_capacity_crud = input("Max Capacity: ")
            Res_adress_crud = input("Restaurant adress: ")
            Res_manager_crud = input("Restaurant manager ")
            Res_web_crud = input("Restaurant website URL: ")
            Res_phone_crud = input("Restaurant Phone: ")
            Res_dist_crud = input("Restaurant dist: ")
            restaurants.update_restaurant(Res_id_crud,Res_name_crud,Res_cusine_crud,Res_capacity_crud,Res_adress_crud,Res_manager_crud,Res_web_crud,Res_phone_crud,Res_dist_crud)

        elif CrudSvar == "d" or CrudSvar == "D":
            Res_id_crud = input("ID of Restaurant to be deleted: ")
            restaurants.delete_restaurant(Res_id_crud)
