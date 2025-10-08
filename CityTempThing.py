filename = "citytempData.txt"

def loadData():
    data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                city, temp, = line.strip().split(":") 
                data[city] = float(temp)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error has occured:", e)
    return data

def saveData(data):
    with open(filename, "w") as file:
        for city, temp in data.items():
            file.write(f"{city}: {temp} °C\n")

def analyse(data):
    if not data:
        print("There is no data to be analysed.")
        return
    highest = max(data, key=data.get)
    lowest = min(data, key=data.get)
    average = sum(data.values()) / len(data)
    print(f"Highest: {highest} ({data[highest]}°C)")
    print(f"Lowest: {lowest} ({data[lowest]}°C)")
    print(f"average: {average:.2f}°C")

def main():
    data = loadData()
    while True:
        print("\n1. Add Temperature: 2. Analyse: 3. Quit:")
        choice = input("Choose: ")
        if choice == "1":
            while True:
                city = input("City name: (or press Enter to stop) ").strip()
                if city == "":
                    break
                try:
                    temp = float(input("temperature (°C): "))
                    data[city] = temp
                except ValueError:
                    print("Please enter a number.")
                continue
            saveData(data)    
        elif choice == "2":
                analyse(data)
        elif choice == "3":
                print("Program will now close! Goodbye.")
                break
        else:
                print("Invalid Choice.")



if __name__=="__main__":
    main()
