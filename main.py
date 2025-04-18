from pet import Pet

def main():
    print("Creating pet: Max")
    max_pet = Pet("Max")
    
    max_pet.eat()
    max_pet.play()
    max_pet.sleep()
    
    # Teach two tricks
    max_pet.train("roll over")
    max_pet.train("play dead")

    max_pet.get_status()

if __name__ == "__main__":
    main()
