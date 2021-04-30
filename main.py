import Person as human
import ClinicTime

def main():
    print("Testing")
    p = human.Person('Ben Espiritu', 19, '09195494610', 'Tondo')
    
    print(p.name, p.age, p.contact_num, p.address)
    print(p)


if __name__ == "__main__":
    main()