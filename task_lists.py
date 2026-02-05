tasklist.py:
-----------
class Task_List():
    """
    Class for different tasks.
    Attributes (class):
        + task_list (list)
        + completed_task_list (list)
    """
    
    task_list = []
    completed_task_list = []
    
class Task():
    """
    Class for different tasks.
    Attributes (instance):
        + task_message (str)
        - task_idd (str)
        - vital_dates (list)
            - date_of_completion (str)
            - date_of_creation (str)
            - deadline (str)
    Methods:
        + __init__(task_message, task_idd, date_of_completion, date_of_creation, deadline): void
        - task_idd(self): str
        - task_idd(self, idd_newval): void
        - vital_dates(self): list
        - vital_dates(self, new_date): void
        + __repr__(self): str
    """
    def __init__(self, task_message, task_idd, date_of_creation, deadline):
        """
        Initializes a new task object
        Args:
            task_message (str)
            task_idd (str)
            date_of_completion (str)
            date_of_creation (str)
            deadline (str)
        """
        self.task_message = task_message
        self.task_idd = task_idd
        self.date_of_completion = None
        self.date_of_creation = date_of_creation
        self.deadline = deadline
        self.vital_dates = [
            self.date_of_completion,
            self.date_of_creation,
            self.deadline
        ]
        Task_List.task_list.append(self)

    @property
    def task_idd(self):
        """Returns the book's tasks idd."""
        return self._task_idd

    @task_idd.setter
    def task_idd(self, val):
        """
        Method to set a valid idd, if not valid, raise an error
        Args:
            val (str)
        Raises:
            ValueError: If the input is a string of 10 numbers, and it doesn't already exist with a current task.
        """
        for tasks in Task_List.task_list:
            if val == tasks.task_idd:
                raise ValueError("WHAT ARE YOU DOING!!!!!!!!!!!")
        count = 0
        for character in val:
            count = count + 1
            if character in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                count = count + 1
        if count != 20:
            raise ValueError("WHAT ARE YOU DOING!!!!!!!!!!!")
        else:
            self._task_idd = val
            
    @property
    def date_of_completion(self):
        """Returns the list with the three important dates."""
        return self._date_of_completion
        
    @date_of_completion.setter
    def date_of_completion(self, val):
        """
        Method to set a valid date, if not valid, raise an error
        Args:
            val (str)
        Raises:
            ValueError: If the input is not in correct date format or a None then it raises an error.
        """
        if val == None:
            self._date_of_completion = val
        else:
            if Task.date_verification(val):
                self._date_of_completion = val
            else:
                raise ValueError("IM ANGRRRRRRRRRYYYYYYYYYYY!")
            
    @property
    def date_of_creation(self):
        """Returns the list with the three important dates."""
        return self._date_of_creation
        
        
    @date_of_creation.setter
    def date_of_creation(self, val):
        """
        Method to set a valid date, if not valid, raise an error
        Args:
            val (str)
        Raises:
            ValueError: If the input is not in correct date format then it raises an error.
        """
        if Task.date_verification(val):
            self._date_of_creation = val
        else:
            raise ValueError("IM ANGRRRRRRRRRYYYYYYYYYYY!")
        
    @property
    def deadline(self):
        """Returns the list with the three important dates."""
        return self._deadline
        
    @deadline.setter
    def deadline(self, val):
        """
        Method to set a valid date, if not valid, raise an error
        Args:
            val (str)
        Raises:
            ValueError: If the input is not in correct date format then it raises an error.
        """
        if Task.date_verification(val):
            self._deadline = val
        else:
            raise ValueError("IM ANGRRRRRRRRRYYYYYYYYYYY!")
        
    @staticmethod    
    def date_verification(val):
        """
        Utility function to verify if the date is provided in the correct format.
        Args:
            val (str)
        Returns
            (bool)
        """
        count = 0
        for character in val:
            count = count + 1
            if count == 2 or count == 5:
                if character != "/":
                    return False
            else:
                if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    return False
                    
        if count != 9:
            return False
        else:
            return True
        

    def __repr__(self):
        """
        Returns developer string for class use.
        Args:
            None
        Returns:
            (str)
        """
        return (
            f"Task(message={self.task_message!r}, "
            f"idd={self.task_idd!r}, "
            f"completion={self.date_of_completion!r}, "
            f"creation={self.date_of_creation!r}, "
            f"deadline={self.deadline!r}, "
            f"date_list={self.vital_dates!r})"
        )

main.py:
-------
from tasklist import Task_List, Task

for i in range(5):
    Task_A = Task("AMONG US", "8222" + str(i) + "22222", "8/17/2028", "1/29/2026",)

Task_B = Task("AMONG US", "8222922222", "8/20/2001", "1/29/2026",)
for i in Task_List.task_list:
    print(i)

