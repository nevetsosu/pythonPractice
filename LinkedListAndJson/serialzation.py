from LinkedList import LinkedList
import pickle

def main():
    LL = LinkedList(True, True)
    LL.append_node(123)

    json_data = pickle.dumps(LL)

    file = open("data", "wb")
    file.write(json_data)

    file.close()

    try:
        file = open("dataa", "rb")
        data = file.read()
        file.close()    
        print(pickle.loads(data))
    except OSError:
        print("Could not open file!")
    
if __name__ == "__main__": main()