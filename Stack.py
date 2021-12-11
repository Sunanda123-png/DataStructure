import logging
from self import self

logging.basicConfig(filename="Stack.log", filemode="w")


class Stack:

    def __init__(self):
        self.stack = []

    def push(self):
        """
        :return:
        """
        element = input("Enter the element")
        self.stack.append(element)
        print(self.stack)

    def pop(self):
        """
        :return:
        """
        if not self.stack:
            print("Stack is empty")
        else:
            e = self.stack.pop()
            print("remove element:", e)
            print(self.stack)


if __name__ == "__main__":

    st = Stack()
    try:
        while True:
            print("Select the operation 1.Push 2.Pop 3.Quit")
            choice = int(input())
            if choice == 1:
                st.push()
            elif choice == 2:
                st.pop()
            elif choice == 3:
                break
            else:
                print("Enter correct operation!")
        st.push()
        st.pop()
    except ValueError:
        logging.exception("Type propper value")
