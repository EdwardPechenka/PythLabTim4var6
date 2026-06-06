from handlers import requestSpaceData

def main():
    print("--- NASA Data Retrieval (Open Notify API) ---")
    print("Requesting information about crews in orbit...\n")
    
    data = requestSpaceData()

    if data and data.get('message') == 'success':
        search_craft = input("Enter spacecraft name to filter (e.g., ISS, Tiangong) or press Enter for all: ").strip()
        
        print("\n--- Result ---")
        
        if not search_craft:
            total_people = data['number']
            print(f"Current number of people in space: {total_people}\n")
            print("List of all astronauts:")
            print("=" * 40)
            for person in data['people']:
                print(f"Astronaut: {person['name']}")
                print(f"Spacecraft/Station: {person['craft']}")
                print("-" * 40)
        else:
            filtered_people = [p for p in data['people'] if p['craft'].lower() == search_craft.lower()]
            
            if filtered_people:
                print(f"Current number of people on {search_craft.upper()}: {len(filtered_people)}\n")
                print(f"List of astronauts on {search_craft.upper()}:")
                print("=" * 40)
                for person in filtered_people:
                    print(f"Astronaut: {person['name']}")
                    print("-" * 40)
            else:
                print(f"No astronauts found on spacecraft matching: '{search_craft}'")
            
    else:
        print("Error: Unable to retrieve current space data.")

if __name__ == "__main__":
    main()